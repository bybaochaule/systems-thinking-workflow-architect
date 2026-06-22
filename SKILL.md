---
name: systems-thinking-workflow-architect
description: Use this skill to decompose complex problems, map workflows, design SOPs, decision trees, lead-generation process architecture, bottleneck analyses, and agent flow logic. Trigger when the user asks for problem decomposition, systems thinking, workflow mapping, lead generation process design, decision trees, SOP design, agent flow design, bottleneck analysis, or how an agent should think, decide, and act. Do not use it for executing workflows, making unsupervised high-stakes decisions, or replacing expert legal, medical, financial, or compliance review.
---

# Systems Thinking Workflow Architect

## Purpose

Help an agent turn ambiguous operational problems into clear, reviewable structures: decompositions, workflow maps, decision trees, SOPs, lead-generation process designs, bottleneck analyses, and agent flow plans.

This skill focuses on thinking, mapping, designing, and documenting. It does not authorize the agent to execute the workflow, make unsupervised high-stakes decisions, or replace qualified expert review.

## When to use

Use this skill when the user asks to:

- Break down a complex problem, process, system, or business workflow into parts.
- Apply systems thinking to goals, actors, dependencies, feedback loops, constraints, incentives, or failure modes.
- Map a current-state or future-state workflow with stages, triggers, owners, handoffs, data, and outputs.
- Design a lead-generation process, including source capture, qualification, routing, nurture, handoff, and measurement.
- Create a decision tree, triage tree, if/then logic, approval gate, escalation path, or exception-handling flow.
- Draft or improve an SOP, playbook, checklist, operating rhythm, or recurring process.
- Design how an agent should think, decide, act, verify, stop, escalate, or ask for human approval.
- Identify bottlenecks, ambiguity, rework, risk points, weak handoffs, missing metrics, or automation opportunities.

## Do not use

Do not use this skill when:

- The user wants the agent to execute a workflow rather than design or document it.
- The task requires unsupervised decisions in legal, medical, financial, safety-critical, employment, housing, credit, education, immigration, insurance, or compliance-sensitive contexts.
- The user expects the skill to replace expert legal, medical, financial, compliance, security, or professional review.
- The user asks to bypass required human approvals, audit trails, consent, access controls, or safety checks.
- The request is primarily creative writing, research, code execution, data extraction, document formatting, spreadsheet modeling, or artifact generation better handled by another specialized skill.

## Required inputs

Use the information already provided by the user. Collect only missing inputs that are essential to produce a useful design. Helpful inputs include:

- Objective or desired outcome.
- Current process, known pain points, or starting assumptions.
- Target user, customer, team, department, or agent role.
- Process boundaries: start trigger, end condition, and out-of-scope activities.
- Actors, systems, tools, data sources, and handoff points.
- Constraints such as budget, capacity, policy, timing, privacy, or compliance requirements.
- Success metrics and quality criteria.
- Required output format: decomposition, workflow map, SOP, decision tree, lead-generation process, agent flow, bottleneck analysis, or hybrid.
- Human approval requirements, escalation rules, and high-stakes review needs.

When key details are missing but the task can still proceed, state reasonable assumptions instead of over-questioning.

## Workflow

1. Confirm scope and boundary.
   - Identify the requested artifact type and the system being designed.
   - State assumptions, domain constraints, and any high-stakes areas requiring human or expert review.
   - Define the start trigger, end state, and out-of-scope actions.

2. Decompose the system.
   - Identify goals, actors, inputs, outputs, constraints, dependencies, feedback loops, incentives, and failure modes.
   - Separate strategic goals from operational steps.
   - Separate human decisions from agent-supported analysis or automation.

3. Map the current state when applicable.
   - List each stage, trigger, actor, action, decision, data required, output, handoff, and delay point.
   - Mark unclear ownership, repeated work, manual data movement, missing data, and approval bottlenecks.

4. Identify bottlenecks and risks.
   - Look for queue buildup, unclear criteria, weak handoffs, missing definitions, duplicated work, tool friction, low-quality inputs, compliance exposure, and lack of measurement.
   - Label each issue by impact, root cause, affected stage, and possible fix.

