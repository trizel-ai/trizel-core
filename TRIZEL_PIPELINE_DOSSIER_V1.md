# TRIZEL PIPELINE DOSSIER V1

Status: CANONICAL GOVERNANCE ARTIFACT  
Layer: 0  
Purpose: Define the operational data pipeline governing ingestion, generation, validation, and presentation.

---

## 1. Scope

This document defines the TRIZEL operational pipeline across Layer-1 (generation) and Layer-2 (presentation interface).

It establishes non-negotiable rules for how observational data is:
- ingested
- transformed
- validated
- presented

---

## 2. Core Epistemic Principle

structure ≠ evidence

The existence of a record does not imply the existence of valid data.

All pipeline components must preserve this distinction.

---

## 3. Data Lifecycle

data ingestion → data generation → validation → publication

Flow:

data/ingestion/*.json
        ↓
scripts/build_observations.py
        ↓
public/*.json
        ↓
scripts/validate_pipeline.py

---

## 4. Generator Authority (Single Source of Truth)

scripts/build_observations.py is the only authority responsible for:

- computing observation status
- computing valid_record_count
- computing day_status
- producing final public JSON artifacts

No downstream component is allowed to modify generated data.

---

## 5. Validator Constraints (Read-Only Enforcement)

scripts/validate_pipeline.py:

- must operate as read-only
- must not modify any data
- must fail execution if inconsistencies are detected

Validation is enforcement, not correction.

---

## 6. Observation State Model

Each observation must be classified into one of the following states:

- ok            → valid, retrieved, verifiable data
- scheduled     → future observation
- not_released  → expected but not yet published
- unavailable   → anomaly or retrieval failure

No implicit states are allowed.

---

## 7. Presentation Rules (Layer-2)

The presentation layer must:

- display valid_record_count instead of total records
- explicitly expose observation status
- avoid any misleading aggregation

Warnings are allowed only for:
- unavailable

No warnings for:
- scheduled
- not_released

---

## 8. CI Guarantees

The CI system must enforce:

- deterministic pipeline execution
- validation failure on any inconsistency
- zero tolerance for malformed artifacts

All pipeline outputs must be reproducible.

---

## 9. Multilingual Constraints

Supported languages:

- EN
- AR
- FR
- ZH

Rules:

- SUPPORTED_LANGS must match defined translations
- no unsupported languages allowed
- RTL layout applies only to Arabic

---

## 10. Epistemic Guarantee

A record is considered valid data only if it is:

- retrieved (non-empty retrieval timestamp)
- timestamped (retrieved_utc defined)
- verifiable (source traceable)

Otherwise, it must not be treated as evidence.

---

## 11. Non-Activation Clause

This artifact:

- does not perform execution
- does not introduce analysis
- does not produce scientific conclusions
- does not activate Gate-6

It defines governance constraints only.

---

END OF DOSSIER
