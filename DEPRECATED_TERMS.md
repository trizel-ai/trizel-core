# DEPRECATED_TERMS.md

## Permanently Forbidden Terminology

**Repository**: `trizel-ai/trizel-core`  
**Policy Version**: 1.0.0  
**Last Updated**: 2026-01-11  
**Enforcement**: CI-validated, build-blocking

---

## Purpose

This document maintains the canonical list of deprecated terms that **must not appear anywhere** in the TRIZEL ecosystem.

These terms are permanently forbidden and cannot be:
- Used in new content
- Preserved in legacy content
- Renamed or reinterpreted
- Replaced with equivalents

If encountered: **REMOVE COMPLETELY**.

---

## Deprecated Terms Registry

### Absolutely Prohibited Terms

The following terms and concepts are **permanently deprecated**:

1. **"STOE"**
   - Status: FORBIDDEN
   - Action if found: REMOVE COMPLETELY
   - No reinterpretation allowed
   - No preservation allowed

2. **"V12–V22"** (and any variant)
   - Status: FORBIDDEN
   - Includes: V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, V22
   - Includes: Any version number in this range
   - Action if found: REMOVE COMPLETELY

3. **Versioned system labels**
   - Status: FORBIDDEN
   - Examples: "V1 system", "V2 system", "Version N framework"
   - Action if found: REMOVE COMPLETELY

4. **Framework evolution labels**
   - Status: FORBIDDEN
   - Examples: "evolved from", "supersedes", "next generation of"
   - Context: When referencing theoretical lineage
   - Action if found: REMOVE COMPLETELY

5. **Theoretical lineage labels**
   - Status: FORBIDDEN
   - Examples: "based on theory X", "derived from Y", "extension of Z"
   - Context: When implying theoretical dependency or preference
   - Action if found: REMOVE COMPLETELY

---

## Allowed Terminology

### The ONLY Allowed Algorithm Name

**"AUTO DZ ACT"**
- Exact spelling required
- No variants allowed
- No versioning allowed
- No "system" suffixes allowed
- Standalone, neutral, non-theoretical

### Acceptable Variants (NONE)

There are **NO acceptable variants** of the algorithm name.

Use only: **AUTO DZ ACT**

Do NOT use:
- "AUTO DZ ACT system"
- "AUTO DZ ACT v1"
- "AUTO DZ ACT framework"
- "AUTO-DZ-ACT" (wrong hyphenation)
- "AutoDzAct" (wrong capitalization)
- Any other variation

---

## Historical Experiment Description

### Allowed Description

When referring to the 2024 validation work, use ONLY:

**"historical validation experiment (2024)"**

### Forbidden Descriptions

Do NOT use:
- Names of tested theories
- "Theory X validation"
- "Testing framework Y"
- "V[number] validation"
- Anything implying theoretical evolution, preference, or dependency

---

## Enforcement Rules

### Automated Checking

All TRIZEL repositories must implement CI checks that:

1. **Scan all files** for deprecated terms
2. **Block merges** if deprecated terms detected
3. **Report exact location** of violations
4. **Fail builds** immediately
5. **Log violations** for audit trail

### Manual Review

All pull requests must include checklist item:

- [ ] **Deprecated terms check**: PASS (no forbidden terminology)

Reviewers must verify:
- No deprecated terms in code
- No deprecated terms in documentation
- No deprecated terms in comments
- No deprecated terms in commit messages
- No deprecated terms in metadata

---

## Removal Protocol

### If Deprecated Terms Found in Legacy Content

1. **REMOVE the term completely**
   - Do NOT rename
   - Do NOT reinterpret
   - Do NOT preserve in comments
   - Do NOT replace with equivalent

2. **Remove surrounding context if necessary**
   - If removal creates incomplete sentence: remove entire sentence
   - If removal creates incomplete paragraph: remove entire paragraph
   - If removal creates incomplete section: remove entire section

3. **Do NOT attempt to preserve meaning**
   - The deprecated terminology represents deprecated concepts
   - Removing the term means removing the concept
   - This is intentional

4. **Update version and document**
   - Increment version number
   - Document removal in changelog
   - Note compliance with TRIZEL DIRECTIVE

---

## CI Check Implementation

### Required CI Workflow

All repositories must include `.github/workflows/deprecated-terms-check.yml`:

```yaml
name: Deprecated Terms Check

on:
  pull_request:
    types: [opened, synchronize, reopened]
  push:
    branches: [main, master, develop]

jobs:
  check-deprecated-terms:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Check for deprecated terms
        run: |
          # Fetch deprecated terms list
          if [ -f DEPRECATED_TERMS.md ]; then
            echo "Checking for deprecated terms..."
            
            # Check for STOE
            if grep -r "STOE" --exclude-dir=.git --exclude="DEPRECATED_TERMS.md" .; then
              echo "ERROR: Found deprecated term 'STOE'"
              exit 1
            fi
            
            # Check for V12-V22
            if grep -rE "V(12|13|14|15|16|17|18|19|20|21|22)" --exclude-dir=.git --exclude="DEPRECATED_TERMS.md" .; then
              echo "ERROR: Found deprecated version labels (V12-V22)"
              exit 1
            fi
            
            echo "No deprecated terms found."
          else
            echo "DEPRECATED_TERMS.md not found, skipping check"
          fi
```

