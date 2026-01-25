# Gate 3A — Output Schema Definition
## DERIVED Package Metadata Schemas (Definition-Only)

**Repository:** trizel-ai/trizel-core  
**Authorization ID:** GATE-3A-LAB-EXEC-001  
**Document Type:** Schema Definition (Non-Executable)  
**Effective Date:** 2026-01-25  
**Status:** PENDING APPROVAL  
**Schema Version:** 1.0.0

---

## 1. Purpose

This document defines **minimal JSON schema examples** for DERIVED packages produced under Gate 3A authorization.

**Critical Constraints:**
- These schemas are **DEFINITION-ONLY** (governance documentation)
- These schemas are **NOT** used by executable code in this PR
- These schemas provide **governance reference** for future implementation
- These schemas are **examples only** and may be refined under separate authorization

**Scope:**
- Define structure for `derived-manifest.json` (SHA-256 map)
- Define structure for `derived-status.json` (validation state)
- Define minimal requirements for `ro-crate-metadata.json`

**Non-Scope:**
- This document does NOT implement validation logic
- This document does NOT provide executable schema validators
- This document does NOT authorize code that uses these schemas

---

## 2. Common Metadata Requirements

All DERIVED package metadata files must include the following common fields:

### 2.1 Required Fields (All Metadata Files)

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `gate` | string | Gate authorization identifier | `"3A"` |
| `proof_type` | string | Proof classification | `"lab-derived"` |
| `as_of_utc` | string | ISO 8601 UTC timestamp | `"2026-01-25T23:00:00Z"` |
| `provenance` | object | Source tracking metadata | See Section 2.2 |
| `integrity` | object | Cryptographic integrity metadata | See Section 2.3 |

### 2.2 Provenance Object Structure

```json
{
  "provenance": {
    "source_repository": "https://github.com/trizel-ai/trizel-observatory",
    "source_path": "snapshots/3I-ATLAS/snapshot-2026-01-20.json",
    "source_commit": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0",
    "source_package_type": "SNAPSHOT",
    "source_package_checksum": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "transformation_method": "Orbital trajectory integration using Runge-Kutta 4th order method",
    "transformation_timestamp_utc": "2026-01-25T22:30:00Z"
  }
}
```

**Required Provenance Fields:**
- `source_repository` — URL or identifier of source repository
- `source_path` — Path to source file within repository
- `source_commit` — Git commit SHA or immutable version reference
- `source_package_type` — Type of source package (e.g., "SNAPSHOT")
- `source_package_checksum` — SHA-256 checksum of source package
- `transformation_method` — Description of analytical operation applied
- `transformation_timestamp_utc` — ISO 8601 UTC timestamp of transformation

### 2.3 Integrity Object Structure

```json
{
  "integrity": {
    "algorithm": "SHA-256",
    "checksums": {
      "derived-data.json": "5d41402abc4b2a76b9719d911017c592e9e5c8b2f8e8b8e8b8e8b8e8b8e8b8e8",
      "validation-trace.json": "7d793037a0760186574b0282f2f435e4d45d5e5e5e5e5e5e5e5e5e5e5e5e5e5e"
    },
    "manifest_checksum": "9e107d9d372bb6826bd81d3542a419d6e7e7e7e7e7e7e7e7e7e7e7e7e7e7e7e7"
  }
}
```

**Required Integrity Fields:**
- `algorithm` — Hash algorithm (must be "SHA-256")
- `checksums` — Object mapping filenames to SHA-256 checksums
- `manifest_checksum` — SHA-256 checksum of the manifest file itself

---

## 3. Derived Manifest Schema

### 3.1 Purpose

The `derived-manifest.json` file provides a **complete inventory** of all files in a DERIVED package with cryptographic integrity checksums.

### 3.2 Minimal Schema Example

