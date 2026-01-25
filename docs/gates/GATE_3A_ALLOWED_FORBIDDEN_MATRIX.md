# Gate 3A — Allowed/Forbidden Activity Matrix
## Layer-3 Laboratory and Layer-2 Presentation Constraints

**Repository:** trizel-ai/trizel-core  
**Authorization ID:** GATE-3A-LAB-EXEC-001  
**Document Type:** Governance Reference Matrix  
**Effective Date:** 2026-01-25  
**Status:** PENDING APPROVAL

---

## Overview

This matrix provides a **crisp, binary reference** for activities permitted and prohibited under Gate 3A authorization.

**Purpose:**
- Clarify boundaries between authorized and unauthorized activities
- Distinguish Layer-3 (Laboratory) from Layer-2 (Presentation) constraints
- Provide quick-reference for compliance verification

**Critical Principle:**
- If an activity is **not explicitly listed as ALLOWED**, it is **PROHIBITED** by default
- Ambiguous cases require Layer-0 governance clarification before proceeding

---

## 1. Layer-3 (Laboratory) Activities

### 1.1 ALLOWED — Laboratory Execution

The following activities are **PERMITTED** within Layer-3 (Laboratory) under Gate 3A:

| Activity | Description | Constraints |
|----------|-------------|-------------|
| **Execution** | Running analytical workflows and transformations | Must operate on authorized SNAPSHOT inputs only |
| **Transformation** | Converting SNAPSHOT data to DERIVED artifacts | Must document transformation method in provenance |
| **Validation** | Verifying correctness and integrity of outputs | Must produce validation trace (VALID/INVALID/INCONCLUSIVE/PENDING) |
| **Packaging** | Creating DERIVED packages with metadata | Must include complete provenance and integrity checksums |
| **Checksum Generation** | Computing SHA-256 hashes for artifacts | Required for all files in DERIVED packages |
| **RO-Crate Metadata** | Generating RO-Crate metadata packages | Must conform to minimal schema (see GATE_3A_OUTPUT_SCHEMA.md) |
| **Provenance Recording** | Documenting source → transformation → output chain | Required fields: source_package, source_commit, transformation_method |
| **Reproducibility Documentation** | Recording parameters, configurations, tool versions | Recommended for all DERIVED packages |
| **Internal Quality Checks** | Running integrity and consistency tests | Results must be recorded in validation trace |
| **Archival Preparation** | Preparing DERIVED packages for long-term storage | Must maintain all metadata and checksums |

**Scope Constraint:**  
All ALLOWED activities operate **within the laboratory environment only**. Outputs are NOT authorized for public release under Gate 3A.

---

### 1.2 FORBIDDEN — Laboratory Activities

The following activities are **PROHIBITED** within Layer-3 (Laboratory) under Gate 3A:

| Activity | Description | Why Prohibited |
|----------|-------------|----------------|
| **Interpretation** | Drawing scientific conclusions from DERIVED artifacts | Violates non-interpretive constraint |
| **Conclusion Statements** | Asserting outcomes or findings as established facts | Requires Gate 4 (publication) authorization |
| **Scientific Claims** | Making causal, predictive, or explanatory assertions | Interpretive activity outside Gate 3A scope |
| **Prediction** | Forecasting future states or events | Interpretive activity outside Gate 3A scope |
| **Narrative Analysis** | Constructing explanatory stories from data | Interpretive activity outside Gate 3A scope |
| **Hypothesis Testing** | Confirming or rejecting scientific hypotheses | Interpretive activity; violates theory-neutral constraint |
| **Publication** | Releasing DERIVED artifacts to public surfaces | Requires Gate 4 authorization |
| **Dashboard Creation** | Building live or interactive analytical interfaces | Violates non-publication constraint |
| **DOI Registration** | Assigning Digital Object Identifiers to DERIVED artifacts | Requires Gate 4 authorization |
| **Zenodo Deposit** | Uploading DERIVED artifacts to Zenodo | Requires Gate 4 authorization |
| **Public Communication** | Announcing or describing DERIVED artifacts publicly | Requires Gate 4 authorization |

**Violation Consequence:**  
Engaging in ANY FORBIDDEN activity invalidates Gate 3A authorization and triggers governance review.

---

## 2. Layer-2 (Presentation) Activities

**Context:**  
Gate 3A does **NOT** grant Layer-2 publication rights. The matrix below describes what Layer-2 **may** display **IF** separate Gate 4 authorization is granted.

