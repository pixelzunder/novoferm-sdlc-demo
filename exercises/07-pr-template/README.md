# Exercise 07 - The pull request that carries its intent

**Time:** 10 minutes · **Book:** chapter 9, The Team Operating Model · **No agent needed**

**What you will see:** when code is generated in minutes, review becomes the bottleneck. The
way out is not to read faster. The author proves more, the gates check the mechanics, and the
reviewer reads the few places where being wrong is expensive.

## Steps

1. Read `.github/PULL_REQUEST_TEMPLATE.md`. It has four parts: description, agentic generation
   context, verification and accountability, reviewer focus.

2. Take the change from exercise 03 or 04 (or apply a sample: `python scripts/apply_solution.py 04`)
   and fill in the template as if you opened the pull request. Time yourself: it should take
   three minutes. If it takes ten, the intent was not clear before the agent started.

3. Swap with your neighbour. Review **only** with the three reviewer questions - do not read
   the diff line by line. Did you find something? Would a line-by-line read have found more?

4. Adapt the template for your team, in pairs:
   - Which checkbox is missing for your product (migrations, translations, performance)?
   - Which paths must always be read by a human (money, permissions, data migrations)?
   - Which checkbox can be deleted because a gate already enforces it?

## The four team commitments behind the template

1. **Accountability** - the name on the commit owns the behaviour in production.
2. **Intent transparency** - the intent and the decisions travel with the change.
3. **Context boundaries** - the team has a written list of what never goes into an agent.
4. **Continuous education** - a regular slot to share the best intents and the worst failures.

## Take to your own repo

- The template (Azure DevOps: `.azuredevops/pull_request_template.md`,
  GitHub: `.github/PULL_REQUEST_TEMPLATE.md`).
- The rule: every reduction in reading follows a gate that earned it - never the other way round.
- Sample result: `solutions/07-pr-template/example-pr.md`