```json
{
  "schema_version": "1.0.0",
  "package_type": "DERIVED",
  "gate": "3A",
  "proof_type": "lab-derived",
  "package_id": "DERIVED-3I-ATLAS-ORBIT-2026-01-25",
  "as_of_utc": "2026-01-25T23:00:00Z",
  "provenance": {
    "source_repository": "https://github.com/trizel-ai/trizel-observatory",
    "source_path": "snapshots/3I-ATLAS/snapshot-2026-01-20.json",
    "source_commit": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0",
    "source_package_type": "SNAPSHOT",
    "source_package_checksum": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "transformation_method": "Orbital trajectory integration using Runge-Kutta 4th order method",
    "transformation_timestamp_utc": "2026-01-25T22:30:00Z",
    "transformation_tool": "orbital-integrator v2.1.3",
    "transformation_parameters": {
      "time_step_seconds": 3600,
      "integration_duration_days": 365,
      "gravitational_model": "JPL DE440"
    }
  },
  "integrity": {
    "algorithm": "SHA-256",
    "checksums": {
      "derived-data.json": "5d41402abc4b2a76b9719d911017c592e9e5c8b2f8e8b8e8b8e8b8e8b8e8b8e8",
      "validation-trace.json": "7d793037a0760186574b0282f2f435e4d45d5e5e5e5e5e5e5e5e5e5e5e5e5e5e",
      "ro-crate-metadata.json": "8f14e45fceea167a5a36dedd4bea2543d8e8e8e8e8e8e8e8e8e8e8e8e8e8e8e8",
      "README.md": "6c3fd04de5d5e5e5e5e5e5e5e5e5e5e5e5e5e5e5e5e5e5e5e5e5e5e5e5e5e5e"
    },
    "manifest_checksum": "9e107d9d372bb6826bd81d3542a419d6e7e7e7e7e7e7e7e7e7e7e7e7e7e7e7e7"
  },
  "file_count": 4,
  "total_size_bytes": 524288,
  "reproducibility_notes": "Integration requires JPL DE440 ephemeris file (SHA-256: d3e4f5...). Random seed not applicable (deterministic integration).",
  "created_by": "trizel-lab-pipeline v1.0.0",
  "created_at_utc": "2026-01-25T23:00:00Z"
}
```

### 3.3 Required Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `schema_version` | string | Yes | Schema version identifier |
| `package_type` | string | Yes | Must be `"DERIVED"` |
| `gate` | string | Yes | Must be `"3A"` |
| `proof_type` | string | Yes | Must be `"lab-derived"` |
| `package_id` | string | Yes | Unique identifier for this package |
| `as_of_utc` | string | Yes | ISO 8601 UTC timestamp |
| `provenance` | object | Yes | See Section 2.2 |
| `integrity` | object | Yes | See Section 2.3 |
| `file_count` | integer | Yes | Number of files in package |
| `total_size_bytes` | integer | No | Total package size (recommended) |
| `reproducibility_notes` | string | No | Notes for reproducibility (recommended) |
| `created_by` | string | Yes | Tool or pipeline identifier |
| `created_at_utc` | string | Yes | ISO 8601 UTC timestamp |

---

## 4. Derived Status Schema

### 4.1 Purpose

The `derived-status.json` file provides a **non-interpretive validation state** for a DERIVED package.

**Permitted Status Values:**
- `"VALID"` — All validation checks passed
- `"INVALID"` — One or more validation checks failed
- `"INCONCLUSIVE"` — Validation could not determine status
- `"PENDING"` — Validation not yet completed

### 4.2 Minimal Schema Example

```json
{
  "schema_version": "1.0.0",
  "package_type": "DERIVED",
  "gate": "3A",
  "proof_type": "lab-derived",
  "package_id": "DERIVED-3I-ATLAS-ORBIT-2026-01-25",
  "as_of_utc": "2026-01-25T23:00:00Z",
  "provenance": {
    "source_repository": "https://github.com/trizel-ai/trizel-observatory",
    "source_path": "snapshots/3I-ATLAS/snapshot-2026-01-20.json",
    "source_commit": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0",
    "source_package_type": "SNAPSHOT",
    "source_package_checksum": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "transformation_method": "Orbital trajectory integration using Runge-Kutta 4th order method",
    "transformation_timestamp_utc": "2026-01-25T22:30:00Z"
  },
  "integrity": {
    "algorithm": "SHA-256",
    "checksums": {
      "derived-status.json": "7d793037a0760186574b0282f2f435e4d45d5e5e5e5e5e5e5e5e5e5e5e5e5e5e"
    },
    "manifest_checksum": "9e107d9d372bb6826bd81d3542a419d6e7e7e7e7e7e7e7e7e7e7e7e7e7e7e7e7"
  },
  "validation_status": "VALID",
  "validation_timestamp_utc": "2026-01-25T23:00:00Z",
  "validation_trace": [
    {
      "check_id": "checksum-verification",
      "check_description": "Verify SHA-256 checksums for all files",
      "check_result": "PASS",
      "check_timestamp_utc": "2026-01-25T22:55:00Z"
    },
    {
      "check_id": "provenance-verification",
      "check_description": "Verify source package exists and matches checksum",
      "check_result": "PASS",
      "check_timestamp_utc": "2026-01-25T22:56:00Z"
    },
    {
      "check_id": "schema-validation",
      "check_description": "Validate JSON schema compliance for all metadata files",
      "check_result": "PASS",
      "check_timestamp_utc": "2026-01-25T22:57:00Z"
    },
    {
      "check_id": "reproducibility-check",
      "check_description": "Verify transformation can be reproduced with documented parameters",
      "check_result": "PASS",
      "check_timestamp_utc": "2026-01-25T22:59:00Z"
    }
  ],
  "validation_summary": {
    "total_checks": 4,
    "passed_checks": 4,
    "failed_checks": 0,
    "inconclusive_checks": 0
  },
  "validation_tool": "trizel-validator v1.2.0",
  "validation_notes": "All checks passed. Package is ready for archival."
}
```

