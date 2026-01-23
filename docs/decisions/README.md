# Governance Decisions Directory

**Path:** `docs/decisions/`  
**Purpose:** Stores Layer-0 governance decision records by phase  
**Governance Authority:** Layer-0 (Governance)

---

## Overview

This directory contains governance decision records organized by implementation phase. Each decision represents a Layer-0 governance authorization or policy determination that is binding on TRIZEL repositories and activities.

Decision records document:
- Authorization statements for specific activities
- Explicit allow-lists and deny-lists
- Governance controls and constraints
- Effect and supersedence relationships
- Sign-off by Layer-0 governance authority

---

## Directory Structure

Decisions are organized by phase:

```
docs/decisions/
├── README.md (this file)
└── phase-f/
    └── DECISION_PHASE_F_UNFREEZE_END_TO_END.md
```

---

## Active Decisions

### Phase-F Decisions

#### DECISION_PHASE_F_UNFREEZE_END_TO_END
**Path:** `phase-f/DECISION_PHASE_F_UNFREEZE_END_TO_END.md`  
**Status:** ACTIVE  
**Effective Date:** 2026-01-23  
**Summary:** Authorizes end-to-end publication enablement (Layer-1 → Layer-2) for static artifact generation and publication while maintaining Phase-E security constraints.

---

## Related Decision Records

Additional governance decision records may be found in:
- `docs/governance/decisions/` — Phase-E publication and transition decisions
  - `DECISION_PHASE_E_PUBLICATION.md` — Phase-E publication eligibility and allowlist
  - `DECISION_PHASE_E_TRANSITION.md` — Phase-E T1/T2/T3 transition authorization

---

## Decision Requirements

All decision records in this directory must:

1. Include all mandatory sections (Title/Date/Scope, Decision, Permitted, Forbidden, Governance Controls, Effect/Supersedence, Sign-off)
2. Be issued by Layer-0 governance authority
3. Include clear authorization statements
4. Define explicit allow-lists and deny-lists
5. Document governance controls and review cycles
6. Clarify effect and supersedence relationships

---

**Maintained by:** Layer-0 Governance Authority  
**Last Updated:** 2026-01-23
