from dataclasses import replace

import pytest

from doorcfg.models import DoorConfiguration
from doorcfg.pricing import InvalidConfigurationError, divide_half_up, net_price_cents
from doorcfg.rules import RuleSet


def test_divide_half_up() -> None:
    assert divide_half_up(5, 10) == 1
    assert divide_half_up(4, 10) == 0
    assert divide_half_up(15, 10) == 2


def test_net_price_of_base_configuration(base_config: DoorConfiguration, rules: RuleSet) -> None:
    # 2.5 m x 2.125 m = 5.3125 m2 x 112.00 EUR = 595.00 EUR, plus standard drive 349.00 EUR
    assert net_price_cents(base_config, rules) == 59_500 + 34_900


def test_options_are_added(base_config: DoorConfiguration, rules: RuleSet) -> None:
    config = replace(base_config, options=frozenset({"windows", "smart_control"}))
    assert net_price_cents(config, rules) == 59_500 + 34_900 + 21_900 + 12_900


def test_price_is_always_an_integer(base_config: DoorConfiguration, rules: RuleSet) -> None:
    config = replace(base_config, width_mm=2333, height_mm=2001, surface="woodgrain")
    assert isinstance(net_price_cents(config, rules), int)


def test_invalid_configuration_has_no_price(base_config: DoorConfiguration, rules: RuleSet) -> None:
    with pytest.raises(InvalidConfigurationError) as error:
        net_price_cents(replace(base_config, width_mm=10), rules)
    assert [violation.code for violation in error.value.violations] == ["WIDTH_OUT_OF_RANGE"]
