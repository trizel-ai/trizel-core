# Governance Directory

This directory contains the governance enforcement infrastructure for `trizel-core`.

## Purpose

The governance directory centralizes all documentation, rules, and tooling related to:
- **GATE 1 (Layer-0 Governance Enforcement)** - Comprehensive validation framework
- Repository boundary enforcement (Layer 0 rules)
- Deprecated terminology prevention
- GitHub ruleset configuration
- Automated validation scripts
- Branch-aware governance (main vs format branches)

## Contents

### Documentation

- **`APPROVAL.md`** - Governance change approval log
  - Required for all governance file modifications
  - Tracks PR number, files, reason, and approver
  - Single source of truth for governance authorization

- **`RULESET_CONFIGURATION.md`** - Complete guide for configuring the GitHub ruleset `layer0-main-governance`
  - Step-by-step setup instructions
  - Verification checklist
  - Troubleshooting guide
  - Propagation instructions for other repositories

- **`GOVERNANCE_ENFORCEMENT_CHECKLIST.md`** - Deliverables checklist and status report
  - Current state verification
  - Workflow status
  - Infrastructure completeness
  - Next steps and propagation readiness

### Rules Definitions

Directory: `rules/`

- **`layer-boundaries.yml`** - Layer 0 boundary rules
  - Defines allowed vs prohibited content types
  - Lists required governance files
  - Documents validation enforcement

- **`forbidden-terms.yml`** - Deprecated terminology rules
  - Lists deprecated terms and patterns
  - Defines algorithm naming conventions
  - Specifies scan scope for enforcement

## Related Files

### Root Documentation

- **`BRANCH_CONTRACT.md`** - Branch governance contract (NEW)
  - Defines roles for main, format, and feature branches
  - Branch-specific enforcement rules
  - Protection settings and requirements

- **`GOVERNANCE_ENFORCEMENT.md`** - Comprehensive enforcement guide (NEW)
  - How each check works
  - How to trigger failures (for testing)
  - How to make checks pass
  - Troubleshooting and verification procedures

### Workflows

Location: `.github/workflows/`

- **`governance-enforcement.yml`** - GATE 1 comprehensive enforcement (NEW)
  - 5 independent validation jobs
  - Branch-aware enforcement (blocking vs reporting mode)
  - Runs on all PRs and pushes to main

- **`governance-validation.yml`** - Validates Layer 0 boundaries (LEGACY)
  - Checks for prohibited executable code
  - Checks for prohibited data files
  - Verifies required governance files exist
  - Validates markdown files are non-empty

- **`deprecated-terms-check.yml`** - Validates YAML/JSON for deprecated terms (LEGACY)
  - Scans for deprecated term "STOE"
  - Scans for deprecated version labels (V12-V22)
  - Enforces algorithm naming conventions

### Validator Scripts

Location: `scripts/governance/` (NEW - GATE 1)

- **`governance_integrity.sh`** - Validates governance change approvals
  - Detects changes to governance-controlled files
  - Requires approval entry in governance/APPROVAL.md
  - Documents approved path enforcement

- **`schema_validation.py`** - Validates YAML/JSON syntax
  - Checks all YAML and JSON files for syntax errors
  - Reports exact line numbers for issues
  - Excludes build artifacts and dependencies

- **`deprecated_terms_check.sh`** - Scans for forbidden terminology
  - Uses DEPRECATED_TERMS.md as single source of truth
  - Checks for STOE, V12-V22, algorithm variants
  - Comprehensive term scanning across all files

- **`immutable_references_check.sh`** - Validates governance completeness
  - Blocks TODO/XXXX/TBD placeholders in governance
  - Ensures CROSS_REPO_GOVERNANCE.md integrity
  - Enforces immutable references requirement

- **`evidence_first_check.py`** - Validates evidence metadata
  - Checks evidence files for required fields
  - Requires Evidence, Method, Validation, ImmutableRefs
  - Conservative enforcement on identified artifacts

Location: `scripts/governance/` (LEGACY)

