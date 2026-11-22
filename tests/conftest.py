import pytest

from doorcfg.models import DoorConfiguration
from doorcfg.rules import RuleSet, load_rules


@pytest.fixture(scope="session")
def rules() -> RuleSet:
    return load_rules()


@pytest.fixture
def base_config() -> DoorConfiguration:
    """A small, valid door: 2500 x 2125 mm, smooth surface, standard drive."""
    return DoorConfiguration(width_mm=2500, height_mm=2125, surface="smooth", drive="standard")
