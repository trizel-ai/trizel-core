# GitHub Ruleset Configuration Guide

## layer0-main-governance Ruleset

This document provides the exact configuration for the `layer0-main-governance` GitHub Ruleset that enforces governance boundaries on the `main` branch of `trizel-ai/trizel-core`.

## Purpose

The ruleset ensures that:
1. All changes go through pull request review
2. Required status checks pass before merging
3. Governance boundaries are validated automatically
4. No deprecated terminology enters the codebase

## Ruleset Configuration

### Basic Settings

- **Ruleset Name**: `layer0-main-governance`
- **Status**: Active
- **Enforcement**: Enabled (not in evaluation mode)
- **Target**: Branch `main`

### Rules

#### 1. Require Pull Request Before Merging

**Setting**: ENABLED

**Configuration**:
- Dismiss stale pull request approvals when new commits are pushed: Optional
- Require approval of the most recent reviewable push: Optional
- Required approving reviews: 1 (recommended)
- Require review from code owners: Optional

#### 2. Require Status Checks to Pass

**Setting**: ENABLED

**Required Status Checks** (MUST be exactly these two):

1. **Governance Validation / Validate governance boundaries**
   - Source: `.github/workflows/governance-validation.yml`
   - Job name: `validate-governance`
   - Check name: `Validate governance boundaries`
   
2. **Deprecated Terms Check / Check for deprecated terminology**
   - Source: `.github/workflows/deprecated-terms-check.yml`
   - Job name: `check-deprecated-terms`
   - Check name: `Check for deprecated terminology (YAML/JSON only)`

**Additional Settings**:
- Require branches to be up to date before merging: Optional (recommended: No, to reduce friction)
- Additional required checks: None (only the two above)

#### 3. Block Force Pushes

**Setting**: ENABLED (recommended)

Prevents rewriting history on the `main` branch.

#### 4. Restrict Deletions

**Setting**: ENABLED (recommended)

Prevents accidental deletion of the `main` branch.

### Bypass List

**Configuration**: EMPTY (strict enforcement)

**Rationale**: No one should bypass governance checks, including administrators. If absolutely necessary for emergency situations, only the organization owner (`trizel-admin`) should be on the bypass list, but prefer keeping it empty.

## How to Configure

### Step 1: Access Ruleset Settings

