# TRIZEL Observation Sources Registry

This file serves as the canonical governance registry for all official observation sources across TRIZEL layers.

## Purpose

- Formally register raw observation sources (Layer-1)
- Document provenance, integrity, and data authority
- Maintain append-only governance record
- Track gate status for each registered source

## Registry Format

Each registered source must include:
- `repo_id`: Unique repository identifier
- `repository`: GitHub organization/repository
- `layer`: TRIZEL architectural layer (Layer-1, Layer-2, etc.)
- `role`: Data role (raw, transformed, analysis, etc.)
- `instrument`: Source instrument or telescope
- `data_authority`: Authoritative data provider
- `ingestion_mode`: How data is ingested
- `integrity`: Integrity verification method
- `provenance`: Provenance tracking method
- `registered_by`: Registration authority
- `gate_status`: Current governance gate status
- `registration_timestamp_utc`: UTC timestamp of registration

---

## Registered Sources

---
### TESS Sector-1751 (Raw Observation Source)

- repo_id: tess-sector-1751
- repository: trizel-ai/tess-sector-1751-raw
- layer: Layer-1
- role: raw
- instrument: NASA TESS Space Telescope
- sector: 1751
- data_authority: NASA / MAST
- ingestion_mode: automatic (schema discovery)
- integrity: integrity.sha256
- provenance: provenance.json
- registered_by: TRIZEL Governance
- gate_status: Gate-6 (pending)
- registration_timestamp_utc: 2026-02-19T01:27:28Z
