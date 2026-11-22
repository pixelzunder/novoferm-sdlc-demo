import importlib.util
import sys
from pathlib import Path
from types import ModuleType

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "scan_sensitive.py"


@pytest.fixture(scope="module")
def scanner() -> ModuleType:
    spec = importlib.util.spec_from_file_location("scan_sensitive", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules["scan_sensitive"] = module
    spec.loader.exec_module(module)
    return module


def kinds(scanner: ModuleType, text: str) -> list[str]:
    return [finding.kind for finding in scanner.scan_text("file.txt", text)]


def test_finds_api_key_and_redacts_it(scanner: ModuleType) -> None:
    key = "nvf_live_" + "A1b2C3d4" * 3
    findings = scanner.scan_text("config.py", f"KEY = {key}")
    assert [finding.kind for finding in findings] == ["API key"]
    assert key not in findings[0].excerpt


def test_finds_personal_data(scanner: ModuleType) -> None:
    assert kinds(scanner, "IBAN DE12 3456 7890 1234 5678 90") == ["IBAN"]
    assert kinds(scanner, "call +49 151 2345678") == ["phone number"]
    assert kinds(scanner, "mail erika.muster@some-company.de") == ["e-mail address"]


def test_synthetic_addresses_are_fine(scanner: ModuleType) -> None:
    assert kinds(scanner, "mail erika@example.com") == []


def test_hard_coded_credential(scanner: ModuleType) -> None:
    assert kinds(scanner, 'password = "hunter2hunter2"') == ["hard-coded credential"]
    assert kinds(scanner, 'DB_PASSWORD = "hunter2hunter2"') == ["hard-coded credential"]
    assert kinds(scanner, 'password = os.environ["DB_PASSWORD"]') == []


def test_exercise_seed_files_are_allowed(scanner: ModuleType) -> None:
    assert scanner.is_allowed("exercises/06-pii-gate/seed/customers.json")
    assert not scanner.is_allowed("src/doorcfg/cli.py")
