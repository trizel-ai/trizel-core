# Governance Enforcement Guide

**Repository:** trizel-ai/trizel-core  
**Version:** 1.0.0  
**Last Updated:** 2026-01-17

---

## Overview

This document explains the GATE 1 (Layer-0 Governance Enforcement) system, how it works, what files are controlled, and how to verify compliance.

---

## What is GATE 1?

GATE 1 is the **Layer-0 Governance Enforcement** framework that:

1. **Validates governance integrity** - Ensures governance files are modified only through approved paths
2. **Validates schemas** - Checks YAML/JSON syntax correctness
3. **Checks deprecated terms** - Prevents forbidden terminology from entering the codebase
4. **Enforces immutable references** - Blocks TODO/XXXX placeholders in governance
5. **Requires evidence-first metadata** - Ensures evidence artifacts have proper metadata

---

## Enforcement Workflow

The enforcement is implemented in `.github/workflows/governance-enforcement.yml` and consists of 5 independent jobs:

### 1. Governance Integrity Check
**Script:** `scripts/governance/governance_integrity.sh`

**Purpose:** Ensures governance-controlled files are only modified with proper approval

**Checks:**
- Detects changes to governance-controlled files
- Requires corresponding entry in `governance/APPROVAL.md`
- Validates approval entry contains PR number, files, reason, and approver

**Governance-Controlled Files:**
- `trizel-ai/trizel-core/docs/governance/CROSS_REPO_GOVERNANCE.md`
- `DEPRECATED_TERMS.md`
- `COPILOT_INSTRUCTIONS.md`
- `ROLE.md`
- `OUTPUT_CONTRACT.md`
- `PUBLICATION_POLICY.md`
- `governance/rules/layer-boundaries.yml`
- `governance/rules/forbidden-terms.yml`

---

### 2. Schema Validation Check
**Script:** `scripts/governance/schema_validation.py`

**Purpose:** Validates all YAML and JSON files for syntax errors

**Checks:**
- Finds all `.yml`, `.yaml`, and `.json` files
- Validates syntax using Python's yaml and json parsers
- Reports exact line numbers for errors
- Excludes build artifacts and dependencies

---

### 3. Deprecated Terms Check
**Script:** `scripts/governance/deprecated_terms_check.sh`

**Purpose:** Scans for forbidden terminology defined in DEPRECATED_TERMS.md

**Source:** `DEPRECATED_TERMS.md` (single source of truth)

**Checks for:**
- Deprecated term "STOE"
- Version labels V12-V22
- "V<number> system" patterns
- Incorrect algorithm name variants (AUTO-DZ-ACT, AutoDzAct, etc.)
- Versioned algorithm names (AUTO DZ ACT system, AUTO DZ ACT v1, etc.)

**Scope:**
- All files except documentation directories (docs/, Documents/, website/, governance/)
- Excludes files that document the deprecated terms themselves

**Allowed:**
- Canonical form only: **AUTO DZ ACT** (exact case and spacing)

---

### 4. Immutable References Check
**Script:** `scripts/governance/immutable_references_check.sh`

**Purpose:** Ensures governance files are complete and contain no placeholders

**Checks for:**
- TODO placeholders in governance files
- XXXX placeholders in governance files
- TBD (To Be Determined) in critical locations
- Presence and integrity of CROSS_REPO_GOVERNANCE.md

**Critical Paths:**
- `governance/`
- `trizel-ai/trizel-core/docs/governance/`
- Root governance files (ROLE.md, etc.)

---

### 5. Evidence First Check
**Script:** `scripts/governance/evidence_first_check.py`

**Purpose:** Enforces evidence-first metadata for identified artifacts

**Files Checked:**
- Markdown files with "evidence", "validation", "artifact", "record", or "manifest" in path

**Required Metadata Fields:**
- Evidence: Description of evidence source
- Method: How evidence was obtained
- Validation: How evidence was validated
- ImmutableRefs: Commit hashes or content hashes

**Scope:** Conservative - only enforces on files that clearly identify as evidence records

---

## Branch-Aware Governance

The enforcement system is **branch-aware** and applies different rules based on the target branch:

### Targeting `main` branch
- **BLOCKING MODE**: All checks must pass to merge
- No bypasses allowed
- Strictest enforcement

### Targeting `format*` branches
- **REPORT MODE**: Checks run but don't block
- Used for non-functional changes
- Still reports violations

