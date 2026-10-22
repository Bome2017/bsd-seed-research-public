# W3 four-value push

Start with REPORT.md; DERIVATION.md contains the written mathematics and ARITHMETIC_CONTINUATION.md states the next arithmetic calculation.

All new mathematical assertions are at written-derivation/imported-theorem grade under retained inputs; independent review is pending. No actual Kato value was computed and no new Sha-vanishing theorem is asserted.

Run the standalone exact controls with:

```bash
python3 four_value.py --self-test
python3 checks/symbolic_check.py
```

The input mode of four_value.py processes four externally supplied, arithmetically certified source residues; it does not certify their provenance. No sample seed residue is fabricated.

The ZIP is the only delivered attachment. Upload status is in UPLOAD_STATUS.json.
