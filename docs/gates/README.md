# Gate Authorization Documents

This directory contains formal governance authorization documents for the TRIZEL framework.

## Gate Index (0–6)

- **Gate 0:** Foundation governance (not yet documented)
- **Gate 1:** Initial authorization (not yet documented)
- **Gate 2:** Data flow authorization (not yet documented)
- **Gate 3A:** Lab Execution Authorization
- **Gate 3B:** Lab Execution Implementation
- **Gate 4:** Presentation authorization (not yet documented)
- **Gate 5:** Execution Authorization (OFF BY DEFAULT)
- **Gate 6:** Interpretation & Publication (not yet documented)

**Note:** Gate-5 remains CLOSED unless START_EXECUTION = TRUE is explicitly signed by the owner.

---

## Gate 3A — Lab Execution Authorization

Gate 3A authorizes controlled execution of analytical workflows within Layer-3 (Laboratory/Analysis) to produce DERIVED artifacts from SNAPSHOT inputs under strict non-interpretive constraints.

**Status:** PENDING APPROVAL  
**Authorization ID:** GATE-3A-LAB-EXEC-001  
**Effective Date:** 2026-01-25

### Documents

1. **[GATE_3A_LAB_EXECUTION_AUTHORIZATION.md](GATE_3A_LAB_EXECUTION_AUTHORIZATION.md)**
   - Primary authorization document
   - Authority statement and scope
   - Input/output contracts
   - Audit requirements
   - Evidence chain model

2. **[GATE_3A_ALLOWED_FORBIDDEN_MATRIX.md](GATE_3A_ALLOWED_FORBIDDEN_MATRIX.md)**
   - Binary reference for permitted/prohibited activities
   - Layer-3 (Laboratory) constraints
   - Layer-2 (Presentation) constraints
   - Compliance quick reference

3. **[GATE_3A_ACCEPTANCE_SIGNOFF_FORM.md](GATE_3A_ACCEPTANCE_SIGNOFF_FORM.md)**
   - Formal acceptance form for human governance approval
   - Precondition verification checklist
   - Scope lock verification
   - Content verification
   - Sign-off block

4. **[GATE_3A_OUTPUT_SCHEMA.md](GATE_3A_OUTPUT_SCHEMA.md)**
   - Definition-only schema examples (NOT executable)
   - derived-manifest.json schema
   - derived-status.json schema (VALID/INVALID/INCONCLUSIVE/PENDING)
   - ro-crate-metadata.json minimal requirements

### Prerequisites

- **Gate 2I-B:** CLOSED (real-data flow established without analysis)
- **Layer-2 Baseline:** layer-2-baseline-v1 (immutable presentation baseline)

### Key Constraints

**Definition-Only:**
- This authorization is documentation-only
- No executable code, workflows, or scripts authorized
- No CI/CD or automation changes
- Implementation requires separate authorization

**Layer Separation:**
- Layer-3 (Lab): Execution, transformation, validation, packaging
- Layer-2 (Presentation): Declarative status only (requires separate Gate 4)

**Non-Interpretive:**
- No interpretation, conclusions, or scientific claims
- No predictions or narrative analysis
- Validation status only: VALID, INVALID, INCONCLUSIVE, PENDING

**Audit Requirements:**
- Complete provenance metadata (source → transformation → output)
- SHA-256 integrity checksums for all artifacts
- Immutable timestamps (ISO 8601 UTC)
- Reproducibility documentation

### External References

- TRIZEL Layer-0 Governance Framework
- RO-Crate Metadata Specification 1.1: https://www.researchobject.org/ro-crate/

---

## Gate 3B — Lab Execution Implementation

Gate 3B defines the deterministic implementation framework for Laboratory (Layer-3) execution to produce DERIVED artifacts from SNAPSHOT inputs under the authorization established by Gate 3A.

**Status:** PENDING APPROVAL  
**Implementation ID:** GATE-3B-LAB-IMPL-001  
**Effective Date:** 2026-01-25

### Documents

1. **[GATE_3B_LAB_EXECUTION_IMPLEMENTATION.md](GATE_3B_LAB_EXECUTION_IMPLEMENTATION.md)**
   - Primary implementation framework document
   - Separation of concerns (authorization vs. implementation vs. execution)
   - Eligible Laboratory repositories
   - Execution boundaries (environment, resource, temporal)
   - Input requirements (SNAPSHOT packages)
   - Output requirements (DERIVED packages)
   - Transformation implementation constraints
   - Validation and quality constraints
   - Audit and reproducibility hooks
   - Evidence chain alignment
   - External dependency framework
   - Non-interpretive constraint enforcement

