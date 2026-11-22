# Product Update Log

## 2026-11-22
* **Migration**: Migrated the [bundle index](index.md) from OKF v0.2 to v0.3 and added its title and scope description. Checked metadata paths and local links under v0.3 resolution rules. Preserved concept content, source snapshots, and generation metadata. This was structural validation, not a new factual verification.

## 2026-10-21
* **Update**: Changed snapshot links and source resource paths in [source records](references/source-records.md) to document-relative paths.
* **Creation**: Added [overview](/overview.md), [setup and usage](/setup-and-usage.md), [extraction workflow](/extraction-workflow.md), [output format](/output-format.md), [verification](/verification.md), and [limits and troubleshooting](/limits-and-troubleshooting.md), using the supplied extraction README to select documentation themes.
* **Verification**: Ran the existing DocLang checker suite: 10 tests passed with Python 3.9.6. No model inference or official schema validation was performed.
* **Provenance**: Included [source records](/references/source-records.md) and local source snapshots so this product's documentation can be delivered without the other wiki bundles.
