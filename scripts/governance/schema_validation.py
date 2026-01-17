#!/usr/bin/env python3
"""
Schema Validation Check
Validates YAML and JSON syntax for in-repo files
"""

import sys
import json
import yaml
from pathlib import Path
from typing import List, Tuple

def find_yaml_json_files(repo_path: Path) -> List[Path]:
    """Find all YAML and JSON files in the repository"""
    files = []
    
    # Exclude directories
    exclude_dirs = {
        '.git', 'node_modules', 'vendor', 'dist', 'build', 
        'target', '.venv', '.mypy_cache', '.pytest_cache', '__pycache__'
    }
    
    for ext in ['*.yml', '*.yaml', '*.json']:
        for file_path in repo_path.rglob(ext):
            # Check if any parent is in exclude_dirs
            if not any(parent.name in exclude_dirs for parent in file_path.parents):
                files.append(file_path)
    
    return files

def validate_yaml(file_path: Path) -> Tuple[bool, str]:
    """Validate YAML file syntax"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            yaml.safe_load(f)
        return True, ""
    except yaml.YAMLError as e:
        return False, str(e)
    except Exception as e:
        return False, f"Error reading file: {str(e)}"

def validate_json(file_path: Path) -> Tuple[bool, str]:
    """Validate JSON file syntax"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json.load(f)
        return True, ""
    except json.JSONDecodeError as e:
        return False, f"Line {e.lineno}, Column {e.colno}: {e.msg}"
    except Exception as e:
        return False, f"Error reading file: {str(e)}"

def main():
    print("=" * 50)
    print("SCHEMA VALIDATION CHECK")
    print("=" * 50)
    print()
    
    repo_path = Path.cwd()
    print(f"Repository: {repo_path}")
    print()
    
    # Find all YAML and JSON files
    files = find_yaml_json_files(repo_path)
    
    if not files:
        print("ℹ️  No YAML or JSON files found")
        return 0
    
    print(f"Found {len(files)} YAML/JSON files to validate")
    print()
    
    errors = []
    
    for file_path in sorted(files):
        rel_path = file_path.relative_to(repo_path)
        
        if file_path.suffix in ['.yml', '.yaml']:
            valid, error = validate_yaml(file_path)
        elif file_path.suffix == '.json':
            valid, error = validate_json(file_path)
        else:
            continue
        
        if not valid:
            errors.append((rel_path, error))
            print(f"❌ {rel_path}")
            print(f"   {error}")
        else:
            print(f"✅ {rel_path}")
    
    print()
    
    if errors:
        print(f"❌ VALIDATION FAILED: {len(errors)} file(s) with syntax errors")
        print()
        print("Files with errors:")
        for file_path, error in errors:
            print(f"  - {file_path}")
            print(f"    Error: {error}")
        return 1
    else:
        print(f"✅ ALL FILES VALID: {len(files)} file(s) passed validation")
        return 0

if __name__ == '__main__':
    sys.exit(main())
