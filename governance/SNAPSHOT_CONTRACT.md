# SNAPSHOT CONTRACT

**Repository**: `trizel-ai/trizel-core`  
**Layer**: 0 — Governance  
**Contract Version**: 1.0.0  
**Effective Date**: 2026-01-21  
**Status**: Active

---

## Purpose

This document defines the technical contract for immutable scientific snapshots in the TRIZEL ecosystem.

A **snapshot** is a frozen, hash-verified, time-stamped collection of files representing a complete scientific artifact at a specific point in time.

---

## Scope

This contract governs:

1. **Snapshot immutability** requirements
2. **Hashing and verification** standards
3. **Manifest structure** and content
4. **Timestamping** protocols
5. **Versioning** conventions

This contract applies to:
- All scientific outputs eligible for DOI issuance
- All artifacts submitted for governance review
- All content referenced in Layer-2 presentation

---

## Core Principles

### 1. Immutability is Non-Negotiable

Once a snapshot is created:
- **No modifications** to any file
- **No additions** of new files
- **No deletions** of existing files
- **No metadata edits** (except governance approval status)

**Violation = snapshot invalidated**

### 2. Hash Verification is Mandatory

Every snapshot must:
- Have a cryptographic hash for every file
- Have a manifest hash for the complete collection
- Support independent verification
- Detect any modification attempts

**No hash = not a snapshot**

### 3. Time is Immutable

Snapshot timestamps:
- Recorded at creation time
- Never modified retroactively
- Used for provenance tracking
- Part of the immutable record

**Timestamp tampering = snapshot invalidated**

### 4. Completeness is Required

A snapshot must be:
- Self-contained (all dependencies declared)
- Fully manifested (all files listed)
- Completely described (metadata complete)
- Independently reproducible (given manifest)

**Incomplete snapshot = not eligible for DOI**

---

## Snapshot Immutability

### Immutability Definition

A snapshot is **immutable** if:

1. **Files cannot change**: Content of every file is fixed
2. **Structure cannot change**: No files added or removed
3. **Metadata is fixed**: Descriptive information locked
4. **Hashes verify**: Cryptographic verification succeeds
5. **Timestamps are permanent**: Creation time never changes

### Immutability Enforcement

Immutability is enforced through:

#### Technical Controls
- **Read-only storage**: Files stored in read-only mode
- **Hash verification**: Regular integrity checks
- **Git tags**: Immutable references (no force-push)
- **Archive format**: Packaged in tamper-evident format

#### Governance Controls
- **Review process**: Snapshot reviewed before approval
- **Approval record**: Snapshot state logged in governance
- **Rejection on modification**: Any change invalidates snapshot
- **Resubmission required**: Modified content = new snapshot

### Immutability Verification

To verify snapshot immutability:

1. **Compute file hashes**: SHA-256 for each file
2. **Compare with manifest**: Check against recorded hashes
3. **Verify manifest hash**: Check manifest integrity
4. **Check timestamps**: Verify creation time unchanged
5. **Inspect git tag**: Verify tag points to correct commit

**All checks must pass**

---

## Hashing Requirements

### Minimum Hash Algorithm: SHA-256

All snapshots must use **SHA-256 or stronger** cryptographic hash functions.

**Acceptable algorithms**:
- SHA-256 (minimum required)
- SHA-384 (stronger, acceptable)
- SHA-512 (stronger, acceptable)
- SHA3-256 or SHA3-512 (acceptable)

**Not acceptable**:
- MD5 (cryptographically broken)
- SHA-1 (deprecated, collision vulnerabilities)
- CRC32 (checksum, not cryptographic)
- Custom hash functions (not verifiable)

### Hash Computation

Hashes must be computed:

1. **For every file**: Individual file hashes
2. **For the manifest**: Hash of the complete manifest
3. **Deterministically**: Same input → same hash
4. **Independently verifiable**: Using standard tools

### Hash Format

Hashes must be recorded in lowercase hexadecimal format:

**Example**:
```
a3c5f1e2b9d8c7a6f5e4d3c2b1a09876543210fedcba9876543210fedcba98
```

**Not allowed**:
- Uppercase hex (use lowercase only)
- Base64 encoding (use hex)
- Truncated hashes (use full length)
- Prefixes or suffixes (hash only)

### Hash Verification Protocol

