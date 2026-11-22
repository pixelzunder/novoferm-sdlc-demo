from dataclasses import replace

from doorcfg.models import DoorConfiguration
from doorcfg.rules import RuleSet, validate


def codes(config: DoorConfiguration, rules: RuleSet) -> list[str]:
    return [violation.code for violation in validate(config, rules)]


def test_valid_configuration_has_no_violations(
    base_config: DoorConfiguration, rules: RuleSet
) -> None:
    assert validate(base_config, rules) == []


def test_width_limits_are_inclusive(base_config: DoorConfiguration, rules: RuleSet) -> None:
    assert codes(replace(base_config, width_mm=rules.width_mm.min), rules) == []
    assert codes(replace(base_config, width_mm=rules.width_mm.min - 1), rules) == [
        "WIDTH_OUT_OF_RANGE"
    ]


def test_height_out_of_range(base_config: DoorConfiguration, rules: RuleSet) -> None:
    assert codes(replace(base_config, height_mm=rules.height_mm.max + 1), rules) == [
        "HEIGHT_OUT_OF_RANGE"
    ]


def test_unknown_surface_and_drive(base_config: DoorConfiguration, rules: RuleSet) -> None:
    config = replace(base_config, surface="glass", drive="hydraulic")
    assert codes(config, rules) == ["UNKNOWN_SURFACE", "UNKNOWN_DRIVE"]


def test_manual_drive_is_limited_by_width(base_config: DoorConfiguration, rules: RuleSet) -> None:
    limit = rules.drives["manual"].max_width_mm
    assert codes(replace(base_config, drive="manual", width_mm=limit), rules) == []
    assert codes(replace(base_config, drive="manual", width_mm=limit + 1), rules) == [
        "DRIVE_TOO_WEAK"
    ]


def test_widest_door_needs_power_drive(base_config: DoorConfiguration, rules: RuleSet) -> None:
    widest = replace(base_config, width_mm=rules.width_mm.max)
    assert codes(widest, rules) == ["DRIVE_TOO_WEAK"]
    assert codes(replace(widest, drive="power"), rules) == []


def test_smart_control_needs_a_motor(base_config: DoorConfiguration, rules: RuleSet) -> None:
    config = replace(base_config, drive="manual", options=frozenset({"smart_control"}))
    assert codes(config, rules) == ["OPTION_REQUIRES_DRIVE"]


def test_unknown_option(base_config: DoorConfiguration, rules: RuleSet) -> None:
    assert codes(replace(base_config, options=frozenset({"sunroof"})), rules) == ["UNKNOWN_OPTION"]