- **`validate_repo.py`** - Python validation script
  - Programmatic interface to run governance checks locally
  - Can be integrated into pre-commit hooks or CI/CD
  - Provides same validations as GitHub workflows

## Quick Start

### Run GATE 1 Checks Locally

```bash
# From repository root
bash scripts/governance/governance_integrity.sh main HEAD
python3 scripts/governance/schema_validation.py
bash scripts/governance/deprecated_terms_check.sh
bash scripts/governance/immutable_references_check.sh
python3 scripts/governance/evidence_first_check.py
```

### Run Legacy Validation

```bash
# From repository root
python scripts/governance/validate_repo.py --verbose
```

### Configure GitHub Ruleset

See `RULESET_CONFIGURATION.md` for complete instructions.

Quick checklist:
1. Navigate to: Settings → Rules → Rulesets → layer0-main-governance
2. Ensure ruleset is Active
3. Target branch: `main`
4. Enable "Require PR before merging"
5. Enable "Require status checks to pass"
6. Add GATE 1 required checks:
   - `Governance Integrity Check`
   - `Schema Validation Check`
   - `Deprecated Terms Check`
   - `Immutable References Check`
   - `Evidence First Check`
7. Ensure bypass list is EMPTY

### Check Current Status

See `GOVERNANCE_ENFORCEMENT_CHECKLIST.md` for:
- Current implementation status
- Verification checklist
- Propagation readiness
- Next steps

## Enforcement Model

### GATE 1 Required Status Checks (NEW)

Five independent checks run on every PR:

1. **Governance Integrity Check**
   - Source: `scripts/governance/governance_integrity.sh`
   - Validates governance change approvals

2. **Schema Validation Check**
   - Source: `scripts/governance/schema_validation.py`
   - Validates YAML/JSON syntax

3. **Deprecated Terms Check**
   - Source: `scripts/governance/deprecated_terms_check.sh`
   - Prevents forbidden terminology

4. **Immutable References Check**
   - Source: `scripts/governance/immutable_references_check.sh`
   - Blocks placeholders in governance

5. **Evidence First Check**
   - Source: `scripts/governance/evidence_first_check.py`
   - Validates evidence metadata

### Legacy Status Checks

Two GitHub Actions workflows (being superseded by GATE 1):

1. **Governance Validation / Validate governance boundaries**
   - Source: `.github/workflows/governance-validation.yml`
   - Enforces Layer 0 structural rules

2. **Deprecated Terms Check / Check for deprecated terminology**
   - Source: `.github/workflows/deprecated-terms-check.yml`
   - Prevents forbidden terminology

### Enforcement Level

**Strict**: No bypasses allowed. All PRs must pass checks before merge.

### Branch-Aware Enforcement

- **`main` branch**: BLOCKING MODE - All checks must pass
- **`format*` branches**: REPORT MODE - Checks run but don't block
- **Other branches**: BLOCKING MODE - All checks must pass

See `BRANCH_CONTRACT.md` for complete branch governance rules.

### Scope

- **Governance Validation**: All files (except `.git`, `.github`, `scripts/governance`)
- **Deprecated Terms**: YAML and JSON files only

## Propagation to Other Repositories

Once `trizel-core` governance is stable, the same enforcement pattern should be propagated to:

1. `trizel-ai/trizel-AI`
2. `trizel-ai/trizel-monitor`
3. (Optional) `trizel-ai-site/*` repos

See `RULESET_CONFIGURATION.md` section "Propagation to Other Repositories" for detailed instructions.

## Policy References

The governance enforcement implements the following policies:

- `ROLE.md` - Repository charter and role definition
- `DEPRECATED_TERMS.md` - Forbidden terminology policy
- `PUBLICATION_POLICY.md` - Publication guidelines
- `COPILOT_INSTRUCTIONS.md` - AI assistant instructions
- `OUTPUT_CONTRACT.md` - Output format specifications

## Support

For questions or issues:

1. Review the documentation in this directory
2. Check workflow run logs for specific failure details
3. Consult policy documents (listed above)
4. Contact repository administrators

## Version

Governance enforcement version: 1.0.0  
Last updated: 2026-01-16
