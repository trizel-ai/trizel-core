# Branch Contract

**Repository:** trizel-ai/trizel-core  
**Version:** 1.0.0  
**Effective Date:** 2026-01-17

---

## Purpose

This document defines the branch governance contract for the trizel-core repository.
It establishes clear roles, rules, and enforcement mechanisms for different branches.

---

## Branch Roles

### Canonical / Protected Branch: `main`

**Role:** Production-ready governance source of truth

**Rules:**
- All governance enforcement checks apply **strictly**
- Merges are **blocked** unless all checks pass
- No bypasses allowed (including administrators)
- All changes must go through pull request review
- Branch is protected and cannot be force-pushed or deleted

**Enforcement:**
- GATE 1 Governance Enforcement workflow runs on all PRs targeting `main`
- All five checks must pass:
  1. Governance Integrity
  2. Schema Validation
  3. Deprecated Terms Check
  4. Immutable References Check
  5. Evidence First Check

---

### Formatting / Non-Functional Branch: `format` (or variants)

**Role:** Formatting, style fixes, documentation improvements

**Rules:**
- Governance checks run but in **reporting mode**
- Used for non-functional changes (formatting, typos, etc.)
- Cannot bypass governance rules
- Must eventually merge to `main` where full enforcement applies

**Enforcement:**
- Same checks run as for `main`
- Checks report but allow merge (warnings only)
- Final merge to `main` enforces all rules strictly

**Naming Conventions:**
- `format`
- `format/*` (e.g., `format/markdown-cleanup`)
- `formatting/*`

---

### Feature / Development Branches

**Role:** All other branches for features, fixes, and development

**Rules:**
- Full governance enforcement applies when targeting `main`
- Checks adapt based on target branch
- Must maintain governance compliance

**Naming Conventions:**
- `feature/*`
- `fix/*`
- `docs/*`
- `copilot/*`
- Any other branch names

---

## Enforcement Matrix

| Target Branch | Governance Integrity | Schema Validation | Deprecated Terms | Immutable Refs | Evidence First | Merge Blocking |
|---------------|---------------------|-------------------|------------------|----------------|----------------|----------------|
| `main`        | ✅ REQUIRED         | ✅ REQUIRED       | ✅ REQUIRED      | ✅ REQUIRED    | ✅ REQUIRED    | ✅ YES         |
| `format*`     | ⚠️ REPORT ONLY     | ⚠️ REPORT ONLY   | ⚠️ REPORT ONLY  | ⚠️ REPORT ONLY | ⚠️ REPORT ONLY | ❌ NO          |
| Other         | ✅ REQUIRED         | ✅ REQUIRED       | ✅ REQUIRED      | ✅ REQUIRED    | ✅ REQUIRED    | ✅ YES         |

---

## Branch Protection Settings

### Required for `main` branch:

1. **Require pull request before merging**
   - At least 1 approval recommended
   - Dismiss stale approvals on new commits (recommended)

2. **Require status checks to pass**
   - All five GATE 1 checks must pass:
     - `Governance Integrity Check`
     - `Schema Validation Check`
     - `Deprecated Terms Check`
     - `Immutable References Check`
     - `Evidence First Check`

3. **Require branches to be up to date**
   - Optional (recommended: disabled to reduce friction)

4. **Block force pushes**
   - Required

5. **Restrict deletions**
   - Required

6. **Bypass list**
   - Must be **EMPTY** (no bypasses allowed)

---

## Workflow Integration

The GATE 1 Governance Enforcement workflow (`.github/workflows/governance-enforcement.yml`) automatically detects the target branch and applies appropriate enforcement:

```yaml
env:
  BASE_BRANCH: ${{ github.event.pull_request.base.ref }}
  HEAD_BRANCH: ${{ github.event.pull_request.head.ref }}
```

**Branch Detection Logic:**
- If `BASE_BRANCH == "main"` → **BLOCKING MODE** (all checks must pass)
- If `BASE_BRANCH` starts with `"format"` → **REPORT MODE** (checks report only)
- Otherwise → **BLOCKING MODE** (all checks must pass)

---

## Governance Change Workflow

When modifying governance-controlled files:

1. **Create feature branch** from `main`
2. **Make changes** to governance files
3. **Update `governance/APPROVAL.md`** with:
   - PR number
   - List of modified files
   - Reason for changes
   - Approver
4. **Open PR** targeting `main`
5. **All checks must pass** (including governance integrity check)
6. **Review and merge** after approval

---

## Governance-Controlled Files

These files require approval entries in `governance/APPROVAL.md`:

- `trizel-ai/trizel-core/docs/governance/CROSS_REPO_GOVERNANCE.md`
- `DEPRECATED_TERMS.md`
- `COPILOT_INSTRUCTIONS.md`
- `ROLE.md`
- `OUTPUT_CONTRACT.md`
- `PUBLICATION_POLICY.md`
- `governance/rules/layer-boundaries.yml`
- `governance/rules/forbidden-terms.yml`

---

## Quick Reference

### ✅ Allowed on `main`
- Governance documents
- Policy definitions
- Documentation
- YAML/JSON schemas
- Workflow definitions

### ❌ Forbidden on `main`
- Executable code (except `.github/` and `scripts/governance/`)
- Data files (CSV, databases, pickles)
- Jupyter notebooks
- TODO/XXXX placeholders in governance files
- Deprecated terminology

---

## Compliance Verification

To verify compliance locally before pushing:

```bash
# Run all governance checks
bash scripts/governance/governance_integrity.sh main HEAD
python3 scripts/governance/schema_validation.py
bash scripts/governance/deprecated_terms_check.sh
bash scripts/governance/immutable_references_check.sh
python3 scripts/governance/evidence_first_check.py
```

---

## Related Documents

- `GOVERNANCE_ENFORCEMENT.md` - Detailed enforcement guide
- `governance/APPROVAL.md` - Governance change approval log
- `governance/README.md` - Governance directory overview
- `DEPRECATED_TERMS.md` - Forbidden terminology policy
- `.github/workflows/governance-enforcement.yml` - Enforcement workflow

---

## Version History

| Version | Date       | Changes                                    |
|---------|------------|---------------------------------------------|
| 1.0.0   | 2026-01-17 | Initial branch contract for GATE 1          |

---

**Authority:** This document is part of the Layer-0 governance framework.  
**Enforcement:** Automated via GitHub Actions + branch protection rules.  
**Compliance:** Mandatory for all contributors.
