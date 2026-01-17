#!/bin/bash
set -euo pipefail

# Deprecated Terms Check
# Scans for forbidden terms using DEPRECATED_TERMS.md as the source

echo "=========================================="
echo "DEPRECATED TERMS CHECK"
echo "=========================================="
echo ""

DEPRECATED_TERMS_FILE="DEPRECATED_TERMS.md"

if [[ ! -f "$DEPRECATED_TERMS_FILE" ]]; then
  echo "❌ ERROR: $DEPRECATED_TERMS_FILE not found"
  exit 1
fi

echo "Using source file: $DEPRECATED_TERMS_FILE"
echo ""

# Exclusions - files where deprecated terms are documented
EXCLUDE_ARGS=(
  "--exclude-dir=.git"
  "--exclude-dir=.github"
  "--exclude-dir=node_modules"
  "--exclude-dir=vendor"
  "--exclude-dir=dist"
  "--exclude-dir=build"
  "--exclude-dir=target"
  "--exclude-dir=.venv"
  "--exclude-dir=Documents"
  "--exclude-dir=website"
  "--exclude-dir=docs"
  "--exclude-dir=governance"
  "--exclude=DEPRECATED_TERMS.md"
  "--exclude=GOVERNANCE_ENFORCEMENT.md"
  "--exclude=deprecated-terms-check.yml"
  "--exclude=deprecated_terms_check.sh"
  "--exclude=forbidden-terms.yml"
  "--exclude=IMPLEMENTATION_SUMMARY.md"
  "--exclude=COPILOT_DELIVERABLES.md"
  "--exclude=FINAL_VALIDATION_REPORT.md"
  "--exclude=IMPLEMENTATION_SUMMARY_METADATA_AND_REGISTRY.md"
  "--exclude=RULESET_CONFIGURATION.md"
  "--exclude=*.log"
)

# Track failures
FAILURES=0

# Function to check for a pattern
check_pattern() {
  local label="$1"
  local pattern="$2"
  local message="$3"
  
  echo "Checking: $label"
  
  if grep -rIEn "${EXCLUDE_ARGS[@]}" "$pattern" . 2>/dev/null; then
    echo "❌ FAILED: $message"
    echo ""
    FAILURES=$((FAILURES + 1))
    return 1
  else
    echo "✅ PASSED: $label"
    echo ""
    return 0
  fi
}

# Check for STOE (word boundary)
check_pattern \
  "Deprecated term 'STOE'" \
  "\bSTOE\b" \
  "Found deprecated term 'STOE'. Remove completely."

# Check for V12-V22 (word boundary)
check_pattern \
  "Deprecated version labels V12-V22" \
  "\bV(12|13|14|15|16|17|18|19|20|21|22)\b" \
  "Found deprecated version labels (V12-V22). Remove completely."

# Check for "V<number> system" pattern
check_pattern \
  "Forbidden 'V<number> system' patterns" \
  "\bV[0-9]+[[:space:]]+system\b" \
  "Found forbidden 'V<number> system' pattern. Remove completely."

# Check for algorithm name variants
# Note: This checks for incorrect variants, canonical "AUTO DZ ACT" is allowed
if grep -rIEn "${EXCLUDE_ARGS[@]}" "AUTO-DZ-ACT|AutoDzAct|auto dz act" . 2>/dev/null; then
  echo "Checking: Algorithm name variants"
  echo "❌ FAILED: Found incorrect algorithm name variant"
  echo "   Only 'AUTO DZ ACT' (exact case and spacing) is allowed"
  echo ""
  FAILURES=$((FAILURES + 1))
fi

# Check for versioned algorithm names
if grep -rIEn "${EXCLUDE_ARGS[@]}" "AUTO DZ ACT[[:space:]]+system|AUTO DZ ACT[[:space:]]+v|AUTO DZ ACT[[:space:]]+V" . 2>/dev/null; then
  echo "Checking: Versioned algorithm names"
  echo "❌ FAILED: Found versioned or suffixed algorithm name"
  echo "   Do not append 'system', 'v1', etc. to 'AUTO DZ ACT'"
  echo ""
  FAILURES=$((FAILURES + 1))
fi

# Summary
echo "=========================================="
if [[ $FAILURES -eq 0 ]]; then
  echo "✅ ALL CHECKS PASSED"
  echo "✅ No deprecated terms found"
  echo "✅ Repository compliant with TRIZEL DIRECTIVE"
  exit 0
else
  echo "❌ CHECKS FAILED: $FAILURES violation(s) detected"
  echo ""
  echo "REMEDIATION:"
  echo "  1. Review the violations listed above"
  echo "  2. Remove all deprecated terms completely"
  echo "  3. Use only canonical forms (e.g., 'AUTO DZ ACT')"
  echo "  4. Refer to DEPRECATED_TERMS.md for complete policy"
  exit 1
fi
