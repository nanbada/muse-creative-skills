---
name: "voice_dump_dispatch"
description: "Turn a rambling voice memo or multi-task message into a structured, parallel-executed dispatch. Use when the user sends a voice note or a single message containing 2+ distinct tasks, corrections, or questions. Parse into a numbered list, fan independent tasks out to parallel subagents, and return one compressed report."
---

# Voice-Dump Dispatch

Friction is input, not model quality. Accept a rambling dump, structure it,
run independent tasks in parallel, report once — compactly.

## Trigger

- Voice memo, dictated message, or a single text containing 2+ distinct
  tasks / corrections / questions ("이거 해주고, 저것도 확인해주고...").
- Single-task inputs use the normal flow.

## Workflow

1. **Structure.** Parse the dump into a numbered task list. Classify each:
   - (a) independent, reversible or prepare-only → may run immediately
   - (b) depends on another task's output → queue behind it
   - (c) external action with side effects (구매·충전·가입·발행·전송·삭제·권한 변경)
     → approval required; do groundwork only
2. **Confirm compactly.** One message: numbered tasks + class + what runs in
   parallel vs needs approval. User corrects by number. (Default: always
   confirm; skip only if the user later says so.)
3. **Dispatch.** Fan (a)-class tasks out to parallel subagents
   (worker/window pattern). Max 4 lanes by default. Track state per task;
   no cross-task chatter.
4. **Compressed report.** ONE message when done: per-task one-liner + result
   or file/link + what still needs the user's decision. No per-task flood.

## Hard boundaries

- Class (c) actions: always stop for approval. Never invent approval.
- 2FA/CAPTCHA: stop and report; never bypass.
- Money, publication, or third parties ambiguous → stop and ask.
- Voice input is evidence for THIS task only; do not persist memo contents
  to memory unless the user says so.

## Done when

- [ ] 2+ task dump acknowledged with a numbered structure within one turn
- [ ] independent tasks executed in parallel; results in one compressed message
- [ ] approval-gated items listed separately with groundwork done
- [ ] every numbered item gets a status (done / queued / needs you) — nothing
      silently dropped

## When unsure

Stop the dispatch and ask by number. Never silently skip an item.
