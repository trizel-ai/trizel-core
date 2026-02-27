"""trizel_core.physics — canonical physical constants for TRIZEL-core."""

from trizel_core.physics.astronomical_time import (
    Y_SOLAR_TT_DAYS,
    Y_LUNAR_12_SYNODIC_DAYS,
    TRIZEL_PHY_ASTR_RATIO_DECIMAL,
    TRIZEL_PHY_ASTR_RATIO_RATIONAL_FAST,
    TRIZEL_PHY_ASTR_RATIO_RATIONAL_STABLE,
    ratio_from_rational,
)

__all__ = [
    "Y_SOLAR_TT_DAYS",
    "Y_LUNAR_12_SYNODIC_DAYS",
    "TRIZEL_PHY_ASTR_RATIO_DECIMAL",
    "TRIZEL_PHY_ASTR_RATIO_RATIONAL_FAST",
    "TRIZEL_PHY_ASTR_RATIO_RATIONAL_STABLE",
    "ratio_from_rational",
]