---

### 2.1 ALLOWED — Layer-2 Presentation (Under Future Gate 4 Only)

The following activities **may be permitted** under **separate Gate 4 authorization** (NOT granted under Gate 3A):

| Activity | Description | Constraints |
|----------|-------------|-------------|
| **Declarative Status** | Displaying validation status of DERIVED artifacts | Must use exact terms: VALID, INVALID, INCONCLUSIVE, PENDING |
| **DOI Links** | Providing hyperlinks to archived DERIVED artifacts on Zenodo | Link only; no content display without explicit authorization |
| **Temporal Markers** | Displaying "As of YYYY-MM-DD" timestamps | Must use exact dates; no ranges or approximations |
| **Provenance References** | Citing source SNAPSHOT packages by identifier | Reference only; no content display |
| **Metadata Display** | Showing artifact title, authors, creation date | Metadata only; no analytical results or content |
| **Archive Status** | Indicating whether artifact is archived (e.g., "Available on Zenodo") | Status only; no live updates |

**Critical Requirement:**  
These activities require **explicit Gate 4 authorization**. Gate 3A does **NOT** authorize Layer-2 display.

---

### 2.2 FORBIDDEN — Layer-2 Presentation (Prohibited Under Gate 3A and Beyond)

The following activities are **PROHIBITED** on Layer-2 surfaces, even if Gate 4 authorization is granted:

| Activity | Description | Why Prohibited |
|----------|-------------|----------------|
| **Live Dashboards** | Real-time or auto-updating analytical displays | Violates declarative-only constraint |
| **Runtime Analytics** | Displaying metrics computed on-the-fly | Violates archival/immutable constraint |
| **Operational KPIs** | Showing performance indicators or system metrics | Violates non-operational constraint |
| **Interactive Exploration** | Allowing users to query or filter DERIVED data | Violates declarative-only constraint |
| **Live Data Feeds** | Streaming DERIVED data to public surfaces | Violates archival/immutable constraint |
| **Dynamic Visualizations** | Graphs or charts that update based on user interaction | Violates declarative-only constraint |
| **Search Interfaces** | Allowing searches within DERIVED artifact content | Violates declarative-only constraint |
| **Embedded Analytics** | JavaScript widgets displaying analytical results | Violates declarative-only constraint |

**Rationale:**  
Layer-2 is a **declarative presentation layer** only. Analytical or operational functionality violates the governance boundary between Layer-2 (Presentation) and Layer-3 (Laboratory).

---

## 3. Cross-Layer Constraints

### 3.1 Input/Output Flow

**ALLOWED:**
- Layer-1 (Observatory) → SNAPSHOT → Layer-3 (Laboratory)
- Layer-3 (Laboratory) → DERIVED → Internal Archive
- Internal Archive → (Gate 4) → Layer-2 (Presentation) *(requires Gate 4 authorization)*

**FORBIDDEN:**
- Layer-1 → Layer-2 (direct data flow without Layer-3 processing)
- Layer-3 → Layer-2 (direct output without Gate 4 archival step)
- External Sources → Layer-2 (without Layer-0 authorization and archival)

---

### 3.2 Metadata Requirements

**ALLOWED:**
- Provenance metadata linking DERIVED artifacts to source SNAPSHOT packages
- Integrity checksums (SHA-256) for all artifacts
- Validation traces documenting transformation integrity
- RO-Crate metadata packages for DERIVED artifacts

**FORBIDDEN:**
- Metadata containing interpretive statements or conclusions
- Metadata with missing provenance or integrity fields
- Metadata with live or runtime-computed values
- Metadata without immutable timestamps

---

## 4. External Dependency Constraints

### 4.1 Laboratory Context (Layer-3)

**ALLOWED (with explicit Layer-0 authorization):**
- Access to external data sources for internal analytical purposes
- Use of external libraries or tools (with version pinning)
- Reference to external publications (with DOI or stable identifier)

**FORBIDDEN (default):**
- Incorporating external data without Layer-0 authorization
- Using external sources without immutable archival reference
- Publishing DERIVED artifacts that depend on non-archived external sources

---

### 4.2 Presentation Context (Layer-2)

**ALLOWED (only if separately archived and authorized):**
- Links to archived external sources (Zenodo, DOI-registered archives)
- Citations of external publications (with DOI)

