# GATE 1 Governance Validators

This directory contains the validation scripts for GATE 1 (Layer-0 Governance Enforcement).

## Validators

### 1. governance_integrity.sh
**Purpose:** Validates that governance-controlled files are only modified through approved paths

**Usage:**
```bash
bash tools/governance/governance_integrity.sh <base_branch> <head_branch>
```

**Example:**
```bash
bash tools/governance/governance_integrity.sh main HEAD
```

**What it checks:**
- Detects changes to governance-controlled files
- Requires approval entry in `governance/APPROVAL.md`
- Validates approval contains PR number, files, reason, and approver

**Exit codes:**
- 0: All checks passed
- 1: Governance files modified without approval

---

### 2. schema_validation.py
**Purpose:** Validates YAML and JSON syntax for all files in the repository

**Usage:**
```bash
python3 tools/governance/schema_validation.py
```

**What it checks:**
- All `.yml`, `.yaml`, and `.json` files
- Validates syntax using Python parsers
- Reports exact line numbers for errors

**Exit codes:**
- 0: All files valid
- 1: Syntax errors found

**Requirements:**
- Python 3.8+
- PyYAML library

---

### 3. deprecated_terms_check.sh
**Purpose:** Scans for forbidden terminology using DEPRECATED_TERMS.md as source

**Usage:**
```bash
bash tools/governance/deprecated_terms_check.sh
```

**What it checks:**
- Deprecated term "STOE"
- Version labels V12-V22
- "V<number> system" patterns
- Incorrect algorithm name variants
- Versioned algorithm names

**Scope:**
- All files except documentation directories
- Excludes: docs/, Documents/, website/, governance/

**Exit codes:**
- 0: No deprecated terms found
- 1: Deprecated terms detected

---

### 4. immutable_references_check.sh
**Purpose:** Ensures governance files are complete and contain no placeholders

**Usage:**
```bash
bash tools/governance/immutable_references_check.sh
```

**What it checks:**
- TODO placeholders in governance files
- XXXX placeholders in governance files
- TBD (To Be Determined) in critical locations
- CROSS_REPO_GOVERNANCE.md integrity

**Critical paths:**
- `governance/`
- `trizel-ai/trizel-core/docs/governance/`
- Root governance files (ROLE.md, COPILOT_INSTRUCTIONS.md, etc.)

**Exit codes:**
- 0: All checks passed
- 1: Placeholders found or critical files missing

---

### 5. evidence_first_check.py
**Purpose:** Validates evidence metadata for identified artifacts

**Usage:**
```bash
python3 tools/governance/evidence_first_check.py
```

**What it checks:**
- Markdown files with evidence-related naming patterns
- Required metadata fields: Evidence, Method, Validation, ImmutableRefs

**Scope:**
- Conservative enforcement
- Only files clearly identified as evidence records by naming convention:
  - `*evidence_record*.md`
  - `*evidence_artifact*.md`
  - `*artifact_record*.md`
  - `*manifest_record*.md`

**Exit codes:**
- 0: All evidence files have required metadata
- 1: Evidence files missing required fields

**Requirements:**
- Python 3.8+

---

## Running All Checks

To run all governance checks locally:

```bash
# From repository root
cd /path/to/trizel-core

# Run all validators
bash tools/governance/governance_integrity.sh main HEAD
python3 tools/governance/schema_validation.py
bash tools/governance/deprecated_terms_check.sh
bash tools/governance/immutable_references_check.sh
python3 tools/governance/evidence_first_check.py
```

## Integration with GitHub Actions

These validators are integrated into the GATE 1 workflow:
- **Workflow:** `.github/workflows/governance-enforcement.yml`
- **Trigger:** On pull requests and pushes to main
- **Enforcement:** All checks must pass for merge to main

## Requirements

### System Requirements
- Bash 4.0+
- Python 3.8+
- Git

### Python Dependencies
- PyYAML (for schema_validation.py)

Install with:
```bash
pip install pyyaml
```

## Exit Codes

All validators follow the same exit code convention:
- **0:** Success (all checks passed)
- **1:** Failure (violations detected)

## Troubleshooting

### Schema Validation Fails
- Check YAML/JSON syntax in reported file
- Verify indentation (use spaces, not tabs)
- Check for special characters or quotes

### Deprecated Terms Check Fails
- Review DEPRECATED_TERMS.md for complete list
- Use only canonical form: "AUTO DZ ACT"
- Remove all forbidden terms completely

### Immutable References Check Fails
- Remove TODO/XXXX/TBD placeholders from governance
- Replace with concrete values or commit hashes
- Ensure CROSS_REPO_GOVERNANCE.md exists

### Governance Integrity Check Fails
- Update governance/APPROVAL.md with PR entry
- List all modified governance files
- Include PR number, reason, and approver

### Evidence First Check Fails
- Add required metadata fields to evidence files
- Include: Evidence, Method, Validation, ImmutableRefs
- Follow evidence-first metadata format

## Related Documentation

- **GOVERNANCE_ENFORCEMENT.md** - Complete enforcement guide
- **BRANCH_CONTRACT.md** - Branch governance rules
- **governance/APPROVAL.md** - Approval log
- **DEPRECATED_TERMS.md** - Forbidden terminology policy

---

**Version:** 1.0.0  
**Last Updated:** 2026-01-17  
**Part of:** GATE 1 (Layer-0 Governance Enforcement)
