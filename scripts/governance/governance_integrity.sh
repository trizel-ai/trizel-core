#!/bin/bash
set -euo pipefail

# Governance Integrity Check
# Ensures that governance-controlled files are only modified through approved paths

BASE_BRANCH="${1:-main}"
HEAD_BRANCH="${2:-HEAD}"

echo "=========================================="
echo "GOVERNANCE INTEGRITY CHECK"
echo "=========================================="
echo "Base branch: $BASE_BRANCH"
echo "Head branch: $HEAD_BRANCH"
echo ""

# Define governance-controlled files and directories
GOVERNANCE_FILES=(
  "trizel-ai/trizel-core/docs/governance/CROSS_REPO_GOVERNANCE.md"
  "DEPRECATED_TERMS.md"
  "COPILOT_INSTRUCTIONS.md"
  "ROLE.md"
  "OUTPUT_CONTRACT.md"
  "PUBLICATION_POLICY.md"
  "governance/rules/layer-boundaries.yml"
  "governance/rules/forbidden-terms.yml"
)

APPROVAL_FILE="governance/APPROVAL.md"

# Check if running in PR context
if [[ "$BASE_BRANCH" != "main" ]] && [[ "$BASE_BRANCH" != "format"* ]]; then
  echo "ℹ️  Non-standard target branch: $BASE_BRANCH"
fi

# Get list of changed files
if git rev-parse origin/"$BASE_BRANCH" >/dev/null 2>&1; then
  CHANGED_FILES=$(git diff --name-only origin/"$BASE_BRANCH"...HEAD 2>/dev/null || true)
else
  echo "⚠️  Cannot find base branch origin/$BASE_BRANCH, checking against HEAD~1"
  CHANGED_FILES=$(git diff --name-only HEAD~1...HEAD 2>/dev/null || true)
fi

if [[ -z "$CHANGED_FILES" ]]; then
  echo "✅ No changed files detected"
  exit 0
fi

echo "Changed files:"
echo "$CHANGED_FILES" | sed 's/^/  - /'
echo ""

# Check if any governance files were modified
MODIFIED_GOVERNANCE_FILES=()
for file in "${GOVERNANCE_FILES[@]}"; do
  if echo "$CHANGED_FILES" | grep -q "^${file}$"; then
    MODIFIED_GOVERNANCE_FILES+=("$file")
  fi
done

if [[ ${#MODIFIED_GOVERNANCE_FILES[@]} -eq 0 ]]; then
  echo "✅ No governance-controlled files were modified"
  exit 0
fi

echo "⚠️  Governance-controlled files modified:"
for file in "${MODIFIED_GOVERNANCE_FILES[@]}"; do
  echo "  - $file"
done
echo ""

# Check if APPROVAL.md exists and was updated
if [[ ! -f "$APPROVAL_FILE" ]]; then
  echo "❌ ERROR: governance/APPROVAL.md does not exist"
  echo ""
  echo "Governance-controlled files require approval."
  echo "Create governance/APPROVAL.md and document this change."
  exit 1
fi

# Check if APPROVAL.md was modified in this PR
if echo "$CHANGED_FILES" | grep -q "^${APPROVAL_FILE}$"; then
  echo "✅ APPROVAL.md was updated in this PR"
  echo ""
  echo "Verifying approval entry..."
  
  # Check if the approval file contains recent content (basic check)
  if [[ -s "$APPROVAL_FILE" ]] && grep -q "PR #" "$APPROVAL_FILE"; then
    echo "✅ APPROVAL.md contains approval entries"
    echo ""
    echo "⚠️  MANUAL REVIEW REQUIRED:"
    echo "   - Verify that approval entry matches this PR"
    echo "   - Verify that all modified files are listed"
    echo "   - Verify that reason is documented"
    exit 0
  else
    echo "❌ ERROR: APPROVAL.md appears incomplete"
    echo "   - Must contain PR number"
    echo "   - Must list all modified governance files"
    echo "   - Must include reason and approver"
    exit 1
  fi
else
  echo "❌ ERROR: Governance files modified without approval"
  echo ""
  echo "REQUIRED ACTION:"
  echo "  1. Update governance/APPROVAL.md with:"
  echo "     - PR number"
  echo "     - List of modified files:"
  for file in "${MODIFIED_GOVERNANCE_FILES[@]}"; do
    echo "       - $file"
  done
  echo "     - Clear reason for changes"
  echo "     - Approver name/role"
  echo ""
  echo "  2. Commit the updated APPROVAL.md in this PR"
  echo ""
  echo "See governance/APPROVAL.md for format examples."
  exit 1
fi
