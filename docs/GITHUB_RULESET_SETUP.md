# GitHub Ruleset Configuration Guide

## Overview

This document provides instructions for configuring the Layer-0 governance enforcement ruleset in the GitHub repository settings.

## Purpose

The ruleset ensures that all changes to the `main` branch go through proper governance checks before being merged, with no bypass mechanism available.

## Configuration Steps

### 1. Access Repository Settings

1. Navigate to the repository: `trizel-ai/trizel-core`
2. Ensure you are authenticated as `trizel-admin`
3. Click on **Settings** → **Rules** → **Rulesets**

### 2. Create New Ruleset

Click **Create ruleset** and configure as follows:

#### Basic Settings
- **Ruleset Name**: `layer0-main-governance`
- **Status**: ✅ **Enabled**
- **Target Branch**: `main`

#### Branch Protection Rules

Enable the following rules:

##### Require Pull Request Before Merging
- ✅ **ON**
- This ensures all changes go through a PR review process

##### Require Status Checks to Pass
- ✅ **ON**
- **Require branches to be up to date before merging**: Recommended

Add the following **Required Status Checks** (EXACT names):

1. `Governance Validation / Validate governance boundaries`
2. `Deprecated Terms Check / Check for deprecated terminology`

**IMPORTANT**: The check names must match EXACTLY as shown above. These correspond to the `job.name` values in the workflow files.

#### Security Settings

- **Allow force pushes**: ❌ **OFF**
- **Allow deletions**: ❌ **OFF**

#### Bypass List

- **Bypass list**: ⚠️ **EMPTY** (no bypass allowed)
- This ensures that even administrators must pass the governance checks

### 3. Save Ruleset

Click **Create** or **Save changes** to activate the ruleset.

## Verification

### Test the Ruleset

1. Create a test branch: `test/layer0-proof`
   ```bash
   git checkout -b test/layer0-proof
   ```

2. Make a minimal change (e.g., edit `README.md`):
   ```bash
   echo "" >> README.md
   git add README.md
   git commit -m "test: verify governance checks"
   git push origin test/layer0-proof
   ```

3. Open a Pull Request to `main`

4. Verify that:
   - Both checks appear with exact names:
     - "Governance Validation / Validate governance boundaries"
     - "Deprecated Terms Check / Check for deprecated terminology"
   - GitHub blocks the merge button until checks pass
   - No bypass option is available

5. Once checks pass (green), the merge button should become available

## Workflow Files

The ruleset references these workflow files:

- `.github/workflows/governance-validation.yml`
- `.github/workflows/deprecated-terms-check.yml`

Both workflows run on:
- `pull_request` events (opened, synchronize, reopened)
- `workflow_dispatch` (manual trigger)

## Troubleshooting

### Check Names Don't Match

If the required checks don't appear or don't match:

1. Verify the exact `job.name` values in the workflow YAML files
2. The format must be: `"<Workflow Name> / <Job Description>"`
3. Update the ruleset to match the exact names from the workflows

### Checks Not Running

If checks don't run on PRs:

1. Verify workflows are in `.github/workflows/` on the target branch
2. Check workflow syntax with: `yamllint .github/workflows/*.yml`
3. Review GitHub Actions logs for errors

### Unable to Merge Despite Green Checks

1. Verify all required checks have passed
2. Check if additional review requirements are configured
3. Ensure the branch is up to date with `main`

## References

- GitHub Docs: [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- GitHub Docs: [Managing rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/managing-rulesets-for-a-repository)

---

**Document Version**: 1.0.0  
**Last Updated**: 2026-01-16  
**Layer**: 0 (Governance)
