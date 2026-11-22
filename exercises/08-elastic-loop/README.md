# Exercise 08 - How long is the leash? (paper exercise)

**Time:** 10 minutes · **Book:** chapter 7 (the Elastic Loop) and chapter 11 (Red Zones) ·
**You need:** five tickets from your own backlog, a pen

**What you will see:** autonomy is not a setting for the team. It is a decision per task, and
it depends on two things: what happens if it goes wrong, and how well your gates would notice.

## The matrix

|  | **Weak harness** - little context, few gates | **Strong harness** - rich context, strict gates |
|---|---|---|
| **High risk** - large blast radius | **Tight loop** - small steps, you read every line, you run the checks | **Guarded loop** - the agent builds the feature, you review the pull request after all gates are green |
| **Low risk** - isolated scope | **Loose loop** - quick prototypes, checked by hand, thrown away or reworked later | **No loop** - the agent works end to end, merge on green, you watch the numbers |

The rule behind it: *never give an agent more autonomy than your harness can verify.*

## Steps

1. Write five current tickets on the worksheet (`worksheet.md`) and place each in a quadrant.
   Note the reason in a few words.

2. For every ticket in the left column: what **one** thing (a test, a schema, an ADR, a rule
   in `AGENTS.md`) would move it to the right?

3. **Red zones.** List three or four operations that always need a human decision, no matter
   how green the gates are. Typical: database migrations in production, access to personal
   data, credentials, changes to an interface another team uses.

4. Compare in the group. Where do you disagree about a ticket? That disagreement is the
   interesting part - it usually means the risk or the gates are not written down.

## Take to your own repo

- Put the red zones into `AGENTS.md` ("stop and ask") **and** into the pipeline (required
  approval for those paths). Written down is good, enforced is better.
- Revisit the placement when a gate is added - or when a defect slips through. Loosening is
  not a one-way street.