### Check Scope

The deprecated terms check must scan:

- All source code files
- All documentation files (.md, .txt, .rst)
- All configuration files (.yml, .yaml, .json)
- All README files
- All commit messages (in PR)
- All comments and docstrings

Exclusions:
- `.git` directory
- `DEPRECATED_TERMS.md` itself (this file)
- Binary files
- Build artifacts

---

## Violation Handling

### During Development

If deprecated terms detected during development:

1. **Block commit**: Pre-commit hook fails
2. **Show location**: Display exact file and line
3. **Require fix**: Cannot proceed until removed
4. **Re-run check**: Verify after removal

### During PR Review

If deprecated terms detected in PR:

1. **Block merge**: CI check fails
2. **Require changes**: Request removal
3. **Re-run CI**: After changes pushed
4. **Verify compliance**: Before approval

### In Production

If deprecated terms discovered in merged code:

1. **Create urgent PR**: Remove immediately
2. **Document incident**: Log compliance violation
3. **Update checks**: Prevent recurrence
4. **Audit history**: Check how it passed review

---

## Scope of Prohibition

### Where Terms are Forbidden

Deprecated terms are forbidden in:

- Source code
- Documentation
- Comments
- Commit messages
- Issue titles and descriptions
- PR titles and descriptions
- README files
- Configuration files
- Metadata files
- Website content
- Repository names (if creating new repos)
- Branch names
- Tag names
- Release notes

### Where Terms May Appear (ONLY)

Deprecated terms may appear ONLY in:

- This file (`DEPRECATED_TERMS.md`) as registry
- CI check implementation (for detection purposes)
- Incident reports documenting removal of deprecated terms
- Historical audit logs

---

## Algorithm Name Compliance

### Correct Usage

```
AUTO DZ ACT
```

### Incorrect Usage (All Forbidden)

```
STOE                    ❌ FORBIDDEN
AUTO DZ ACT system      ❌ FORBIDDEN
AUTO DZ ACT v1          ❌ FORBIDDEN
AUTO-DZ-ACT             ❌ FORBIDDEN (wrong hyphenation)
AutoDzAct               ❌ FORBIDDEN (wrong capitalization)
auto dz act             ❌ FORBIDDEN (wrong capitalization)
V12                     ❌ FORBIDDEN
V22                     ❌ FORBIDDEN
```

---

## Repository-Specific Guidance

### Layer 0 (trizel-core)

- Deprecated terms check: **MANDATORY**
- Enforcement: Build-blocking CI check
- Scope: All governance documents
- Exception: This file only

### Layer 1 (Auto-dz-act)

- Algorithm name: **AUTO DZ ACT ONLY**
- No version labels
- No system labels
- No theoretical lineage references

### Layer 2-6 (All Other Repositories)

- Must implement deprecated terms CI check
- Must pass check before merge
- No exceptions allowed
- Regular audits required

---

## Compliance Checklist

For every repository in TRIZEL ecosystem:

- [ ] DEPRECATED_TERMS.md present (or linked from trizel-core)
- [ ] CI check implemented and active
- [ ] Pre-commit hooks configured (optional but recommended)
- [ ] PR template includes deprecated terms check
- [ ] All existing content scanned and cleaned
- [ ] All contributors aware of policy
- [ ] Violations logged and tracked

---

## Audit and Monitoring

### Regular Audits

Quarterly audit must verify:

1. All repositories have deprecated terms check
2. All checks are active and passing
3. No violations in recent merges
4. CI configuration up to date
5. This registry is current

### Violation Metrics

Track and report:
- Number of violations caught by CI
- Number of violations in PR review
- Number of violations in production
- Time to remediation
- Repeat violations by contributor

---

## Updates to This Registry

### Adding New Deprecated Terms

To add terms to this registry:

1. Create PR in `trizel-core`
2. Update this file with new term
3. Document reason for deprecation
4. Update CI check to detect new term
5. Notify all repository maintainers
6. Scan all repositories for new term
7. Remove all instances before enforcement

### Removing Terms from Registry

Terms can only be removed if:
- Originally added in error
- Requires governance approval
- Must document reason in changelog

**Generally, deprecations are permanent.**

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-11 | Initial DEPRECATED_TERMS.md with TRIZEL DIRECTIVE |

---

## Related Documents

- `COPILOT_INSTRUCTIONS.md` — Copilot operating rules (references this file)
- `.github/workflows/deprecated-terms-check.yml` — CI enforcement
- `.github/PULL_REQUEST_TEMPLATE/` — PR checklists
- `ROLE.md` — Repository layer assignment
