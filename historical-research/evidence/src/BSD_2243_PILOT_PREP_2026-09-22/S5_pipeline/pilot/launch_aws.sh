#!/bin/bash
# launch_aws.sh -- start ONE capped pilot instance on AWS EC2 and run the 2243 pilot on it. DRY RUN unless --launch.
#
# Spend is bounded BY CONSTRUCTION, not by billing alerts (AWS Budgets data lags by hours; set a $100 budget with alerts
# as a second, independent guard -- see PILOT_PROPOSAL.md):
#   * the instance runs `shutdown -h +MAX_MINUTES` from user-data BEFORE anything else, with shutdown behavior = terminate;
#   * spot requests carry MaxPrice = the on-demand price; the root volume is deleted on termination;
#   * one instance per invocation; this script keeps a local ledger (pilot_ledger.txt) of the WORST-CASE spend of every
#     instance it has launched and refuses a launch that would take the ledger total past CAP_USD (default 100).
# Worst case per instance = on-demand $/h x MAX_MINUTES/60 + 100 GB gp3 for that time (+ negligible transfer).
#
# Needs: aws CLI v2 with a profile allowed to run/describe/terminate instances and read the public SSM AMI parameter;
# an existing key pair (KEY + SSH_KEY) and a security group (SG) that allows SSH from your address only.
# Usage:  [KEY=mykey SSH_KEY=~/.ssh/mykey.pem SG=sg-0123 -- required only with --launch] [ITYPE=c7a.16xlarge] [MARKET=spot|on-demand] [MAX_MINUTES=300]
#         [STAGES=P1,P2,P3,P4] [P4_MINUTES=40] [REGION=us-east-1] [ONDEMAND_PRICE=3.2845] ./launch_aws.sh [--launch]
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd); BUNDLE=${BUNDLE:-$HERE/bundle/pilot_bundle_2243.tar.gz}; LEDGER=$HERE/pilot_ledger.txt
REGION=${REGION:-us-east-1}; ITYPE=${ITYPE:-c7a.16xlarge}; MARKET=${MARKET:-spot}; MAX_MINUTES=${MAX_MINUTES:-300}
ONDEMAND_PRICE=${ONDEMAND_PRICE:-3.2845}; CAP_USD=${CAP_USD:-100}; STAGES=${STAGES:-P1,P2,P3,P4}; P4_MINUTES=${P4_MINUTES:-40}
LAUNCH=0; [ "${1:-}" = "--launch" ] && LAUNCH=1
if [ $LAUNCH = 1 ]; then KEY=${KEY:?set KEY (EC2 key pair name)}; SG=${SG:?set SG (security group id)}; SSH_KEY=${SSH_KEY:?set SSH_KEY (private key path)}
  [ -f "$BUNDLE" ] || { echo "missing bundle $BUNDLE (run make_bundle.sh)"; exit 1; }; fi
[ "$MAX_MINUTES" -le 480 ] || { echo "MAX_MINUTES > 480 refused (pilot limit)"; exit 1; }
worst=$(python3 -c "print(round($ONDEMAND_PRICE * $MAX_MINUTES / 60 + 100 * 0.08 * $MAX_MINUTES / 60 / 730, 2))")
spent=$(awk '{s += $NF} END {printf "%.2f", s + 0}' "$LEDGER" 2>/dev/null || echo 0)
echo "PLAN   1 x $ITYPE ($MARKET; spot MaxPrice = on-demand \$$ONDEMAND_PRICE/h) in $REGION, Ubuntu 24.04 amd64, 100 GB gp3"
echo "LIMIT  self-termination after $MAX_MINUTES min; stages $STAGES (P4 $P4_MINUTES min)"
echo "SPEND  worst case this instance \$$worst; ledger so far \$$spent; cap \$$CAP_USD"
python3 -c "import sys; sys.exit(0 if $spent + $worst <= $CAP_USD else 1)" || { echo "REFUSED: ledger + worst case would exceed the cap"; exit 1; }
PRICE=$ONDEMAND_PRICE
if ! command -v aws > /dev/null; then
  echo "AWS    aws CLI not found: live AMI and spot price not shown"
  [ $LAUNCH = 1 ] && { echo "REFUSED: --launch needs the aws CLI (v2), configured"; exit 1; }
  echo "DRY RUN -- nothing started."; exit 0; fi
AMI=$(aws ssm get-parameters --region $REGION --names /aws/service/canonical/ubuntu/server/24.04/stable/current/amd64/hvm/ebs-gp3/ami-id --query 'Parameters[0].Value' --output text)
echo "AMI    $AMI"
if [ "$MARKET" = spot ]; then
  sp=$(aws ec2 describe-spot-price-history --region $REGION --instance-types $ITYPE --product-descriptions Linux/UNIX --max-items 1 --query 'SpotPriceHistory[0].SpotPrice' --output text)
  echo "SPOT   current price \$$sp/h (the pilot's \$/chunk uses it)"; PRICE=$sp; fi
if [ $LAUNCH = 0 ]; then echo "DRY RUN -- nothing started. Re-run with --launch to start the instance."; exit 0; fi
UD=$(mktemp); printf '#!/bin/bash\nshutdown -h +%s\n' "$MAX_MINUTES" > $UD
MKT=(); [ "$MARKET" = spot ] && MKT=(--instance-market-options "MarketType=spot,SpotOptions={MaxPrice=$ONDEMAND_PRICE,SpotInstanceType=one-time,InstanceInterruptionBehavior=terminate}")
IID=$(aws ec2 run-instances --region $REGION --image-id $AMI --instance-type $ITYPE --key-name $KEY --security-group-ids $SG \
      --instance-initiated-shutdown-behavior terminate --user-data file://$UD "${MKT[@]}" \
      --block-device-mappings 'DeviceName=/dev/sda1,Ebs={VolumeSize=100,VolumeType=gp3,DeleteOnTermination=true}' \
      --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=bsd2243-pilot}]' --count 1 --query 'Instances[0].InstanceId' --output text)
echo "$(date -u +%FT%TZ) $IID $ITYPE $MARKET $MAX_MINUTES $worst" >> "$LEDGER"; echo "LAUNCHED $IID (ledger updated)"
aws ec2 wait instance-running --region $REGION --instance-ids $IID
IP=$(aws ec2 describe-instances --region $REGION --instance-ids $IID --query 'Reservations[0].Instances[0].PublicIpAddress' --output text)
echo "IP $IP"; for i in $(seq 1 40); do ssh -o StrictHostKeyChecking=accept-new -o ConnectTimeout=5 -i $SSH_KEY ubuntu@$IP true 2>/dev/null && break; sleep 10; done
scp -i $SSH_KEY "$BUNDLE" ubuntu@$IP:
ssh -i $SSH_KEY ubuntu@$IP "tar xzf $(basename $BUNDLE) && cd pilot_bundle_2243 && nohup bash -c 'scripts/bootstrap.sh && STAGES=$STAGES P4_MINUTES=$P4_MINUTES PRICE_PER_HOUR=$PRICE scripts/pilot_run.sh; sudo shutdown -h +10' > pilot_nohup.log 2>&1 &"
echo "RUNNING. Watch: ssh -i $SSH_KEY ubuntu@$IP tail -f pilot_bundle_2243/results/pilot.log"
echo "Fetch before termination: ./fetch_results.sh $IP   (the machine terminates 10 min after PILOT_DONE, or at the $MAX_MINUTES-min limit)"
