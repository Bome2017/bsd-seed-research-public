# Run013 source-preservation baseline

This baseline binds the original Aristotle archive members to the exact
immutable extraction used by the independent PASS audit. A separate fresh
extraction of the original archive was compared recursively with the audited
extraction; all 28 regular files were byte-identical and neither tree contained
a symbolic link.

The original archive member path is the relative path below under
`run013-aristotle-handoff-2026-08-22_aristotle/`. The two digest columns were
computed independently from the fresh archive extraction and the audited
extraction.

| Relative path | Original archive member SHA-256 | Audited extraction SHA-256 | Status |
|---|---|---|---|
| `ARISTOTLE_SUMMARY.md` | `e63fc06504bf5024700b1909dde83b81f9ff7f2c5599d5f423d8a5b756d5363c` | `e63fc06504bf5024700b1909dde83b81f9ff7f2c5599d5f423d8a5b756d5363c` | PRESERVED_BYTE_IDENTICAL; original stale manifest did not enumerate it |
| `PROJECT_MANIFEST.sha256` | `60c6e5ddef0902b715ed2a361818e18b53879a733c2a35af90b27de3bbb08f51` | `60c6e5ddef0902b715ed2a361818e18b53879a733c2a35af90b27de3bbb08f51` | ORIGINAL_STALE_MANIFEST_REPLACED_NOT_SHIPPED |
| `README.md` | `39ec8cd0459306d9f50cf0c0da2aaf858aeaba5affa9ae26c3dbaee9f872f0ab` | `39ec8cd0459306d9f50cf0c0da2aaf858aeaba5affa9ae26c3dbaee9f872f0ab` | PRESERVED_BYTE_IDENTICAL; original stale manifest did not enumerate it |
| `RUN013_FORMALIZATION_REPORT.md` | `b7519917de47babeabac6a429b278e390a9401466c212d5567bd826cf36d84d3` | `b7519917de47babeabac6a429b278e390a9401466c212d5567bd826cf36d84d3` | PRESERVED_BYTE_IDENTICAL |
| `RequestProject/.gitkeep` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | PRESERVED_BYTE_IDENTICAL |
| `RequestProject/Main.lean` | `929b0bddef0b781f3fb42c7a99f252dc0bda7331f698104f7075e12ff637c52d` | `929b0bddef0b781f3fb42c7a99f252dc0bda7331f698104f7075e12ff637c52d` | THEOREM_BEARING_PRESERVED |
| `RequestProject/Run013/Audit.lean` | `3f9462ac658a103805d6f6e1d183a6f2354c57cc565a724635dc78529b1bed9c` | `3f9462ac658a103805d6f6e1d183a6f2354c57cc565a724635dc78529b1bed9c` | THEOREM_BEARING_PRESERVED |
| `RequestProject/Run013/BSDTwoBookkeeping.lean` | `3ba950ac15a1f8299e76efabdac7f412f73ec9f1d23d172525af34a00b02d3fc` | `3ba950ac15a1f8299e76efabdac7f412f73ec9f1d23d172525af34a00b02d3fc` | THEOREM_BEARING_PRESERVED |
| `RequestProject/Run013/Basic.lean` | `4f085a8c7f3cb0621af4341a87a8aed26bde2cee5f0d9148a58a4c3332115947` | `4f085a8c7f3cb0621af4341a87a8aed26bde2cee5f0d9148a58a4c3332115947` | THEOREM_BEARING_PRESERVED |
| `RequestProject/Run013/Curves.lean` | `1d44698f1265873173d8f9c07cca03c345aed8585828404553942d7c9fe55345` | `1d44698f1265873173d8f9c07cca03c345aed8585828404553942d7c9fe55345` | THEOREM_BEARING_PRESERVED |
| `RequestProject/Run013/DualPhiSelmer.lean` | `d5fe8c30c7fc5fa6c5fec8edd83f89a73d0de662083ed04bcd5f9229b770b6f9` | `d5fe8c30c7fc5fa6c5fec8edd83f89a73d0de662083ed04bcd5f9229b770b6f9` | THEOREM_BEARING_PRESERVED |
| `RequestProject/Run013/Family.lean` | `126a208cabdb485e416ede413823a8e1d8b2b8ba824c9d02a7611d646fb28c13` | `126a208cabdb485e416ede413823a8e1d8b2b8ba824c9d02a7611d646fb28c13` | THEOREM_BEARING_PRESERVED |
| `RequestProject/Run013/FullTwoSelmer.lean` | `9caf6cf965b09c2b18c50c188d61940927dac9b287e074ea558b5827d3af825b` | `9caf6cf965b09c2b18c50c188d61940927dac9b287e074ea558b5827d3af825b` | THEOREM_BEARING_PRESERVED |
| `RequestProject/Run013/Isogeny.lean` | `d5883d6454dc5d2a2484ef8a0285c1e5d63e3d2c6c0c1c2c046409b71401d1f9` | `d5883d6454dc5d2a2484ef8a0285c1e5d63e3d2c6c0c1c2c046409b71401d1f9` | THEOREM_BEARING_PRESERVED |
| `RequestProject/Run013/LocalInfinity.lean` | `8fc2a293d66d3fec01f5b232c5845e2d68f0913f5d4ac9a9538cffa26a599d77` | `8fc2a293d66d3fec01f5b232c5845e2d68f0913f5d4ac9a9538cffa26a599d77` | THEOREM_BEARING_PRESERVED |
| `RequestProject/Run013/LocalQ.lean` | `9a68e913a596dc8b07bb4a886d45e6ab937c43d728401e99112d74ef3e1f3100` | `9a68e913a596dc8b07bb4a886d45e6ab937c43d728401e99112d74ef3e1f3100` | THEOREM_BEARING_PRESERVED |
| `RequestProject/Run013/LocalThirtyOne.lean` | `ca34735aa41d5280004903e19b837000d0f1b7428ee05bc0c57225773cea0e4b` | `ca34735aa41d5280004903e19b837000d0f1b7428ee05bc0c57225773cea0e4b` | THEOREM_BEARING_PRESERVED |
| `RequestProject/Run013/LocalTwo.lean` | `3d3bc893d7dff29623cabe2155263ccbdbbf8b581f747e08308d07bd06ea036e` | `3d3bc893d7dff29623cabe2155263ccbdbbf8b581f747e08308d07bd06ea036e` | THEOREM_BEARING_PRESERVED |
| `RequestProject/Run013/Main.lean` | `13b218139711ce07c7ac0fce1ee02bcfd24bcd7e00f066773dd497094dd7d66c` | `13b218139711ce07c7ac0fce1ee02bcfd24bcd7e00f066773dd497094dd7d66c` | THEOREM_BEARING_PRESERVED |
| `RequestProject/Run013/PadicTools.lean` | `630688df129e99e158f3e66ad91adf513a4cf92856c9f517c4c0ec871d4c5ba7` | `630688df129e99e158f3e66ad91adf513a4cf92856c9f517c4c0ec871d4c5ba7` | THEOREM_BEARING_PRESERVED |
| `RequestProject/Run013/PhiSelmer.lean` | `e75602b39d1f986be35cc3200a08df2b1a9f3fa138f226d6853eec3b382488c9` | `e75602b39d1f986be35cc3200a08df2b1a9f3fa138f226d6853eec3b382488c9` | THEOREM_BEARING_PRESERVED |
| `RequestProject/Run013/Selmer.lean` | `4dda4069454b2dd02a7c1a821d0a7e7cf7ecae775147f6e38f9e877f57fa3a0b` | `4dda4069454b2dd02a7c1a821d0a7e7cf7ecae775147f6e38f9e877f57fa3a0b` | THEOREM_BEARING_PRESERVED |
| `RequestProject/Run013/Squareclasses.lean` | `b675c91ebb375be002558cf2990cca7b58557ecb146c72ca12dac1185df33285` | `b675c91ebb375be002558cf2990cca7b58557ecb146c72ca12dac1185df33285` | THEOREM_BEARING_PRESERVED |
| `RequestProject/Run013/Support.lean` | `98805ffbe4d0dcab42a2d0aa7df11c4b93850dd8837b75b3594aa8d19a0f95c1` | `98805ffbe4d0dcab42a2d0aa7df11c4b93850dd8837b75b3594aa8d19a0f95c1` | THEOREM_BEARING_PRESERVED |
| `lake-manifest.json` | `116c6ef00aa899fb38c08c5e4c92c0e434d0e7f9d574fcb5d4d42cc90ffb07cb` | `116c6ef00aa899fb38c08c5e4c92c0e434d0e7f9d574fcb5d4d42cc90ffb07cb` | BUILD_RELEVANT_PRESERVED |
| `lakefile.toml` | `b1481968ce2912f2b85288fc18aa05fb22750e4083f9e03f49f59a8814ba268a` | `b1481968ce2912f2b85288fc18aa05fb22750e4083f9e03f49f59a8814ba268a` | BUILD_RELEVANT_PRESERVED |
| `lean-toolchain` | `db7bb24b756d745bbde83fe92718b51bd3625dae3701ba0f598d0eedcd3f3028` | `db7bb24b756d745bbde83fe92718b51bd3625dae3701ba0f598d0eedcd3f3028` | BUILD_RELEVANT_PRESERVED |
| `run013-aristotle-handoff-2026-08-22.tar.gz` | `652944cf19010247368525f3a68c310c9abc7d3eb20df2a2509c291c5c5d410e` | `652944cf19010247368525f3a68c310c9abc7d3eb20df2a2509c291c5c5d410e` | PRESERVED_BYTE_IDENTICAL |

`.gitignore` was absent from both the original archive and the audited
extraction. No replacement was invented for the successor.

All 19 `.lean` files are classified as theorem-bearing for the preservation
gate. The build-relevant set is those 19 files plus `lakefile.toml`,
`lean-toolchain`, and `lake-manifest.json`, for 22 files total.