### Targeting other branches
- **BLOCKING MODE**: All checks must pass
- Same as main branch enforcement

See `BRANCH_CONTRACT.md` for complete branch governance rules.

---

## How to Trigger Failures (for Testing)

### ❌ Governance Integrity Failure

**Method:** Modify a governance file without updating APPROVAL.md

```bash
# 1. Modify a governance file
echo "# Test change" >> ROLE.md

# 2. Commit without updating governance/APPROVAL.md
git add ROLE.md
git commit -m "Test governance integrity"
git push
```

**Expected:** ❌ Governance Integrity Check fails with message about missing approval

**Fix:**
```bash
# Update APPROVAL.md with proper entry
# Include PR number, files modified, reason, approver
vim governance/APPROVAL.md
git add governance/APPROVAL.md
git commit -m "Add approval entry"
git push
```

---

### ❌ Schema Validation Failure

**Method:** Introduce YAML syntax error

```bash
# Create invalid YAML
cat > test-invalid.yml << 'EOF'
invalid_yaml:
  - item1
  - item2
 missing_indent: bad
EOF

git add test-invalid.yml
git commit -m "Test schema validation"
git push
```

**Expected:** ❌ Schema Validation Check fails with line number and error

**Fix:**
```bash
# Fix YAML syntax
cat > test-invalid.yml << 'EOF'
valid_yaml:
  - item1
  - item2
  correct_indent: good
EOF

git add test-invalid.yml
git commit -m "Fix YAML syntax"
git push
```

---

### ❌ Deprecated Terms Failure

**Method:** Add forbidden term to a file

```bash
# Add deprecated term
echo "This mentions STOE which is forbidden" >> docs/test.md

git add docs/test.md
git commit -m "Test deprecated terms"
git push
```

**Expected:** ❌ Deprecated Terms Check fails showing location of "STOE"

**Fix:**
```bash
# Remove the forbidden term
sed -i '/STOE/d' docs/test.md

git add docs/test.md
git commit -m "Remove deprecated term"
git push
```

---

### ❌ Immutable References Failure

**Method:** Add TODO placeholder in governance file

```bash
# Add TODO to governance
echo "## TODO: Complete this section" >> governance/README.md

git add governance/README.md
git commit -m "Test immutable references"
git push
```

**Expected:** ❌ Immutable References Check fails showing TODO location

**Fix:**
```bash
# Remove TODO placeholder
sed -i '/TODO/d' governance/README.md

git add governance/README.md
git commit -m "Remove TODO placeholder"
git push
```

---

### ❌ Evidence First Failure

**Method:** Create evidence file without required metadata

```bash
# Create evidence file without metadata
cat > docs/evidence-report.md << 'EOF'
# Evidence Report

This is an evidence report without proper metadata fields.
EOF

git add docs/evidence-report.md
git commit -m "Test evidence first"
git push
```

**Expected:** ❌ Evidence First Check fails listing missing fields

**Fix:**
```bash
# Add required metadata
cat > docs/evidence-report.md << 'EOF'
# Evidence Report

**Evidence:** Description of evidence source  
**Method:** How evidence was obtained  
**Validation:** How evidence was validated  
**ImmutableRefs:** commit:abc123def456

This is an evidence report with proper metadata fields.
EOF

git add docs/evidence-report.md
git commit -m "Add evidence metadata"
git push
```

---

## How to Make Checks Pass

### ✅ All Checks Pass

For all checks to pass:

1. **Governance changes** → Update `governance/APPROVAL.md`
2. **YAML/JSON files** → Ensure valid syntax
3. **Content** → No forbidden terms (STOE, V12-V22, etc.)
4. **Governance files** → No TODO/XXXX/TBD placeholders
5. **Evidence files** → Include all required metadata fields

**Example Compliant PR:**

```bash
# Make a safe documentation change
echo "Updated governance guide" >> docs/README.md

git add docs/README.md
git commit -m "Update documentation"
git push

# This will pass all checks ✅
```

---

## Running Checks Locally

Before pushing, run checks locally to catch issues:

```bash
# Change to repository root
cd /path/to/trizel-core

# Run individual checks
bash scripts/governance/governance_integrity.sh main HEAD
python3 scripts/governance/schema_validation.py
bash scripts/governance/deprecated_terms_check.sh
bash scripts/governance/immutable_references_check.sh
python3 scripts/governance/evidence_first_check.py
```