To verify a snapshot:

```bash
# 1. Compute hash of each file
sha256sum file1.txt file2.csv file3.json > computed_hashes.txt

# 2. Compare with manifest
diff manifest_hashes.txt computed_hashes.txt

# 3. Verify manifest integrity
sha256sum manifest.json
# Compare output with recorded manifest hash

# 4. All must match exactly
```

---

## Manifest Structure

### Manifest Definition

A **manifest** is a structured inventory of all files in the snapshot, including:
- File paths
- File hashes
- File sizes
- Creation timestamp
- Snapshot metadata

### Manifest Format: JSON

Manifests must be in JSON format with the following structure:

**Example** (snapshot from Layer-1 repository `trizel-ai/trizel-AI`):

```json
{
  "manifest_version": "1.0.0",
  "snapshot_id": "unique-identifier",
  "snapshot_timestamp": "2026-01-21T22:30:00Z",
  "hash_algorithm": "SHA-256",
  "manifest_hash": "sha256-of-this-manifest-before-this-field-added",
  "files": [
    {
      "path": "data/observation_001.csv",
      "size_bytes": 1024,
      "hash": "a3c5f1e2b9d8c7a6f5e4d3c2b1a09876543210fedcba9876543210fedcba98"
    },
    {
      "path": "results/analysis_summary.json",
      "size_bytes": 512,
      "hash": "b4d6f2e3c9a8b7c6d5e4f3a2b1098765432101fedcba9876543210fedcba87"
    }
  ],
  "metadata": {
    "title": "Snapshot Title",
    "version": "1.0.0",
    "authors": ["Author Name"],
    "method_reference": "AUTO-DZ-ACT",
    "method_version": "1.0",
    "scope": "Description of snapshot scope"
  },
  "provenance": {
    "repository": "trizel-ai/trizel-AI",
    "branch": "main",
    "commit": "abc123def456",
    "created_by": "system-or-username",
    "created_at": "2026-01-21T22:30:00Z"
  }
}
```

**Note**: The `repository` field in provenance identifies where the scientific output was produced (typically `trizel-ai/trizel-AI` for Layer-1 research). This governance contract itself resides in `trizel-ai/trizel-core` (Layer-0).

### Required Manifest Fields

#### Top-Level Fields
- `manifest_version`: Contract version (e.g., "1.0.0")
- `snapshot_id`: Unique identifier for this snapshot
- `snapshot_timestamp`: ISO 8601 creation timestamp
- `hash_algorithm`: Hash algorithm used (e.g., "SHA-256")
- `manifest_hash`: Hash of manifest itself
- `files`: Array of file records
- `metadata`: Scientific metadata object
- `provenance`: Origin and creation information

#### File Record Fields
Each entry in `files` array must have:
- `path`: Relative path within snapshot
- `size_bytes`: File size in bytes
- `hash`: SHA-256 hash (lowercase hex)

#### Metadata Fields
Required in `metadata` object:
- `title`: Descriptive title
- `version`: Snapshot version
- `authors`: Array of author names
- `method_reference`: Canonical method identifier
- `method_version`: Method version used
- `scope`: Explicit scope statement

#### Provenance Fields
Required in `provenance` object:
- `repository`: Source repository
- `branch`: Source branch
- `commit`: Git commit SHA
- `created_by`: Creator identifier
- `created_at`: ISO 8601 timestamp

### Manifest Validation

Before accepting a manifest:

1. **Schema check**: Verify all required fields present
2. **Format check**: Verify JSON syntax valid
3. **Hash check**: Verify all hashes are valid hex strings
4. **Timestamp check**: Verify ISO 8601 format
5. **Completeness check**: Verify no placeholders (TBD, TODO, etc.)
6. **Consistency check**: Verify manifest_hash matches computed hash

**All checks must pass**

### Manifest Immutability

Once created, the manifest is **immutable** except for:
- Adding governance approval status (in separate file)
- Adding assigned DOI (in separate file)

**Core manifest content never changes**

---

## Timestamping and Versioning

### Timestamp Requirements

#### Format: ISO 8601

All timestamps must use ISO 8601 format with UTC timezone:

**Format**: `YYYY-MM-DDTHH:MM:SSZ`

**Example**: `2026-01-21T22:30:00Z`

