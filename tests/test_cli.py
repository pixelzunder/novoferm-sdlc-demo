import json

import pytest

from doorcfg.cli import main


def test_cli_prints_price_for_valid_door(capsys: pytest.CaptureFixture[str]) -> None:
    exit_code = main(
        ["--width", "2500", "--height", "2125", "--surface", "smooth", "--drive", "standard"]
    )
    result = json.loads(capsys.readouterr().out)
    assert exit_code == 0
    assert result == {"valid": True, "violations": [], "net_price_cents": 94_400}


def test_cli_reports_violations(capsys: pytest.CaptureFixture[str]) -> None:
    exit_code = main(
        ["--width", "2500", "--height", "2125", "--surface", "smooth", "--option", "smart_control"]
    )
    result = json.loads(capsys.readouterr().out)
    assert exit_code == 1
    assert result["valid"] is False
    assert result["net_price_cents"] is None
    assert [violation["code"] for violation in result["violations"]] == ["OPTION_REQUIRES_DRIVE"]