**Requirements:**
- Bash 4.0+
- Python 3.8+
- PyYAML (`pip install pyyaml`)
- Git

---

## Exact Failure Conditions

### Governance Integrity
- ❌ Modified governance file WITHOUT corresponding APPROVAL.md entry
- ❌ APPROVAL.md missing or incomplete

### Schema Validation
- ❌ YAML syntax error (indentation, special characters, etc.)
- ❌ JSON syntax error (missing comma, bracket, etc.)

### Deprecated Terms
- ❌ Contains "STOE" (case-sensitive word boundary)
- ❌ Contains V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, or V22
- ❌ Contains "V<number> system" pattern
- ❌ Algorithm name variants: AUTO-DZ-ACT, AutoDzAct, auto dz act
- ❌ Versioned algorithm: AUTO DZ ACT system, AUTO DZ ACT v1

### Immutable References
- ❌ TODO in governance paths
- ❌ XXXX in governance paths
- ❌ CROSS_REPO_GOVERNANCE.md missing or empty

### Evidence First
- ❌ Evidence-related file missing "Evidence" field
- ❌ Evidence-related file missing "Method" field
- ❌ Evidence-related file missing "Validation" field
- ❌ Evidence-related file missing "ImmutableRefs" field

---

## Deprecated Terms Source

The **single source of truth** for deprecated terms is:

**File:** `DEPRECATED_TERMS.md`

This file defines:
- All forbidden terms and patterns
- Canonical algorithm name: AUTO DZ ACT
- Enforcement rules
- Scope of prohibition

**Do not modify enforcement logic without updating this file first.**

---

## Evidence and Immutable Reference Paths

### Evidence and Immutable Reference Paths

### Paths Checked for Evidence Metadata:
- Files with "evidence_record" or "evidence_artifact" in path
- Files with "artifact_record" in path
- Files with "manifest_record" in path

**Note:** Conservative enforcement - only applies to files that clearly identify as evidence records by naming convention.

### Paths Checked for Immutable References:
- `governance/` (entire directory)
- `trizel-ai/trizel-core/docs/governance/`
- `COPILOT_INSTRUCTIONS.md`
- `ROLE.md`
- `OUTPUT_CONTRACT.md`
- `PUBLICATION_POLICY.md`
- `DEPRECATED_TERMS.md`

---

## Extending Rules Safely

To add new governance rules:

1. **Propose changes** in an issue or discussion
2. **Update documentation** first (this file, BRANCH_CONTRACT.md)
3. **Update or create validator script** in `scripts/governance/`
4. **Add job to workflow** in `.github/workflows/governance-enforcement.yml`
5. **Update APPROVAL.md** with justification
6. **Test thoroughly** with intentional failures
7. **Document in this guide** how to trigger failure and fix

**Single source of truth principle:**
- Each rule should have ONE authoritative definition
- Scripts enforce rules, don't define them
- Documentation is the source, code implements it

---

## Troubleshooting

### Check Not Running
- Verify workflow file exists: `.github/workflows/governance-enforcement.yml`
- Check GitHub Actions tab for workflow runs
- Ensure PR targets a branch (not draft)

### Check Always Failing
- Review individual job logs in GitHub Actions
- Run check locally with same parameters
- Verify you've committed all required changes

### False Positives
- Review exclusion patterns in validator scripts
- Check if file should be excluded from scanning
- Consider if rule is too strict (document and propose change)

### Need to Bypass (EMERGENCY ONLY)
- Governance enforcement should NEVER be bypassed
- If absolutely critical: contact repository administrator
- Document reason and remediate immediately after emergency

---

## Related Documents

- `BRANCH_CONTRACT.md` - Branch governance rules
- `governance/APPROVAL.md` - Approval log for governance changes
- `DEPRECATED_TERMS.md` - Forbidden terminology policy
- `governance/README.md` - Governance directory overview
- `.github/workflows/governance-enforcement.yml` - Enforcement workflow
- `docs/policies/ZENODO_ARCHIVING_POLICY.md` - Zenodo archiving and DOI minting policy
- `docs/policies/ZENODO_EXCEPTION_REGISTER.md` - Register of historical Zenodo exceptions
- `docs/policies/ZENODO_READY_CHECKLIST.md` - Mandatory pre-publication readiness checklist for Zenodo

---

## Support