**Required elements**:
- Date: Year, month, day
- Time: Hour, minute, second
- Timezone: Z (UTC)
- Separator: T

**Not allowed**:
- Local timezones (use UTC only)
- Fractional seconds (whole seconds only)
- Timezone offsets (use Z for UTC)
- Unix timestamps (use ISO 8601)

#### Timestamp Accuracy

Timestamps must be:
- **Accurate**: Within reasonable clock accuracy (< 1 minute drift)
- **Monotonic**: Later snapshots have later timestamps
- **Immutable**: Never modified after creation
- **Traceable**: Source clock documented

#### Timestamp Sources

Acceptable timestamp sources:
- System clock (NTP-synchronized preferred)
- Git commit timestamp (if using git)
- Build system timestamp
- Trusted timestamp authority (if available)

**Not acceptable**:
- Manual entry (too error-prone)
- Retroactive timestamps (immutability violation)
- Arbitrary timestamps (not traceable)

### Versioning Requirements

#### Version Format: Semantic Versioning

Snapshot versions should follow semantic versioning (semver):

**Format**: `MAJOR.MINOR.PATCH`

**Example**: `1.0.0`

**Rules**:
- MAJOR: Incompatible changes, new methodology, scope change
- MINOR: Backwards-compatible additions, refinements
- PATCH: Backwards-compatible fixes, corrections

#### Version Immutability

Once a version is published:
- **Version number is permanent**: Never reused
- **Content is frozen**: No modifications to that version
- **New version required**: For any changes

#### Version Relationships

Related snapshots should use consistent versioning:

**Example progression**:
- `1.0.0`: Initial snapshot
- `1.1.0`: Extended dataset, same method
- `1.1.1`: Corrected metadata, same data
- `2.0.0`: Different method, incompatible

### Snapshot Identifier

Each snapshot must have a **unique identifier**:

**Format options**:
1. **Version-based**: `{method}-{version}` (e.g., `AUTO-DZ-ACT-1.0.0`)
2. **Timestamp-based**: `{method}-{YYYYMMDD}` (e.g., `AUTO-DZ-ACT-20260121`)
3. **Hash-based**: `{method}-{short-hash}` (e.g., `AUTO-DZ-ACT-a3c5f1e2`)
4. **Sequential**: `{method}-{sequence}` (e.g., `AUTO-DZ-ACT-001`)

**Requirements**:
- Unique across all snapshots
- Human-readable
- No special characters (use `-` or `_` only)
- Lowercase preferred

---

## Snapshot Creation Workflow

### Standard Workflow

```
1. Prepare artifact files
   ↓
2. Compute SHA-256 hash for each file
   ↓
3. Generate manifest.json with metadata
   ↓
4. Compute manifest hash
   ↓
5. Create timestamp (ISO 8601 UTC)
   ↓
6. Package as immutable snapshot
   ↓
7. Store in read-only location
   ↓
8. Create git tag (if using git)
   ↓
9. Submit for governance review
```

### Pre-Submission Checklist

Before submitting snapshot for DOI review:

- [ ] All files are finalized (no further edits)
- [ ] SHA-256 hashes computed for all files
- [ ] Manifest created with all required fields
- [ ] Manifest hash computed and recorded
- [ ] Timestamp in ISO 8601 UTC format
- [ ] Snapshot ID is unique
- [ ] Metadata complete (no placeholders)
- [ ] Provenance information accurate
- [ ] Snapshot stored in read-only mode
- [ ] Git tag created (if applicable)
- [ ] No deprecated terminology in any file
- [ ] Compliance with all governance rules

**All checks must pass before submission**

---

## Snapshot Verification Procedure

### Independent Verification

Any party must be able to verify snapshot integrity:

#### Step 1: Obtain Manifest

Acquire the `manifest.json` file from trusted source.

#### Step 2: Verify Manifest Integrity

```bash
# Compute hash of manifest (excluding manifest_hash field)
# Compare with recorded manifest_hash
```

#### Step 3: Obtain Snapshot Files

Acquire all files listed in manifest.

#### Step 4: Verify File Hashes

```bash
# For each file in manifest:
sha256sum <file_path>
# Compare output with hash in manifest
```

#### Step 5: Verify Completeness

- Check all files in manifest are present
- Check no extra files are present
- Verify file sizes match manifest