### 4.3 Required Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `schema_version` | string | Yes | Schema version identifier |
| `package_type` | string | Yes | Must be `"DERIVED"` |
| `gate` | string | Yes | Must be `"3A"` |
| `proof_type` | string | Yes | Must be `"lab-derived"` |
| `package_id` | string | Yes | Unique identifier for this package |
| `as_of_utc` | string | Yes | ISO 8601 UTC timestamp |
| `provenance` | object | Yes | See Section 2.2 |
| `integrity` | object | Yes | See Section 2.3 |
| `validation_status` | string | Yes | One of: VALID, INVALID, INCONCLUSIVE, PENDING |
| `validation_timestamp_utc` | string | Yes | ISO 8601 UTC timestamp |
| `validation_trace` | array | Yes | Array of validation check objects (see 4.4) |
| `validation_summary` | object | No | Summary statistics (recommended) |
| `validation_tool` | string | Yes | Tool identifier |
| `validation_notes` | string | No | Free-form notes (non-interpretive) |

### 4.4 Validation Trace Entry Structure

Each entry in `validation_trace` must include:

```json
{
  "check_id": "unique-check-identifier",
  "check_description": "Human-readable description of check",
  "check_result": "PASS or FAIL or INCONCLUSIVE",
  "check_timestamp_utc": "2026-01-25T22:55:00Z",
  "check_details": "Optional details about check execution",
  "check_error": "Optional error message if FAIL"
}
```

**Required Validation Trace Fields:**
- `check_id` — Unique identifier for this validation check
- `check_description` — Human-readable description
- `check_result` — One of: PASS, FAIL, INCONCLUSIVE
- `check_timestamp_utc` — ISO 8601 UTC timestamp

---

## 5. RO-Crate Metadata Minimal Requirements

### 5.1 Purpose

The `ro-crate-metadata.json` file provides **Research Object Crate metadata** conforming to the RO-Crate specification with Gate 3A extensions.

**Reference:** https://www.researchobject.org/ro-crate/specification.html

### 5.2 Minimal Schema Example

