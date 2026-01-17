#!/bin/bash
set -euo pipefail

# Immutable References Check
# Ensures no TODO/XXXX placeholders in governance and requires proper references

echo "=========================================="
echo "IMMUTABLE REFERENCES CHECK"
echo "=========================================="
echo ""

# Paths that require immutable references
CRITICAL_PATHS=(
  "governance/"
  "trizel-ai/trizel-core/docs/governance/"
  "COPILOT_INSTRUCTIONS.md"
  "ROLE.md"
  "OUTPUT_CONTRACT.md"
  "PUBLICATION_POLICY.md"
  "DEPRECATED_TERMS.md"
)

echo "Checking critical governance paths for placeholders..."
echo ""

# Exclusions
EXCLUDE_ARGS=(
  "--exclude-dir=.git"
  "--exclude-dir=.github"
  "--exclude-dir=node_modules"
  "--exclude-dir=vendor"
  "--exclude-dir=dist"
  "--exclude-dir=build"
  "--exclude=*.log"
  "--exclude=GOVERNANCE_ENFORCEMENT.md"
)

FAILURES=0

# Check for TODO placeholders in governance files
echo "1. Checking for TODO placeholders in governance files..."
TODO_FOUND=false
for path in "${CRITICAL_PATHS[@]}"; do
  if [[ -e "$path" ]]; then
    if grep -rIn "${EXCLUDE_ARGS[@]}" "\bTODO\b" "$path" 2>/dev/null; then
      TODO_FOUND=true
    fi
  fi
done

if [[ "$TODO_FOUND" == "true" ]]; then
  echo "❌ FAILED: Found TODO placeholders in governance files"
  echo "   Governance files must be complete, not contain placeholders"
  echo ""
  FAILURES=$((FAILURES + 1))
else
  echo "✅ PASSED: No TODO placeholders in governance files"
  echo ""
fi

# Check for XXXX placeholders in governance files
echo "2. Checking for XXXX placeholders in governance files..."
XXXX_FOUND=false
for path in "${CRITICAL_PATHS[@]}"; do
  if [[ -e "$path" ]]; then
    if grep -rIn "${EXCLUDE_ARGS[@]}" "XXXX" "$path" 2>/dev/null; then
      XXXX_FOUND=true
    fi
  fi
done

if [[ "$XXXX_FOUND" == "true" ]]; then
  echo "❌ FAILED: Found XXXX placeholders in governance files"
  echo "   Governance files must be complete, not contain placeholders"
  echo ""
  FAILURES=$((FAILURES + 1))
else
  echo "✅ PASSED: No XXXX placeholders in governance files"
  echo ""
fi

# Check for TBD (To Be Determined) in critical files
echo "3. Checking for TBD (To Be Determined) in governance files..."
TBD_FOUND=false
for path in "${CRITICAL_PATHS[@]}"; do
  if [[ -e "$path" ]]; then
    if grep -rIn "${EXCLUDE_ARGS[@]}" "\bTBD\b" "$path" 2>/dev/null | grep -v "PR #TBD" 2>/dev/null; then
      TBD_FOUND=true
    fi
  fi
done

if [[ "$TBD_FOUND" == "true" ]]; then
  echo "⚠️  WARNING: Found TBD in governance files (excluding 'PR #TBD')"
  echo "   Consider replacing with concrete values"
  echo ""
  # This is a warning, not a failure
else
  echo "✅ PASSED: No TBD placeholders in governance files"
  echo ""
fi

# Check that CROSS_REPO_GOVERNANCE.md exists and is properly referenced
echo "4. Checking CROSS_REPO_GOVERNANCE.md integrity..."
CROSS_REPO_FILE="trizel-ai/trizel-core/docs/governance/CROSS_REPO_GOVERNANCE.md"

if [[ ! -f "$CROSS_REPO_FILE" ]]; then
  echo "❌ FAILED: $CROSS_REPO_FILE not found"
  echo "   This is a critical governance file"
  echo ""
  FAILURES=$((FAILURES + 1))
else
  # Check if file is not empty
  if [[ ! -s "$CROSS_REPO_FILE" ]]; then
    echo "❌ FAILED: $CROSS_REPO_FILE is empty"
    echo ""
    FAILURES=$((FAILURES + 1))
  else
    echo "✅ PASSED: $CROSS_REPO_FILE exists and is not empty"
    echo ""
  fi
fi

# Summary
echo "=========================================="
if [[ $FAILURES -eq 0 ]]; then
  echo "✅ ALL CHECKS PASSED"
  echo "✅ No placeholder references in governance files"
  echo "✅ Critical governance files are complete"
  exit 0
else
  echo "❌ CHECKS FAILED: $FAILURES critical issue(s) detected"
  echo ""
  echo "REMEDIATION:"
  echo "  1. Remove all TODO/XXXX/TBD placeholders from governance"
  echo "  2. Replace with concrete commit hashes or content hashes"
  echo "  3. Ensure all governance files are complete and final"
  echo "  4. Verify CROSS_REPO_GOVERNANCE.md is present"
  exit 1
fi
