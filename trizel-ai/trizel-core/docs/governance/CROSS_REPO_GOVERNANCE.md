# CROSS-REPO GOVERNANCE
## TRIZEL Ecosystem — Authoritative Coordination Contract

Status: Canonical  
Authority: trizel-ai/trizel-core  
Scope: ALL TRIZEL repositories (personal + organization)  
Effective date: 2026-01-12

---

## 1. PURPOSE

This document defines the single, binding governance contract for coordination across all TRIZEL repositories.

It exists to:
- Eliminate cross-repository ambiguity.
- Prevent local assumptions and fragmented decision-making.
- Enforce deterministic, auditable, and reproducible operation.
- Protect evidence integrity by strict separation of roles.

This document is **structural only**.  
It authorizes **no analysis, no interpretation, no narrative**.

---

## 2. SINGLE SOURCE OF TRUTH (SSOT)

The **only authoritative governance source** for the TRIZEL ecosystem is:
trizel-ai/trizel-core
All other repositories:
- MUST comply with governance defined here.
- MUST NOT redefine governance independently.
- MAY reference this repository but MUST NOT fork governance logic.

In case of conflict, this document **always prevails**.

---

## 3. REPOSITORY ROLE BOUNDARIES

### 3.1 trizel-ai/trizel-core
Role: Governance, contracts, schemas, coordination

ALLOWED:
- Governance documents
- Structural contracts
- Schemas and validation rules

FORBIDDEN:
- Evidence generation
- Evidence storage
- Scientific analysis
- Interpretation or visualization

---

### 3.2 abdelkader-omran/trizel-AI
Role: Public portal & documentation gateway

ALLOWED:
- Methodology description
- Evidence pointers (URLs, DOIs, hashes)
- Status display (non-interpretative)
- Repository index

FORBIDDEN:
- Evidence mutation
- Evidence generation
- Analysis or inference

---

### 3.3 abdelkader-omran/AUTO-DZ-ACT-3I-ATLAS-DAILY
Role: Evidence production & monitoring

ALLOWED:
- Raw data
- Manifests
- Snapshots
- Deterministic scripts and workflows

CONSTRAINTS:
- No interpretation
- No conclusions
- No retroactive modification
- Evidence paths are immutable once verified

---

### 3.4 abdelkader-omran/AUTO-DZ-ACT-ANALYSIS-3I-ATLAS
Role: Analysis layer (downstream)

RULES:
- Consumes evidence only via validated manifests
- Must remain reproducible
- Outputs must be separable from evidence

---

### 3.5 abdelkader-omran/trizel-monitor
Role: Client / visualization application

RULES:
- Reads validated manifests only
- No local inference
- No data mutation
- Must respect evidence immutability

---

## 4. EVIDENCE GOVERNANCE (GLOBAL)

Evidence categories:
- SNAPSHOT: Official institutional announcements
- RAW DATA: Instrumental or observational datasets
- MANIFEST: Structural metadata only

Rules:
- Detection dates are immutable.
- Evidence MUST NOT be renamed or inferred.
- Absence of evidence MUST NOT be represented as data.

---

## 5. CROSS-REPO INTERACTION RULES

- Governance flows only from trizel-core outward.
- No undocumented dependencies are allowed.
- All integrations must be explicit and auditable.

---

## 6. CHANGE MANAGEMENT

- Governance changes originate ONLY in trizel-core.
- No change may retroactively affect evidence.
- Downstream propagation requires explicit PRs.

---

## 7. PROHIBITED PRACTICES

Explicitly forbidden:
- Mixing evidence and interpretation
- Rewriting historical evidence
- Inferring detection dates
- Narrative framing
- Silent cross-repo assumptions

---

## 8. ENFORCEMENT

- Non-compliant repositories are invalid.
- Downstream consumers MUST NOT trust invalid outputs.
- Automated audits may enforce compliance.

---

## 9. FINAL AUTHORITY

This document is binding for all TRIZEL repositories.

If any local rule conflicts with this document:
→ **This document prevails.**

---

End of document.