```json
{
  "@context": "https://w3id.org/ro/crate/1.1/context",
  "@graph": [
    {
      "@type": "CreativeWork",
      "@id": "ro-crate-metadata.json",
      "conformsTo": {
        "@id": "https://w3id.org/ro/crate/1.1"
      },
      "about": {
        "@id": "./"
      },
      "description": "RO-Crate metadata for DERIVED package DERIVED-3I-ATLAS-ORBIT-2026-01-25"
    },
    {
      "@type": "Dataset",
      "@id": "./",
      "name": "DERIVED-3I-ATLAS-ORBIT-2026-01-25",
      "description": "Orbital trajectory integration for interstellar object 3I/ATLAS covering 365 days from 2026-01-20 using Runge-Kutta 4th order method.",
      "dateCreated": "2026-01-25T23:00:00Z",
      "license": {
        "@id": "https://creativecommons.org/licenses/by-nc-nd/4.0/"
      },
      "creator": {
        "@type": "Organization",
        "@id": "https://trizel.ai",
        "name": "TRIZEL Governance Framework"
      },
      "hasPart": [
        {
          "@id": "derived-data.json"
        },
        {
          "@id": "validation-trace.json"
        },
        {
          "@id": "derived-manifest.json"
        },
        {
          "@id": "derived-status.json"
        }
      ],
      "additionalProperty": [
        {
          "@type": "PropertyValue",
          "name": "gate",
          "value": "3A"
        },
        {
          "@type": "PropertyValue",
          "name": "proof_type",
          "value": "lab-derived"
        },
        {
          "@type": "PropertyValue",
          "name": "validation_status",
          "value": "VALID"
        },
        {
          "@type": "PropertyValue",
          "name": "source_repository",
          "value": "https://github.com/trizel-ai/trizel-observatory"
        },
        {
          "@type": "PropertyValue",
          "name": "source_commit",
          "value": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0"
        },
        {
          "@type": "PropertyValue",
          "name": "source_package_checksum",
          "value": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
        }
      ]
    },
    {
      "@type": "File",
      "@id": "derived-data.json",
      "name": "Derived Data",
      "description": "Orbital trajectory data",
      "encodingFormat": "application/json",
      "contentSize": "262144",
      "sha256": "5d41402abc4b2a76b9719d911017c592e9e5c8b2f8e8b8e8b8e8b8e8b8e8b8e8"
    },
    {
      "@type": "File",
      "@id": "validation-trace.json",
      "name": "Validation Trace",
      "description": "Validation check records",
      "encodingFormat": "application/json",
      "contentSize": "16384",
      "sha256": "7d793037a0760186574b0282f2f435e4d45d5e5e5e5e5e5e5e5e5e5e5e5e5e5e"
    },
    {
      "@type": "File",
      "@id": "derived-manifest.json",
      "name": "Derived Manifest",
      "description": "Package manifest with checksums",
      "encodingFormat": "application/json",
      "contentSize": "8192",
      "sha256": "8f14e45fceea167a5a36dedd4bea2543d8e8e8e8e8e8e8e8e8e8e8e8e8e8e8e8"
    },
    {
      "@type": "File",
      "@id": "derived-status.json",
      "name": "Derived Status",
      "description": "Validation status and trace",
      "encodingFormat": "application/json",
      "contentSize": "4096",
      "sha256": "9e107d9d372bb6826bd81d3542a419d6e7e7e7e7e7e7e7e7e7e7e7e7e7e7e7e7"
    }
  ]
}
```

### 5.3 Required RO-Crate Fields

**Root Descriptor Entity (ro-crate-metadata.json):**
- `@type`: Must be `"CreativeWork"`
- `@id`: Must be `"ro-crate-metadata.json"`
- `conformsTo`: Must reference RO-Crate version
- `about`: Must reference the root dataset (`./`)

**Root Dataset Entity (./):**
- `@type`: Must be `"Dataset"`
- `@id`: Must be `"./"`
- `name`: Package identifier
- `description`: Non-interpretive description of package contents
- `dateCreated`: ISO 8601 UTC timestamp
- `license`: License identifier (URL or SPDX code)
- `creator`: Organization or Person entity
- `hasPart`: Array of file references included in package
- `additionalProperty`: Array of Gate 3A-specific properties (see 5.4)

**File Entities:**
Each file must have:
- `@type`: Must be `"File"`
- `@id`: Filename
- `name`: Human-readable name
- `description`: Non-interpretive description
- `encodingFormat`: MIME type
- `contentSize`: File size in bytes (optional but recommended)
- `sha256`: SHA-256 checksum

### 5.4 Gate 3A-Specific Additional Properties

All RO-Crate packages for DERIVED artifacts must include the following additional properties:

```json
{
  "additionalProperty": [
    {
      "@type": "PropertyValue",
      "name": "gate",
      "value": "3A"
    },
    {
      "@type": "PropertyValue",
      "name": "proof_type",
      "value": "lab-derived"
    },
    {
      "@type": "PropertyValue",
      "name": "validation_status",
      "value": "VALID"
    },
    {
      "@type": "PropertyValue",
      "name": "source_repository",
      "value": "https://github.com/trizel-ai/trizel-observatory"
    },
    {
      "@type": "PropertyValue",
      "name": "source_commit",
      "value": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0"
    },
    {
      "@type": "PropertyValue",
      "name": "source_package_checksum",
      "value": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    }
  ]
}
```

**Required Additional Properties:**
- `gate`: Must be `"3A"`
- `proof_type`: Must be `"lab-derived"`
- `validation_status`: One of VALID, INVALID, INCONCLUSIVE, PENDING
- `source_repository`: URL or identifier of source repository
- `source_commit`: Git commit SHA or immutable version reference
- `source_package_checksum`: SHA-256 checksum of source package

---

## 6. Validation Examples

### 6.1 Example: VALID Status

