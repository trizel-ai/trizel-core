# Governance Directory

This directory contains the governance enforcement infrastructure for `trizel-core`.

## Purpose

The governance directory centralizes all documentation, rules, and tooling related to:
- Repository boundary enforcement (Layer 0 rules)
- Deprecated terminology prevention
- GitHub ruleset configuration
- Automated validation scripts

## Contents

### Documentation

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

### Workflows

Location: `.github/workflows/`

- **`governance-validation.yml`** - Validates Layer 0 boundaries
  - Checks for prohibited executable code
  - Checks for prohibited data files
  - Verifies required governance files exist
  - Validates markdown files are non-empty

- **`deprecated-terms-check.yml`** - Validates YAML/JSON for deprecated terms
  - Scans for deprecated term "STOE"
  - Scans for deprecated version labels (V12-V22)
  - Enforces algorithm naming conventions

### Scripts

Location: `scripts/governance/`

- **`validate_repo.py`** - Python validation script
  - Programmatic interface to run governance checks locally
  - Can be integrated into pre-commit hooks or CI/CD
  - Provides same validations as GitHub workflows

## Quick Start

### Run Local Validation

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
6. Add required checks (see RULESET_CONFIGURATION.md for exact names)
7. Ensure bypass list is EMPTY

### Check Current Status

See `GOVERNANCE_ENFORCEMENT_CHECKLIST.md` for:
- Current implementation status
- Verification checklist
- Propagation readiness
- Next steps

## Enforcement Model

### Required Status Checks

Two GitHub Actions workflows run on every PR and must pass:

1. **Governance Validation / Validate governance boundaries**
   - Source: `.github/workflows/governance-validation.yml`
   - Enforces Layer 0 structural rules

2. **Deprecated Terms Check / Check for deprecated terminology**
   - Source: `.github/workflows/deprecated-terms-check.yml`
   - Prevents forbidden terminology

### Enforcement Level

**Strict**: No bypasses allowed. All PRs must pass both checks before merge.

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