For questions or issues:

1. Review this guide and related documentation
2. Check workflow run logs for specific failure details
3. Run checks locally to debug
4. Consult policy documents
5. Contact repository administrators

---

## SYSTEM FREEZE STATUS

**Status:** GLOBAL FREEZE ACTIVE

The TRIZEL project is currently in a **GLOBAL FREEZE** state following the completion of Layer-0 (Governance), Layer-1 (Research Documentation), and Layer-2 (Presentation).

### Freeze Declaration

The formal FREEZE DECLARATION is documented in:

- **Global Freeze:** `docs/FREEZE_DECLARATION.md`
- **Layer-Specific Freeze:** `governance/FREEZE.md`

### Enforcement During Freeze

All Pull Requests are subject to FREEZE compliance:

1. **Scientific Content Prohibition** - Any PR introducing scientific content, research analysis, or scientific publication is **non-compliant** with TRIZEL governance
2. **Automatic Rejection** - Non-compliant PRs introducing scientific material during FREEZE must be rejected
3. **Authorization Requirement** - Scientific activities require explicit Scientific Authorization Declaration (currently NOT GRANTED)

### Scope of Prohibition

During FREEZE, the following are prohibited:

- Scientific research, analysis, or experimentation
- Scientific publication or dissemination
- DOI minting and Zenodo archiving of scientific work
- Dataset creation or release for scientific purposes
- Citation generation for scientific findings

### Compliance Requirement

This FREEZE is binding across all TRIZEL repositories and organizations. All contributors must comply with FREEZE restrictions until the FREEZE is formally lifted by governance authority.

---

## SCIENTIFIC AUTHORIZATION STATUS

**Scientific Authorization Framework:** ACTIVE  
**Scientific Authorization Declaration:** ACTIVE (FRAMEWORK AND SPECIFIC GRANTS)  
**SYSTEM FREEZE:** ACTIVE (PARTIAL EXCEPTION FOR SA-3I-ATLAS-THEORY-001)

### Framework and Declaration

The Scientific Authorization Framework (`governance/SCIENTIFIC_AUTHORIZATION_FRAMEWORK.md`) defines the process by which scientific outputs may be authorized in the future. This framework is now active.

The Scientific Authorization Declaration (`docs/SCIENTIFIC_AUTHORIZATION_DECLARATION.md`) authorizes **BOTH** the governance process for reviewing and deciding scientific authorization requests **AND** specific scientific authorizations that have been granted.

### Current Status

- **SYSTEM FREEZE:** Active with limited exceptions
- **Authorization Process:** Operational (requests may be submitted and reviewed)
- **Specific Scientific Authorizations Granted:**
  1. **SA-3I-ATLAS-THEORY-001** (Effective: 2026-01-18)
     - Theoretical analysis of interstellar object 3I/ATLAS only
     - No observational activity, no publication
     - Document: `docs/authorizations/SA-3I-ATLAS-THEORY-001.md`

### Enforcement Rule

Any Pull Request that introduces scientific content must either:
1. Fall within the scope of an explicitly granted authorization (with proper reference), OR
2. Include a valid scientific authorization record issued through the authorized process

**For SA-3I-ATLAS-THEORY-001:**
- Work must be strictly theoretical analysis of 3I/ATLAS
- No observational activity
- No publication, DOI registration, or Zenodo deposits
- No public scientific communication as TRIZEL output

**For all other scientific work:**
Any Pull Request that introduces scientific content outside of granted authorizations **without** an explicit scientific authorization record issued through the authorized process **MUST** fail governance checks and be rejected.

**Compliance Requirement:**

All scientific PRs must include:
1. Reference to a valid Scientific Authorization Record
2. Evidence of required reviewer approvals (minimum 2 independent reviewers)
3. Formal governance sign-off documentation
4. Compliance verification with all applicable policies

**Without these requirements met, the PR is non-compliant and must be rejected.**

---

## Version History

| Version | Date       | Changes                                       |
|---------|------------|-----------------------------------------------|
| 1.0.0   | 2026-01-17 | Initial governance enforcement guide for GATE 1 |
| 1.1.0   | 2026-01-17 | Added Scientific Authorization Status section |

---

**Authority:** This is part of the Layer-0 governance framework.  
**Enforcement:** Automated via GATE 1 workflow + branch protection.  
**Compliance:** Mandatory for all contributors and PRs.
