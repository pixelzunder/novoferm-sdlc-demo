from dataclasses import replace

from doorcfg.models import DoorConfiguration
from doorcfg.pricing import net_price_cents
from doorcfg.rules import RuleSet, validate

WICKET = frozenset({"wicket_door"})


def codes(config: DoorConfiguration, rules: RuleSet) -> list[str]:
    return [violation.code for violation in validate(config, rules)]


def test_wicket_door_is_valid_and_adds_its_price(
    base_config: DoorConfiguration, rules: RuleSet
) -> None:
    with_wicket = replace(base_config, options=WICKET)
    assert codes(with_wicket, rules) == []
    assert (
        net_price_cents(with_wicket, rules)
        == net_price_cents(base_config, rules) + rules.options["wicket_door"].price_cents
    )


def test_wicket_door_needs_a_minimum_width(base_config: DoorConfiguration, rules: RuleSet) -> None:
    too_narrow = rules.options["wicket_door"].min_width_mm - 1
    assert codes(replace(base_config, width_mm=too_narrow, options=WICKET), rules) == [
        "OPTION_TOO_NARROW"
    ]


def test_minimum_width_is_inclusive(base_config: DoorConfiguration, rules: RuleSet) -> None:
    exactly = rules.options["wicket_door"].min_width_mm
    assert codes(replace(base_config, width_mm=exactly, options=WICKET), rules) == []


def test_wicket_door_and_windows_exclude_each_other(
    base_config: DoorConfiguration, rules: RuleSet
) -> None:
    config = replace(base_config, options=frozenset({"wicket_door", "windows"}))
    assert codes(config, rules) == ["OPTIONS_INCOMPATIBLE"]
