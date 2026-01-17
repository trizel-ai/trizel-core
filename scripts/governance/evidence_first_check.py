#!/usr/bin/env python3
"""
Evidence First Check
Enforces evidence-first metadata requirements for identified artifacts
"""

import sys
import re
from pathlib import Path
from typing import List, Tuple, Dict

# Patterns that identify files requiring evidence metadata
# Conservative: only files that are clearly evidence/artifact records
EVIDENCE_PATTERNS = [
    r'evidence[_-]record',
    r'evidence[_-]artifact',
    r'artifact[_-]record',
    r'manifest[_-]record',
]

# Required metadata fields for evidence-first artifacts
REQUIRED_FIELDS = [
    'Evidence',
    'Method',
    'Validation',
    'ImmutableRefs',
]

def should_check_file(file_path: Path) -> bool:
    """Determine if a file should be checked for evidence metadata"""
    # Only check markdown files
    if file_path.suffix != '.md':
        return False
    
    # Exclude certain directories
    exclude_dirs = {'.git', 'node_modules', 'vendor', 'dist', 'build', 'target'}
    if any(parent.name in exclude_dirs for parent in file_path.parents):
        return False
    
    # Check if filename or path contains evidence-related keywords
    path_str = str(file_path).lower()
    for pattern in EVIDENCE_PATTERNS:
        if re.search(pattern, path_str, re.IGNORECASE):
            return True
    
    return False

def check_evidence_metadata(file_path: Path) -> Tuple[bool, List[str]]:
    """Check if file contains required evidence metadata"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return False, [f"Error reading file: {str(e)}"]
    
    # Look for evidence metadata section
    # This is a conservative check - only fails if file clearly should have metadata
    # but is missing required fields
    
    # Check if file appears to be a metadata/evidence file by looking for headers
    has_metadata_section = any([
        re.search(r'##\s*(Metadata|Evidence|Validation|Method)', content, re.IGNORECASE),
        re.search(r'\*\*Evidence\*\*:|Evidence:', content),
        re.search(r'\*\*Method\*\*:|Method:', content),
    ])
    
    if not has_metadata_section:
        # File doesn't appear to be a formal evidence record
        # No enforcement needed
        return True, []
    
    # If file has metadata section, check for required fields
    missing_fields = []
    for field in REQUIRED_FIELDS:
        # Look for field with various formats: "**Field**:", "Field:", "## Field"
        patterns = [
            rf'\*\*{field}\*\*\s*:',
            rf'{field}\s*:',
            rf'##\s+{field}',
        ]
        
        found = any(re.search(pattern, content, re.IGNORECASE) for pattern in patterns)
        if not found:
            missing_fields.append(field)
    
    if missing_fields:
        return False, missing_fields
    
    return True, []

def main():
    print("=" * 50)
    print("EVIDENCE FIRST CHECK")
    print("=" * 50)
    print()
    
    repo_path = Path.cwd()
    print(f"Repository: {repo_path}")
    print()
    print("Checking for evidence-first metadata compliance...")
    print()
    
    # Find all markdown files that should be checked
    files_to_check = []
    for md_file in repo_path.rglob('*.md'):
        if should_check_file(md_file):
            files_to_check.append(md_file)
    
    if not files_to_check:
        print("ℹ️  No evidence/artifact files found requiring metadata")
        print("✅ Check passed (nothing to validate)")
        return 0
    
    print(f"Found {len(files_to_check)} file(s) to check:")
    for f in files_to_check:
        print(f"  - {f.relative_to(repo_path)}")
    print()
    
    failures = []
    
    for file_path in files_to_check:
        rel_path = file_path.relative_to(repo_path)
        valid, missing = check_evidence_metadata(file_path)
        
        if not valid:
            failures.append((rel_path, missing))
            print(f"❌ {rel_path}")
            print(f"   Missing fields: {', '.join(missing)}")
        else:
            print(f"✅ {rel_path}")
    
    print()
    print("=" * 50)
    
    if failures:
        print(f"❌ CHECKS FAILED: {len(failures)} file(s) missing required metadata")
        print()
        print("Files requiring evidence metadata:")
        for file_path, missing in failures:
            print(f"  - {file_path}")
            print(f"    Missing: {', '.join(missing)}")
        print()
        print("REMEDIATION:")
        print("  Evidence-first files must include:")
        print("    - Evidence: Description of evidence source")
        print("    - Method: How evidence was obtained")
        print("    - Validation: How evidence was validated")
        print("    - ImmutableRefs: Commit hashes or content hashes")
        return 1
    else:
        print(f"✅ ALL CHECKS PASSED")
        print(f"✅ {len(files_to_check)} file(s) have proper evidence metadata")
        return 0

if __name__ == '__main__':
    sys.exit(main())