**FORBIDDEN:**
- Live links to external data sources (non-archived)
- Embedded content from external sources
- Dynamic references to external APIs or databases

---

## 5. Temporal Constraints

### 5.1 ALLOWED — Temporal References

| Reference Type | Description | Format |
|----------------|-------------|--------|
| **As-of Date** | Fixed date marking artifact state | "As of YYYY-MM-DD" (ISO 8601) |
| **Creation Timestamp** | Immutable artifact creation time | ISO 8601 UTC timestamp |
| **Archive Date** | Date of Zenodo deposit or archival | ISO 8601 date |

---

### 5.2 FORBIDDEN — Temporal References

| Reference Type | Description | Why Prohibited |
|----------------|-------------|----------------|
| **"Latest"** | References to most recent state | Violates immutability |
| **"Current"** | References to present-time state | Violates immutability |
| **Relative Times** | "X days ago", "Last week" | Violates immutability |
| **Live Timestamps** | Auto-updating time displays | Violates immutability |

---

## 6. Terminology Constraints

### 6.1 ALLOWED — Non-Interpretive Terms

The following terms are **PERMITTED** in DERIVED artifact metadata and documentation:

- "Validation status: VALID"
- "Validation status: INVALID"
- "Validation status: INCONCLUSIVE"
- "Validation status: PENDING"
- "Transformation method: [description]"
- "Source package: [identifier]"
- "Integrity checksum: [SHA-256]"
- "Provenance: [chain]"

---

### 6.2 FORBIDDEN — Interpretive Terms

The following terms are **PROHIBITED** in DERIVED artifact metadata and documentation:

- "Conclusion"
- "Finding"
- "Discovery"
- "Proves"
- "Disproves"
- "Demonstrates"
- "Indicates"
- "Suggests"
- "Implies"
- "Confirms"
- "Rejects"
- "Shows that"
- "Evidence for"
- "Evidence against"

**Exception:**  
Forbidden terms may appear in **citations of external sources** (if properly quoted and attributed) but must NOT appear in TRIZEL-generated statements.

---

## 7. Compliance Quick Reference

### 7.1 Checklist for DERIVED Artifacts

A DERIVED artifact is **COMPLIANT** with Gate 3A if:

- [ ] Contains NO interpretive statements or conclusions
- [ ] Includes complete provenance metadata (source package, commit, method)
- [ ] Includes SHA-256 checksums for all files
- [ ] Includes validation trace (VALID/INVALID/INCONCLUSIVE/PENDING)
- [ ] Includes immutable timestamps (ISO 8601 UTC)
- [ ] Includes RO-Crate metadata package
- [ ] Documents transformation method
- [ ] Documents reproducibility parameters (recommended)
- [ ] NOT published to Layer-2 (unless Gate 4 authorized)
- [ ] NOT registered with DOI (unless Gate 4 authorized)

---

### 7.2 Checklist for Layer-2 Display (Future Gate 4)

A Layer-2 display is **COMPLIANT** with Gate 3A constraints if:

- [ ] Gate 4 authorization has been granted (Gate 3A alone is NOT sufficient)
- [ ] Displays declarative status only (no live analytics)
- [ ] Uses immutable temporal references ("As of YYYY-MM-DD")
- [ ] Provides DOI links only (no content embedding)
- [ ] Contains NO interpretive statements
- [ ] Contains NO live dashboards or runtime metrics
- [ ] Contains NO operational KPIs
- [ ] Contains NO interactive analytical interfaces

---

## 8. Ambiguity Resolution

**Principle:**  
When in doubt, **default to FORBIDDEN** and request Layer-0 governance clarification.

**Examples of Ambiguous Cases:**
- Activity not explicitly listed in ALLOWED matrix → **FORBIDDEN** (request clarification)
- Terminology not listed in ALLOWED or FORBIDDEN → **FORBIDDEN** (request clarification)
- External dependency not explicitly authorized → **FORBIDDEN** (request authorization)

**Clarification Process:**
1. Document the ambiguous case
2. Submit clarification request to Layer-0 governance
3. Wait for explicit authorization before proceeding
4. Document authorization in governance records

---

## 9. Matrix Maintenance

**Update Authority:** Layer-0 governance only  
**Amendment Procedure:** Requires governance approval and version increment  
**Version History:** Maintained in git commit history

**Current Version:** 1.0.0  
**Last Updated:** 2026-01-25

---

**END OF MATRIX DOCUMENT**