#### Step 6: Report Results

- **Pass**: All hashes match, all files present, manifest verified
- **Fail**: Any mismatch, missing file, extra file, or manifest error

### Automated Verification

A verification script should:

```python
# Example verification logic (pseudocode)

def verify_snapshot(manifest_path, snapshot_dir):
    # 1. Load manifest
    manifest = load_json(manifest_path)
    
    # 2. Verify manifest schema
    validate_schema(manifest)
    
    # 3. Verify each file
    for file_entry in manifest['files']:
        path = file_entry['path']
        expected_hash = file_entry['hash']
        
        # Compute actual hash
        actual_hash = sha256(snapshot_dir + path)
        
        # Compare
        if actual_hash != expected_hash:
            return FAIL
    
    # 4. Verify no extra files
    actual_files = list_files(snapshot_dir)
    manifest_files = [f['path'] for f in manifest['files']]
    
    if actual_files != manifest_files:
        return FAIL
    
    # 5. All checks passed
    return PASS
```

---

## Snapshot Storage

### Storage Requirements

Snapshots must be stored in a manner that ensures:

1. **Immutability**: Read-only access, no modifications
2. **Integrity**: Hash verification remains possible
3. **Availability**: Accessible for verification and citation
4. **Durability**: Protected against data loss

### Acceptable Storage Locations

- **Git tags**: Immutable references (no force-push allowed)
- **Archive repositories**: Zenodo, Figshare, etc. (after approval)
- **Read-only filesystems**: Mounted read-only or WORM storage
- **Blockchain references**: Hash anchoring (optional, supplementary)

### Unacceptable Storage Locations

- **Mutable branches**: Can be force-pushed or modified
- **Temporary directories**: Not durable
- **Writable filesystems**: Modifications possible
- **Unverified cloud storage**: No integrity guarantees

---

## Snapshot Lifecycle

### States

A snapshot progresses through defined states:

1. **Draft**: Being prepared, not yet frozen
2. **Frozen**: Immutable, hash-verified, ready for review
3. **Submitted**: Under governance review
4. **Approved**: DOI issued, published
5. **Rejected**: Review failed, resubmission needed
6. **Archived**: Long-term preservation (post-approval)

### State Transitions

```
Draft → Frozen → Submitted → Approved → Archived
                      ↓
                   Rejected → (new Draft)
```

### State Requirements

#### Draft
- Modifiable (not yet a snapshot)
- No hash verification required
- No governance review

#### Frozen
- Immutable (snapshot created)
- All hashes computed
- Manifest complete
- Ready for submission

#### Submitted
- Under governance review
- No modifications permitted
- Awaiting approval or rejection

#### Approved
- DOI issued
- Permanent archival required
- Public citation permitted

#### Rejected
- Review failed
- Reason documented
- New snapshot required for resubmission

---

## Compliance and Enforcement

### Compliance Checklist

To verify snapshot contract compliance:

- [ ] All files have SHA-256 (or stronger) hashes
- [ ] Manifest includes all required fields
- [ ] Timestamp in ISO 8601 UTC format
- [ ] Version follows semantic versioning
- [ ] Snapshot ID is unique
- [ ] No post-freeze modifications
- [ ] Hash verification passes
- [ ] Metadata complete (no placeholders)
- [ ] Stored in read-only location
- [ ] Independently verifiable

### Enforcement

This contract is enforced by:

1. **Pre-submission verification**: Automated checks before review
2. **Governance review**: Human verification during approval
3. **Rejection on violation**: Non-compliant snapshots rejected
4. **Documentation**: Compliance logged in governance records

### Violations

Contract violations result in:

- **Snapshot invalidation**: Non-compliant snapshot rejected
- **Resubmission required**: New snapshot must be created
- **Approval denial**: DOI not issued
- **Audit trail**: Violation documented

---

## Related Documents

- `governance/DOI_ISSUANCE_POLICY.md` — DOI governance framework
- `governance/METHOD_REFERENCE_RULES.md` — Method citation rules
- `governance/FREEZE.md` — Scientific authorization status
- `PUBLICATION_POLICY.md` — Website publication rules

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-21 | Initial Snapshot Contract (Phase-F) |

---

**Effective Immediately**  
**Authority**: TRIZEL Layer-0 Governance  
**Status**: Active
