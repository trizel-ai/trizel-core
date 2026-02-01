# TRIZEL — LAB_OPERATION_CONTRACT (Permanent Integration) — V001

Artifact Class: Layer-0 Governance Contract (First-Class)
Scope: Defines permanent, auditable, non-promiscuous laboratory integration for Layer-1 execution.
Authority: Owner decision under Layer-0 (non-executing). This contract itself executes nothing.

Status: ACTIVE (Draft-Executable Specification)
Gate Relation: Gate-5 operational precondition. Gate-6 remains CLOSED.

---

## 1) Purpose

This contract defines the permanent operational integration model by which the Layer-1 laboratory may:
- Access RAW observational repositories, instrument feeds, and agency datasets
- Bind execution to explicit allow-lists, time windows, and provenance checks
- Log ingress and verification without duplicating data
- Preserve strict separation: ingestion ≠ analysis ≠ interpretation

This contract prevents:
- Blind global permissions
- Manual ad-hoc data shuffling
- PR-noise operational drift
- Narrative reconstruction and speculative inference in place of instrument engagement

---

## 2) Non-Negotiable Separation (Binding)

- Layer-0: defines permissions, constraints, and contracts; never executes.
- Layer-1: executes only under Gate-5 authorization and under this contract.
- Layer-2: read-only institutional presentation; DOI references only; no authority; no execution; no inference.

---

## 3) Definitions

Ingress: Acquisition of references and/or content under defined channels with integrity verification and logging.
Data Duplication: Copying or mirroring external datasets into Layer-1 storage beyond minimal cached metadata required for audit.
Verification State: Deterministic state output confirming whether a claim's observable was verified from authorized channels.
Interpretation: Any explanatory narrative, causal hypothesis, or scientific conclusion beyond verification states (Gate-6 domain).

---

## 4) Contract Inputs (Governance-Bound)

This contract binds the following input classes:

A) RAW Repositories (Owner-Originated)
- Example: AUTO-DZ-ACT-3I-ATLAS-DAILY (hashed snapshots; provenance manifests)

B) Instrument Feeds (Read-Only)
- Direct instrument telemetry or measurement registries, where applicable
- Must be accessed via allow-listed endpoints and logged by immutable ingress records

C) Agency Datasets (Read-Only)
- Space agency archives and catalogs
- Must be accessed via allow-listed sources and recorded with immutable retrieval manifests

D) Tools (Execution Utilities)
- Approved tools for retrieval, hashing, manifesting, and deterministic verification
- Tools must be listed with versions and checksums where possible

---

## 5) Access Policy Model (Non-Promiscuous)

Principle: Minimum necessary access. Read-only by default. Explicit allow-lists. Time-window binding.

Policy Rules:
1) No global credentials or broad scopes.
2) Each channel requires explicit allow-list entries (source, endpoint, artifact class).
3) Each execution must bind to:
   - Phenomenon identifier (e.g., Claim-001 observable class)
   - Time window (start_date, end_date)
   - Source allow-list
4) Access tokens/secrets are prohibited in governance artifacts. Secrets must be provisioned outside git with sealed mechanisms.

---

## 6) Time-Window Binding (Mandatory)

Every execution request must declare:
- start_date (ISO-8601)
- end_date (ISO-8601)
- allowable backfill rules (if any)
- a fixed reference clock (UTC)

Execution outside the window is invalid.

---

## 7) Integrity & Provenance (Mandatory)

Ingress must:
- Produce an ingress record per source interaction
- Record:
  - timestamp_utc
  - source_id
  - retrieval method
  - content hash (SHA-256) when content is retrieved
  - manifest hash when manifests exist
  - pointer/URL and immutable identifiers where possible (DOI, dataset version, archive id)
- Verify:
  - hash matches manifest where applicable
  - chronological ordering constraints (when applicable)
  - non-tampering signals

No ingress record => no valid verification.

---

## 8) Logging Model (Ingress Logging, Not Data Duplication)

Allowed:
- Store minimal audit metadata:
  - hashes
  - manifests
  - retrieval receipts
  - normalized pointers
  - deterministic verification outputs

Disallowed:
- Mirroring entire upstream datasets unless explicitly authorized by a separate governance artifact.

---

## 9) Execution Boundary (Verification-Only)

Layer-1 may produce:
- Verification states
- Deterministic pass/fail conditions
- Completeness and coverage metrics for the observable

Layer-1 may not produce:
- Interpretations
- Explanatory narratives
- Causal claims
- Publication artifacts

Interpretation remains Gate-6 CLOSED unless explicitly opened by owner.

---

## 10) Minimal Required Deliverables in Layer-1 (Post-Contract)

Once this contract is ACTIVE, Layer-1 MUST implement:
- A channel registry matching the allow-list
- An ingress ledger (append-only)
- Deterministic verification runners that consume ingress records
- A reproducible execution manifest format
- A denial mode that hard-fails on any policy violation

---

## 11) Compliance & Violation Handling

Any violation yields:
- Execution invalidation
- State marked: NON-COMPLIANT
- Required remediation: new execution under compliant ingress and manifests

No exception handling by convenience. Fail closed.

---

## 12) References (Non-Executing)

This contract references the machine-readable specification:
- ./contracts/LAB_OPERATION_CONTRACT_V001.yaml
- ./schemas/LAB_OPERATION_CONTRACT_V001.schema.json

END OF CONTRACT