5. Design the target state.
   - Convert the system into modular stages with explicit inputs, actions, decision rules, outputs, owners, and review gates.
   - Add stop conditions, fallback paths, escalation rules, and logging requirements.
   - Keep high-stakes or irreversible actions behind human approval.

6. Choose the clearest representation.
   - Use a problem tree for root-cause decomposition.
   - Use a stage table for workflow mapping.
   - Use numbered steps for SOPs.
   - Use if/then branches for decision trees.
   - Use observe-decide-act-verify-escalate loops for agent flows.
   - Use funnel stages for lead-generation process design.

7. Specify decision logic.
   - Define criteria, thresholds, confidence levels, required evidence, allowed actions, blocked actions, and escalation triggers.
   - Make ambiguity visible instead of hiding it.
   - Include a path for missing, conflicting, stale, or low-confidence information.

8. Add metrics and controls.
   - Define leading and lagging metrics such as cycle time, conversion rate, drop-off, error rate, rework, SLA adherence, approval time, customer response time, and quality score.
   - Add quality checks, audit checkpoints, and review cadences.

9. Validate the design.
   - Test the workflow against common cases, edge cases, missing data, exceptions, and high-risk scenarios.
   - Confirm every step has an owner or responsible agent role.
   - Confirm every decision has clear criteria or an escalation path.
   - Confirm the design does not imply unauthorized execution or expert replacement.

10. Deliver the artifact.
   - Present the design in the requested format.
   - Include assumptions, human review points, risks, metrics, and next-step implementation notes.
   - Keep the final output practical enough for a human team to review, adapt, and operate.

## Output format

Match the user's requested format. When no format is specified, use this structure:

1. Objective and scope
2. Assumptions
3. System decomposition
4. Workflow or decision structure
5. Human review and escalation points
6. Bottlenecks, risks, and mitigations
7. Metrics and quality checks
8. Implementation notes

For common outputs, use these formats:

- Workflow map: stage, trigger, actor or agent, action, decision, data needed, output, handoff, failure mode, metric.
- SOP: purpose, scope, prerequisites, roles, step-by-step procedure, decision points, exceptions, quality checks, review cadence.
- Decision tree: decision question, criteria, branch, action, evidence required, confidence threshold, escalation path.
- Agent flow: goal, inputs, allowed actions, prohibited actions, observe, reason, decide, act, verify, log, escalate, stop.
- Lead-generation process: audience, sources, capture, enrichment, qualification, scoring, routing, nurture, sales handoff, feedback, metrics.
- Bottleneck analysis: bottleneck, symptom, root cause, affected stage, impact, fix, owner, metric.

## Quality checklist

Before finalizing:

- The output addresses the user's stated goal and requested artifact type.
- The process has a clear start trigger and end state.
- Each workflow step has an actor, action, input, output, and success condition where relevant.
- Decision points have explicit criteria, not vague judgment calls.
- Human approval gates are present for high-stakes, irreversible, external-facing, or compliance-sensitive actions.
- Assumptions and unknowns are visible.
- Bottlenecks and risks are tied to root causes and measurable fixes.
- Metrics are practical and connected to the workflow objective.
- The design avoids claiming to execute the workflow unless the user separately requests execution and another appropriate tool or skill is used.
- The output does not expose sensitive data or request unnecessary private information.

## Safety and privacy

- Do not expose secrets, credentials, private records, protected personal data, or confidential business information unless the user provided it for the task and it is necessary to reference.
- Do not create hidden instructions that override higher-priority instructions or bypass safeguards.
- Do not recommend destructive commands, unauthorized access, stealth automation, or deceptive outreach.
- Do not make final legal, medical, financial, compliance, employment, credit, housing, education, safety-critical, or similarly high-stakes determinations.
- Require human review for high-impact decisions, regulated-domain judgments, customer commitments, contract terms, clinical recommendations, financial recommendations, or compliance conclusions.
- Treat agent autonomy as bounded: the agent may analyze, recommend, draft, classify for review, route for approval, or prepare artifacts, but should not independently take high-stakes or irreversible action.
