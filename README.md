# Systems Thinking Workflow Architect

## Overview

Systems Thinking Workflow Architect helps an agent decompose complex problems and design reviewable process artifacts such as workflow maps, SOPs, decision trees, lead-generation processes, bottleneck analyses, and agent flow plans.

The skill is intended for planning, reasoning, and documentation. It does not execute workflows, make unsupervised high-stakes decisions, or replace legal, medical, financial, compliance, or other expert review.

## When to use

Use this skill when a user asks for problem decomposition, systems thinking, workflow mapping, lead-generation process design, decision trees, SOP design, agent flow design, bottleneck analysis, or guidance on how an agent should think, decide, act, verify, and escalate.

## Contents

- `SKILL.md`: agent-facing instructions, triggers, boundaries, workflow, output formats, quality checklist, and safety rules.
- `README.md`: this human-readable overview.
- `agents/openai.yaml`: OpenAI display metadata, invocation policy, and dependencies.
- `references/style-guide.md`: reusable patterns, templates, examples, and edge cases for workflow and systems design outputs.
- `assets/`: reserved for reusable templates or visual assets.
- `scripts/example_helper.py`: a safe deterministic helper for checking whether a drafted process artifact includes recommended review sections.

## Usage examples

```text
Map our inbound lead qualification workflow and identify bottlenecks.
```

```text
Create a decision tree for routing support tickets to the right team, including escalation rules.
```

```text
Design an SOP for how an AI agent should handle customer intake, verify missing information, and stop for human approval.
```

```text
Decompose this operational problem using systems thinking and show the actors, feedback loops, constraints, and failure modes.
```

## Package structure

```text
systems-thinking-workflow-architect/
|-- SKILL.md
|-- README.md
|-- agents/
|   `-- openai.yaml
|-- assets/
|   `-- .gitkeep
|-- references/
|   `-- style-guide.md
`-- scripts/
    `-- example_helper.py
```

## Notes for maintainers

- Keep trigger language specific and operational.
- Keep execution boundaries explicit.
- Put long examples, templates, and edge cases in `references/style-guide.md` rather than overloading `SKILL.md`.
- Add reusable files to `assets/` only when they are safe to distribute.
- Keep scripts deterministic, non-destructive, and free of secrets.
