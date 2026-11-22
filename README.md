# Agentic SDLC demo: a (fictional) garage door configurator

Hands-on material for the workshop **AI in Software Development** (pixelzunder for Novoferm).
A small Python project with a complete *project harness* - rules, context, gates - and eight
short exercises that show how to work with coding agents reliably.

> **Everything here is invented.** Rules, limits, prices, names, numbers and keys are workshop
> material and have nothing to do with real Novoferm products or customers.

The exercises follow the book *Building the Agentic Software Factory* by Alex Merced and
Benedikt Stemmildt (Packt, 2026). They are tool-agnostic: use GitHub Copilot, Claude Code,
Cursor, a local model - whatever you have. Where a prompt is given, copy it as it is.

## Setup (3 minutes)

You need Python 3.10 or newer and Git.

```
python -m venv .venv
.venv/bin/python -m pip install -e ".[dev]"      # Windows: .venv\Scripts\python -m pip install -e ".[dev]"
git config core.hooksPath .githooks
```

Activate the environment (`source .venv/bin/activate`, Windows: `.venv\Scripts\activate`), then:

```
python scripts/verify.py                          # all gates: lint, types, tests, coverage
python -m doorcfg --width 2500 --height 2125 --surface smooth --drive standard
```

Both must work before you start an exercise.

## Exercises

Each exercise stands alone and starts from a green repository. Reset between exercises with
`git restore . && git clean -fd` (this discards your changes).

| # | Exercise | Time | Agent needed | You take home |
|---|---|---|---|---|
| 01 | [Context experiment: same prompt, without and with an ADR](exercises/01-context-adr/README.md) | 10 min | yes | ADR in four parts, a rule as a script |
| 02 | [From a vague wish to a specification](exercises/02-spec/README.md) | 15 min | optional | intent card template |
| 03 | [AI-TDD: you own the tests](exercises/03-ai-tdd/README.md) | 15 min | yes | three prompts for red, green, refactor |
| 04 | [On the loop: one prompt, the gates decide](exercises/04-harness/README.md) | 15 min | yes | `AGENTS.md` pattern, one verify command |
| 05 | [A gate beats a policy](exercises/05-coverage-gate/README.md) | 15 min | yes | coverage threshold, versioned hook |
| 06 | [A gate for secrets and personal data](exercises/06-pii-gate/README.md) | 10 min | no | scanner and hook |
| 07 | [The pull request that carries its intent](exercises/07-pr-template/README.md) | 10 min | no | pull request template |
| 08 | [How long is the leash?](exercises/08-elastic-loop/README.md) | 10 min | no | Elastic Loop worksheet, red zones |

Short on time? Do **06** (always works, no agent) and **04** (the core idea).
Sample solutions are in `solutions/`; `python scripts/apply_solution.py 03` (or `04`, `05`)
copies one into the working tree.

## What is in the repository

```
AGENTS.md                 rules every agent reads first
docs/architecture.md      context map: modules, data flow, boundaries
docs/adr/                 decisions (ADR-001 money in cents, ADR-002 rules are data)
specs/                    input schema, intent card template
data/rules.json           the rule set: ranges, allowed values, prices
src/doorcfg/              models, rules, pricing, cli
tests/                    the gate - 100 % coverage
scripts/verify.py         one command for all gates
scripts/scan_sensitive.py blocks secrets and personal data
.githooks/pre-commit      runs both before every commit
.github/, azure-pipelines.yml   the same gates on the server, pull request template
exercises/, solutions/    the eight exercises
```

## The idea in one paragraph

An agent is a program that runs a model in a loop. It converges on the checks you give it -
not on correctness. So the work moves from writing code to building the environment: what the
agent **knows** (rules, context), what it can **do** (tools), and what **verifies** its work
(hooks, gates). When a run goes wrong, fix the environment, not only the code.

## Licence and sources

Workshop material by pixelzunder. Exercise ideas adapted from the walkthroughs in
*Building the Agentic Software Factory* (Merced, Stemmildt; Packt 2026) and its companion
repository (MIT): https://github.com/PacktPublishing/Building-the-Agentic-Software-Factory