1. Navigate to the repository: `https://github.com/trizel-ai/trizel-core`
2. Click **Settings** (requires admin access)
3. In the left sidebar, under "Code and automation", click **Rules** → **Rulesets**
4. Click on `layer0-main-governance` (or create it if it doesn't exist)

### Step 2: Configure Target

1. Under "Target branches", click **Add target**
2. Select **Include by pattern**
3. Enter pattern: `main`
4. Save

### Step 3: Configure Branch Protection Rules

Enable the following rules:

1. **Require a pull request before merging**
   - Toggle ON
   - Configure approval requirements as needed

2. **Require status checks to pass before merging**
   - Toggle ON
   - Click **Add checks**
   - Add: `Governance Validation / Validate governance boundaries`
   - Add: `Deprecated Terms Check / Check for deprecated terminology`
   
   **IMPORTANT**: The check names must match EXACTLY as they appear in the workflow runs. The format is:
   ```
   <Workflow Name> / <Job Name>
   ```

3. **Block force pushes** (recommended)
   - Toggle ON

4. **Restrict deletions** (recommended)
   - Toggle ON

### Step 4: Configure Bypass

1. Under "Bypass list", ensure it is **EMPTY**
2. If there are any entries, remove them (click the X next to each entry)

### Step 5: Save and Enable

1. Click **Save changes**
2. Ensure the ruleset status is **Active** (not "Disabled" or "Evaluation")

## Verification Checklist

After configuring the ruleset, verify:

- [ ] Ruleset is **Active** (not disabled or in evaluation mode)
- [ ] Target branch includes `main`
- [ ] "Require a pull request before merging" is **ON**
- [ ] "Require status checks to pass" is **ON**
- [ ] Required checks list contains **EXACTLY** two items:
  - [ ] "Governance Validation / Validate governance boundaries"
  - [ ] "Deprecated Terms Check / Check for deprecated terminology"
- [ ] Bypass list is **EMPTY**
- [ ] Both workflow files exist and are active:
  - [ ] `.github/workflows/governance-validation.yml`
  - [ ] `.github/workflows/deprecated-terms-check.yml`

## Troubleshooting: "Phantom Pending" Status

### Symptoms

A PR shows a yellow "pending" status for required checks at the top (blocking merge), but the same checks appear green/successful in the checks list below.

### Root Cause

GitHub's required check binding has become desynchronized from the actual workflow check names.

### Fix (Ruleset-Level)

**IMPORTANT**: This fix applies to **Rulesets**, not old-style Branch Protection rules.

1. As `trizel-admin`, navigate to: Settings → Rules → Rulesets → `layer0-main-governance`
2. **Temporarily remove** both required checks from the ruleset:
   - Remove "Governance Validation / Validate governance boundaries"
   - Remove "Deprecated Terms Check / Check for deprecated terminology"
3. Click **Save changes**
4. Return to the PR page and refresh
5. If all checks are visibly green/successful in the checks list **and** PR approvals are satisfied, you may merge the PR
6. **Immediately after merging**, go back to: Settings → Rules → Rulesets → `layer0-main-governance`
7. **Re-add** both required checks:
   - Add "Governance Validation / Validate governance boundaries"
   - Add "Deprecated Terms Check / Check for deprecated terminology"
8. Click **Save changes**

**NOTE**: This does NOT disable the workflows. They continue to run. It only resynchronizes GitHub's required-check binding.

### Prevention

- Keep workflow names and job names stable
- Avoid renaming workflows or jobs that are used as required checks
- When updating workflow names, update the ruleset configuration simultaneously

## Workflow File References

### Governance Validation Workflow

**File**: `.github/workflows/governance-validation.yml`

**What it validates**:
- No executable code files (outside `.git` and `.github`)
- No data files, databases, or notebooks
- All required governance files exist
- All markdown files are non-empty
- Heuristic scan for cross-layer content (warning only)

**Check name produced**: `Governance Validation / Validate governance boundaries`

### Deprecated Terms Check Workflow

**File**: `.github/workflows/deprecated-terms-check.yml`

**What it validates** (YAML/JSON only):
- No deprecated term "STOE"
- No deprecated version labels (V12-V22)
- No "V<number> system" patterns
- Algorithm name must be exactly "AUTO DZ ACT" (no variants)

**Check name produced**: `Deprecated Terms Check / Check for deprecated terminology`

## Additional Validation Tools

### Python Validator Script

**File**: `scripts/governance/validate_repo.py`

This script provides a programmatic interface to run the same validations locally:

```bash
# Run validation
python scripts/governance/validate_repo.py

# Run with verbose output
python scripts/governance/validate_repo.py --verbose
```

**Exit codes**:
- `0`: All validations passed
- `1`: Validation failures detected

### Governance Rules Files

**Files**:
- `governance/rules/layer-boundaries.yml` - Defines Layer 0 boundary rules
- `governance/rules/forbidden-terms.yml` - Defines deprecated terminology rules

These files document the governance policies that are enforced by the workflows.

## Propagation to Other Repositories

After `trizel-core` is stable and confirmed working, apply the same pattern to:

1. `trizel-ai/trizel-AI`
2. `trizel-ai/trizel-monitor`
3. (Optional) `trizel-ai-site/*` repositories

### Propagation Checklist (Per Repository)

For each repository:

- [ ] Create/confirm Ruleset targeting `main` branch
- [ ] Enable "Require a pull request before merging"
- [ ] Enable "Require status checks to pass"
- [ ] Add the SAME TWO required checks (or equivalent if workflow names differ)
- [ ] Ensure the workflows exist in that repository
- [ ] Verify workflows produce the expected check names on PR
- [ ] Validate bypass list is EMPTY
- [ ] Test with a sample PR to confirm enforcement

### Repository-Specific Considerations

Each repository may have slightly different governance needs:

- **trizel-AI**: May need additional checks for data processing rules
- **trizel-monitor**: May need checks for monitoring-specific policies
- **trizel-ai-site**: May need checks for publication compliance

Adapt the workflow names and checks accordingly, but maintain the same pattern:
1. PR required before merge
2. Status checks required
3. No bypass list

## References

- **Policy Documents**:
  - `ROLE.md` - Repository charter and role definition
  - `DEPRECATED_TERMS.md` - Forbidden terminology policy
  - `PUBLICATION_POLICY.md` - Publication guidelines
  - `COPILOT_INSTRUCTIONS.md` - AI assistant instructions

- **Governance Files**:
  - `governance/rules/layer-boundaries.yml`
  - `governance/rules/forbidden-terms.yml`

- **Implementation**:
  - `.github/workflows/governance-validation.yml`
  - `.github/workflows/deprecated-terms-check.yml`
  - `scripts/governance/validate_repo.py`

## Contact

For questions or issues with governance enforcement:
- Review this document first
- Check workflow run logs for specific failures
- Consult `ROLE.md` for governance philosophy
- Contact repository administrators if needed
