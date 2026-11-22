# Exercise 06 - A gate for secrets and personal data

**Time:** 10 minutes · **Book:** chapter 8, Security and Safety · **You need:** only Git and
Python - this exercise works without an agent and gives the same result every time

**What you will see:** an agent is a helpful colleague without suspicion. It copies what it
finds - a key from a settings file, a customer from an export - into code, logs and commits.
The gate does not rely on anyone noticing.

All names, numbers and keys in `seed/` are invented.

## Steps

1. Activate the versioned hook (once per clone): `git config core.hooksPath .githooks`

2. Simulate "I just need real data to test the import":

   ```
   cp -r exercises/06-pii-gate/seed customer-import
   git add customer-import
   git commit -m "Add customer import"
   ```

3. **The commit is rejected.** Read the report: nine findings in three files, each with file,
   line and kind, and the values redacted - a gate must not leak what it protects.

4. **Fix it** by hand or with your agent:

   > Run `python scripts/scan_sensitive.py customer-import/*` and fix every finding: read
   > secrets from environment variables, replace personal data with obviously synthetic data
   > (example.com addresses), write [REDACTED] in documents. Do not change the scanner.

5. `git add customer-import && git commit -m "Add customer import"` - now it passes.
   Clean up: `git reset --hard HEAD~1`

6. **Two minutes of discussion:** Which pattern is missing for *your* data (customer numbers,
   order numbers, internal host names)? Add it to `PATTERNS` in `scripts/scan_sensitive.py`.

## Take to your own repo

- `scripts/scan_sensitive.py` (about 100 lines, no dependencies) plus the hook - or a
  maintained tool such as gitleaks, trufflehog or detect-secrets for secrets.
- Run the same scan in CI with `--all`. The local hook can be skipped, the server check cannot.
- Decide as a team which directories never go into an agent's context (exports, dumps, `.env`).
- Sample result: `solutions/06-pii-gate/customer-import/`
