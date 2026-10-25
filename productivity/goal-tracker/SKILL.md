---
name: "goal-tracker"
description: "Goal check-in method: turn a goal into milestones, measure progress from evidence (never intentions), and report next actions on a schedule. Plugs into the existing goals system (user_goal namespace, workspace/goals/<slug>/GOAL.md). Tracking is automatic; commitments, purchases, and messages need approval."
---

# Goal Tracker — evidence-based goal check-ins

Adapted from the awesome-muse-connectors Goal Tracker template (MIT), fitted to
this environment's goal workspaces and tracked items.

## When to use

- A user goal needs steady progress without noisy reminders.
- Scheduled check-ins (weekly goal review) or on-demand progress reports.

## Method

1. **Define the goal sharply.** Outcome, definition of done, target date (or none),
   constraints (time, money, health, people). Ask the user for: the smallest
   meaningful milestone, how progress is measured, what counts as a setback,
   and what the tracker must never do.
2. **Convert to milestones + next actions** that fit the real calendar. Keep a
   short decision log in the goal's `GOAL.md` so plan changes are explainable.
3. **Measure from evidence only.** Use connected notes, calendar events,
   completed tasks, and workspace files. Never claim progress from an intention
   alone. If evidence is missing, say so.
4. **Report on schedule** (per goal, weekly by default):
   - progress since the previous check-in;
   - the next one to three actions;
   - blockers and decisions needed;
   - whether the target date still looks realistic;
   - one adjustment that would make progress easier.
5. **Approval boundary.** If the plan requires buying something, contacting
   someone, or changing a commitment, prepare the option but ask before acting.
   Pause the plan if the user says the goal is no longer active.

## Operating rules

- Goal state lives in `workspace/goals/<goal-slug>/GOAL.md` and the user_goal
  namespace — this skill is the method, not a second source of truth.
- Keep reminders proportional: check-ins on schedule, never nagging or shaming.
- User-facing check-ins are concise Korean, numbers and evidence first.

## First supervised run

Take one goal, one available hour this week, and one constraint. Produce a
milestone plan without connecting any external apps.
