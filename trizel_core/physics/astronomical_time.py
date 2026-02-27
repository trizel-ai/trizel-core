"""
Canonical Solar–Lunar Year Ratio — TRZ-PHY-ASTR-001

Derived constant from declared inputs; not an absolute physical constant.
Any change in inputs requires recomputation and version bump.

Engineering note: calculators or naive implementations may show values near 1.01
or 1.03 due to wrong input definitions (e.g. sidereal vs. tropical year, or a
single synodic month rather than 12) or intermediate float rounding. This module
uses Python Decimal with explicit string literals as the single source of truth,
ensuring reproducible results across all runs and platforms.

Const ID: TRZ-PHY-ASTR-001
"""

from decimal import Decimal

# ── Input constants (declared as Decimal strings; do NOT change without a version bump) ──

Y_SOLAR_TT_DAYS = Decimal("365.24219")
"""TT tropical year expressed in days."""

Y_LUNAR_12_SYNODIC_DAYS = Decimal("354.367066")
"""12 synodic months expressed in days."""

# ── Derived quantity (dimensionless) ──

TRIZEL_PHY_ASTR_RATIO_DECIMAL = Y_SOLAR_TT_DAYS / Y_LUNAR_12_SYNODIC_DAYS
"""
Solar–Lunar year ratio: TT tropical year / 12 synodic months.
Computed deterministically from Decimal inputs; no floats involved.
"""

# ── Approved rational forms (p/q pairs; constants only — not computed here) ──

TRIZEL_PHY_ASTR_RATIO_RATIONAL_FAST = (403, 391)
"""Fast rational approximation of the Solar–Lunar ratio (lower precision)."""

TRIZEL_PHY_ASTR_RATIO_RATIONAL_STABLE = (3157, 3063)
"""Stable rational approximation of the Solar–Lunar ratio (higher precision)."""


def ratio_from_rational(p: int, q: int) -> Decimal:
    """Return *p/q* as a :class:`~decimal.Decimal`, using no floats.

    Parameters
    ----------
    p:
        Numerator of the rational approximation.
    q:
        Denominator of the rational approximation.  Must be non-zero.

    Returns
    -------
    Decimal
        The exact rational value ``p / q`` computed with Decimal arithmetic.
    """
    if q == 0:
        raise ValueError("Denominator q must be non-zero.")
    return Decimal(p) / Decimal(q)