2. **[GATE_3B_IMPLEMENTATION_MATRIX.md](GATE_3B_IMPLEMENTATION_MATRIX.md)**
   - Deterministic mapping of implementation steps
   - Input-to-output flow (SNAPSHOT → DERIVED)
   - Execution step mapping (validation, transformation, packaging, audit)
   - Validation and transformation boundaries
   - Output artifact structure
   - Audit and reproducibility hooks
   - External dependency mapping
   - Error handling and edge cases
   - Compliance quick reference

3. **[GATE_3B_ACCEPTANCE_SIGNOFF_FORM.md](GATE_3B_ACCEPTANCE_SIGNOFF_FORM.md)**
   - Formal acceptance form for human governance approval
   - Precondition verification (Gate 3A closed)
   - Scope lock verification (definition-only, no execution)
   - Content verification (framework and matrix completeness)
   - Alignment verification (Gate 3A, evidence chain, non-interpretive)
   - Explicit non-execution acknowledgment
   - Sign-off block

### Prerequisites

- **Gate 3A:** CLOSED (authorization for laboratory execution)
- **Gate 2I-B:** CLOSED (real-data flow established; indirect prerequisite)
- **Layer-2 Baseline:** layer-2-baseline-v1 (immutable presentation baseline)

### Key Constraints

**Definition-Only:**
- This framework is documentation-only
- No executable code, workflows, or scripts
- No CI/CD or automation changes
- **Gate 3B does NOT authorize execution**
- **Execution activation requires separate governance authorization**

**Separation of Concerns:**
- **Gate 3A:** WHAT is authorized (scope and boundaries)
- **Gate 3B:** HOW implementation SHALL be structured (this framework)
- **Future Gate:** WHEN execution is activated (NOT authorized herein)

**Implementation Framework:**
- Defines eligible Laboratory repositories
- Defines execution boundaries and isolation
- Defines input validation requirements
- Defines transformation constraints
- Defines output packaging requirements
- Defines audit and reproducibility hooks

**Non-Interpretive:**
- All Gate 3A non-interpretive constraints apply
- No interpretation, conclusions, or scientific claims
- Validation status only: VALID, INVALID, INCONCLUSIVE, PENDING
- Transformation boundaries prohibit interpretive output

**Audit Requirements:**
- Complete provenance chain (source → transformation → output)
- SHA-256 integrity checksums for all artifacts
- Immutable timestamps (ISO 8601 UTC)
- Execution audit trail
- Reproducibility documentation

### External References

- Gate 3A — Lab Execution Authorization
- TRIZEL Layer-0 Governance Framework
- RO-Crate Metadata Specification 1.1: https://www.researchobject.org/ro-crate/

---

## Gate 5 — Execution Authorization (OFF BY DEFAULT)

Gate 5 is an explicit ON/OFF authorization switch that permits controlled execution inside Layer-1 for a bounded topic under a declared methodological contract.

**Status:** DRAFT (NON-EXECUTING)  
**Document ID:** TRIZEL-G5-AUTH-0001  
**Effective State:** CLOSED  
**Created:** 2026-01-30

### Document

1. **[GATE_5_EXECUTION_AUTHORIZATION.md](GATE_5_EXECUTION_AUTHORIZATION.md)**
   - Execution switch (START_EXECUTION = FALSE)
   - Topic and scope lock (moving-target prevention)
   - Allowed inputs (evidence + provenance only)
   - Allowed tools, repositories, and execution boundary
   - Owner authorization requirements
   - Methodological contract (verification-first)
   - Forbidden operations
   - Traceability requirements
   - Gate-6 reminder (interpretation & publication)

### Key Features

**Execution Control:**
- Default state: CLOSED (START_EXECUTION = FALSE)
- Requires explicit owner authorization and signature
- Execution only allowed in Layer-1
- Layer-0 (Governance) and Layer-2 (Presentation) never execute

**Scope Lock:**
- Prevents moving-target drift
- Explicit IN SCOPE / OUT OF SCOPE boundaries
- No new topic IDs, sources, observables, or thresholds without new Gate-5 document

**Evidence Provenance:**
- Only immutable references allowed (DOI / hash / archived package)
- Explicit RAW ledger sources
- No non-declared data sources, web scraping, or ad-hoc datasets

**Methodological Contract:**
- Verification-first (no exploratory inference)
- Explicit claims list (bounded, finite)
- Pre-declared thresholds
- AUTO-DZ-ACT state model: (0/0), (DO/DZ), (DZ), (∞/∞)

**Audit-Readiness:**
- Deterministic run identifiers
- Complete traceability chain
- Linkage to Gate-5 Document ID
- Execution log artifact naming convention

### External References

- TRIZEL Layer-0 Governance Framework
- AUTO-DZ-ACT verification engine family

---

**Repository:** trizel-ai/trizel-core  
**Document Type:** Governance Authorization Index  
**Last Updated:** 2026-01-30