```json
{
  "validation_status": "VALID",
  "validation_trace": [
    {
      "check_id": "checksum-verification",
      "check_description": "Verify SHA-256 checksums for all files",
      "check_result": "PASS",
      "check_timestamp_utc": "2026-01-25T22:55:00Z"
    }
  ]
}
```

### 6.2 Example: INVALID Status

```json
{
  "validation_status": "INVALID",
  "validation_trace": [
    {
      "check_id": "checksum-verification",
      "check_description": "Verify SHA-256 checksums for all files",
      "check_result": "FAIL",
      "check_timestamp_utc": "2026-01-25T22:55:00Z",
      "check_error": "Checksum mismatch for derived-data.json: expected 5d41402abc..., got 6e52513bdf..."
    }
  ]
}
```

### 6.3 Example: INCONCLUSIVE Status

```json
{
  "validation_status": "INCONCLUSIVE",
  "validation_trace": [
    {
      "check_id": "reproducibility-check",
      "check_description": "Verify transformation can be reproduced with documented parameters",
      "check_result": "INCONCLUSIVE",
      "check_timestamp_utc": "2026-01-25T22:59:00Z",
      "check_details": "Required external ephemeris file (JPL DE440) not available for verification. Checksum matches documented value but reproduction not verified."
    }
  ]
}
```

### 6.4 Example: PENDING Status

```json
{
  "validation_status": "PENDING",
  "validation_trace": [],
  "validation_notes": "Validation not yet initiated. Package awaiting quality review queue."
}
```

---

## 7. Checksum Computation Guidelines

### 7.1 SHA-256 Algorithm

All checksums must use the **SHA-256 cryptographic hash algorithm**.

**Command-line Example (Linux/macOS):**
```bash
sha256sum filename.json
```

**Command-line Example (Windows):**
```powershell
Get-FileHash -Algorithm SHA256 filename.json
```

**Python Example:**
```python
import hashlib

def compute_sha256(filepath):
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()
```

### 7.2 Manifest Checksum

The `manifest_checksum` field contains the SHA-256 checksum of the manifest file **itself** (excluding the `manifest_checksum` field).

**Procedure:**
1. Generate manifest file with all fields EXCEPT `manifest_checksum`
2. Compute SHA-256 checksum of the incomplete manifest file
3. Insert checksum value into `manifest_checksum` field
4. Do NOT recompute checksum after insertion

---

## 8. Schema Versioning

### 8.1 Current Version

**Schema Version:** 1.0.0  
**Effective Date:** 2026-01-25  
**Status:** PENDING APPROVAL

### 8.2 Version Compatibility

Future versions of Gate 3A schemas will maintain backward compatibility where possible.

**Breaking Changes:**
- Require new major version (e.g., 2.0.0)
- Require separate governance authorization
- May not be applied to existing DERIVED packages without re-validation

**Non-Breaking Changes:**
- Require new minor version (e.g., 1.1.0)
- May add optional fields
- May add recommended fields
- May clarify field descriptions

---

## 9. Implementation Notes

### 9.1 Definition-Only Status

**CRITICAL REMINDER:**  
These schemas are **DEFINITION-ONLY** governance documentation.

**This document does NOT:**
- Implement validation code
- Provide executable schema validators
- Authorize code that generates these metadata files
- Enable execution of any workflows or pipelines

**Implementation Authorization:**  
Separate governance authorization is required to implement code that uses these schemas.

### 9.2 Future Implementation Planning

When implementation is authorized (under separate gate), the following activities may be permitted:
- Code that generates DERIVED packages conforming to these schemas
- Code that validates DERIVED packages against these schemas
- Code that parses and verifies provenance chains
- Code that computes and verifies SHA-256 checksums

**Governance Requirement:**  
All implementation code must be authorized under separate gate (not Gate 3A).

---

## 10. References

### 10.1 RO-Crate Specification

**Title:** RO-Crate Metadata Specification 1.1  
**URL:** https://www.researchobject.org/ro-crate/specification.html  
**Purpose:** Research Object Crate standard for packaging research data

### 10.2 Gate 3A Authorization

**Document:** GATE_3A_LAB_EXECUTION_AUTHORIZATION.md  
**Purpose:** Gate 3A authorization constraints and requirements

### 10.3 Allowed/Forbidden Matrix

**Document:** GATE_3A_ALLOWED_FORBIDDEN_MATRIX.md  
**Purpose:** Activity constraints for Layer-3 and Layer-2

---

**END OF SCHEMA DEFINITION DOCUMENT**
