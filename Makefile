# Convenience only. Everything also works without make: python scripts/verify.py
.PHONY: setup verify scan
setup:
	python3 -m venv .venv && .venv/bin/python -m pip install -e ".[dev]" && git config core.hooksPath .githooks
verify:
	.venv/bin/python scripts/verify.py
scan:
	.venv/bin/python scripts/scan_sensitive.py --all
