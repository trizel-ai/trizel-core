#!/usr/bin/env python3
"""
Governance Repository Validator

This script validates that a repository complies with TRIZEL Layer 0 governance boundaries.
It checks for prohibited file types, required governance files, and other structural requirements.

This script provides a programmatic interface to the validation logic implemented in
.github/workflows/governance-validation.yml

Usage:
    python scripts/governance/validate_repo.py [--verbose]

Exit codes:
    0: All validations passed
    1: Validation failures detected
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List, Tuple


class GovernanceValidator:
    """Validates repository against Layer 0 governance boundaries"""
    
    # File extensions for executable code (prohibited in Layer 0)
    EXECUTABLE_EXTENSIONS = [
        '.py', '.js', '.ts', '.java', '.cpp', '.c', '.h', '.go', '.rs',
        '.rb', '.php', '.swift', '.cs', '.kt', '.m', '.mm', '.scala'
    ]
    
    # File extensions for data files (prohibited in Layer 0)
    DATA_EXTENSIONS = [
        '.csv', '.parquet', '.feather', '.arrow', '.db', '.sqlite', '.sqlite3',
        '.pkl', '.pickle', '.h5', '.hdf5', '.sav', '.dta', '.mat', '.ipynb'
    ]
    
    # Required governance files at repository root
    REQUIRED_FILES = [
        'COPILOT_INSTRUCTIONS.md',
        'ROLE.md',
        'OUTPUT_CONTRACT.md',
        'PUBLICATION_POLICY.md',
        'DEPRECATED_TERMS.md',
        'README.md',
    ]
    
    # Directories to exclude from validation
    # scripts/governance is allowed to contain governance automation scripts
    EXCLUDED_DIRS = {'.git', '.github'}
    
    # Additional path patterns to exclude
    EXCLUDED_PATHS = {'scripts/governance'}
    
    def __init__(self, repo_path: str = '.', verbose: bool = False):
        self.repo_path = Path(repo_path).resolve()
        self.verbose = verbose
        self.errors: List[str] = []
        self.warnings: List[str] = []
    
    def log(self, message: str):
        """Print message if verbose mode is enabled"""
        if self.verbose:
            print(message)
    
    def validate_no_executable_code(self) -> bool:
        """Check that no executable code files exist outside allowed directories"""
        self.log("Checking for executable code files...")
        
        found_files = []
        for root, dirs, files in os.walk(self.repo_path):
            # Skip excluded directories
            dirs[:] = [d for d in dirs if d not in self.EXCLUDED_DIRS]
            
            for file in files:
                if any(file.endswith(ext) for ext in self.EXECUTABLE_EXTENSIONS):
                    rel_path = os.path.relpath(os.path.join(root, file), self.repo_path)
                    # Also check for excluded paths
                    if not any(rel_path.startswith(excl) for excl in self.EXCLUDED_PATHS):
                        found_files.append(rel_path)
        
        if found_files:
            self.errors.append(
                "Found executable code files (prohibited in Layer 0):\n  " +
                "\n  ".join(found_files)
            )
            return False
        
        self.log("✓ No executable code files found")
        return True
    
    def validate_no_data_files(self) -> bool:
        """Check that no data files exist"""
        self.log("Checking for data files...")
        
        found_files = []
        for root, dirs, files in os.walk(self.repo_path):
            # Skip excluded directories
            dirs[:] = [d for d in dirs if d not in self.EXCLUDED_DIRS]
            
            for file in files:
                if any(file.endswith(ext) for ext in self.DATA_EXTENSIONS):
                    rel_path = os.path.relpath(os.path.join(root, file), self.repo_path)
                    found_files.append(rel_path)
        
        if found_files:
            self.errors.append(
                "Found data files (prohibited in Layer 0):\n  " +
                "\n  ".join(found_files)
            )
            return False
        
        self.log("✓ No data files found")
        return True
    
    def validate_required_files(self) -> bool:
        """Check that all required governance files exist"""
        self.log("Checking for required governance files...")
        
        missing_files = []
        for required_file in self.REQUIRED_FILES:
            file_path = self.repo_path / required_file
            if not file_path.exists():
                missing_files.append(required_file)
        
        if missing_files:
            self.errors.append(
                "Missing required governance files:\n  " +
                "\n  ".join(missing_files)
            )
            return False
        
        self.log("✓ All required governance files present")
        return True
    
    def validate_markdown_non_empty(self) -> bool:
        """Check that markdown files are non-empty"""
        self.log("Validating markdown files are non-empty...")
        
        empty_files = []
        for root, dirs, files in os.walk(self.repo_path):
            # Skip excluded directories
            dirs[:] = [d for d in dirs if d not in self.EXCLUDED_DIRS]
            
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    if os.path.getsize(file_path) == 0:
                        rel_path = os.path.relpath(file_path, self.repo_path)
                        empty_files.append(rel_path)
        
        if empty_files:
            self.errors.append(
                "Found empty markdown files:\n  " +
                "\n  ".join(empty_files)
            )
            return False
        
        self.log("✓ All markdown files are non-empty")
        return True
    
    def run_all_validations(self) -> bool:
        """Run all validation checks"""
        print("Running Layer 0 governance validation...")
        print(f"Repository: {self.repo_path}")
        print()
        
        results = [
            self.validate_no_executable_code(),
            self.validate_no_data_files(),
            self.validate_required_files(),
            self.validate_markdown_non_empty(),
        ]
        
        # Print results
        print()
        if self.errors:
            print("❌ VALIDATION FAILED")
            print()
            for error in self.errors:
                print(f"ERROR: {error}")
                print()
        else:
            print("✓ All governance validation checks PASSED")
            print("✓ Repository maintains Layer 0 boundaries")
            print("✓ No executable code, data files, or notebooks detected")
            print("✓ Required governance files present")
        
        return all(results)


def main():
    parser = argparse.ArgumentParser(
        description='Validate repository against TRIZEL Layer 0 governance boundaries'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output'
    )
    parser.add_argument(
        '--repo-path',
        default='.',
        help='Path to repository root (default: current directory)'
    )
    
    args = parser.parse_args()
    
    validator = GovernanceValidator(
        repo_path=args.repo_path,
        verbose=args.verbose
    )
    
    success = validator.run_all_validations()
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
