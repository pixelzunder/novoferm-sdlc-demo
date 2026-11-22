from dataclasses import replace

import pytest

from doorcfg.models import DoorConfiguration
from doorcfg.pricing import InvalidConfigurationError, net_price_cents
from doorcfg.quote import LineItem, build_quote
from doorcfg.rules import RuleSet


def test_quote_of_base_configuration(base_config: DoorConfiguration, rules: RuleSet) -> None:
    quote = build_quote(base_config, rules)
    assert quote.items == (
        LineItem("panel:smooth", 59_500),
        LineItem("drive:standard", 34_900),
    )
    assert quote.net_cents == 94_400
    assert quote.vat_cents == 17_936
    assert quote.gross_cents == 112_336


def test_manual_drive_is_listed_with_zero(base_config: DoorConfiguration, rules: RuleSet) -> None:
    quote = build_quote(replace(base_config, drive="manual"), rules)
    assert LineItem("drive:manual", 0) in quote.items


def test_options_follow_in_alphabetical_order(
    base_config: DoorConfiguration, rules: RuleSet
) -> None:
    config = replace(base_config, options=frozenset({"windows", "smart_control"}))
    labels = [item.label for item in build_quote(config, rules).items]
    assert labels == ["panel:smooth", "drive:standard", "option:smart_control", "option:windows"]


def test_net_matches_pricing_module(base_config: DoorConfiguration, rules: RuleSet) -> None:
    config = replace(base_config, surface="woodgrain", options=frozenset({"windows"}))
    quote = build_quote(config, rules)
    assert quote.net_cents == net_price_cents(config, rules)
    assert quote.net_cents == sum(item.amount_cents for item in quote.items)


def test_vat_rounds_half_up(base_config: DoorConfiguration, rules: RuleSet) -> None:
    # woodgrain: 52 063 + 34 900 = 86 963 cents; 50 % of that is 43 481.5 -> 43 482
    half_rate = replace(rules, vat_percent=50)
    quote = build_quote(replace(base_config, surface="woodgrain"), half_rate)
    assert quote.vat_cents == 43_482
    assert quote.gross_cents == quote.net_cents + quote.vat_cents


def test_invalid_configuration_has_no_quote(base_config: DoorConfiguration, rules: RuleSet) -> None:
    with pytest.raises(InvalidConfigurationError):
        build_quote(replace(base_config, height_mm=1), rules)
