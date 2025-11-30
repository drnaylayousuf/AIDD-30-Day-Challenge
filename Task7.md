# *Spec-Kit Plus Overview*

Spec-Kit Plus is an SDD-RI framework (Specification-Driven Development with Reusable Intelligence) built on a single core principle:

**“Capture intelligence, not just produce code.”**

In traditional development, code is treated as the primary deliverable even though it is temporary, tied to the current tech stack, and destined to be rewritten.
Spec-Kit Plus flips this model. Every feature you build produces two outputs:

### *1. Working Code (Temporary Output)*

This is the functional implementation delivered today.
It’s valuable in the short term but inherently disposable—tied to today’s tools, frameworks, and constraints.

### *2. Reusable Intelligence (Permanent Output)*

 This is the lasting asset:
* The reasoning
* The decision-making logic
* The prompt patterns
* The architectural thinking

This intelligence evolves over time, applies across projects, and forms a growing personal knowledge base.

Spec-Kit Plus is designed to work alongside modern AI development tools (Claude Code, Gemini CLI, Cursor, etc.). Its structured workflows activate the AI’s reasoning capabilities instead of treating it like a code-generator.

#
# *The 5 Core Concepts of Spec-Kit Plus*

Spec-Kit Plus is organized around five slash-commands.
Each represents a stage in the SDD-RI workflow and a different type of intelligence you are capturing


## **1. /Constitution – The Rulebook**
The Constitution is the project’s foundational rulebook.
It defines the non-negotiable quality standards that both you and the AI must follow at every step.

Running /sp.constitution generates constitution.md.
It becomes the guiding document that shapes every specification, plan, task, and implementation throughout the project.


## **2. /Specify – The Complete Specification**
This command creates a clear, testable, AI-aligned specification. A strong spec:
* States the intent and purpose of the feature
* Defines explicit constraints
* Provides measurable success criteria
* Aligns fully with the Constitution
  
In an AI-native workflow, writing great specs is more valuable than writing code.

## **3. /Plan – The Implementation Plan**
Once the specification is ready, the Plan phase answers:

**“How exactly will we build this?”**

/sp.plan analyzes the specification and produces a detailed plan, including:

* Component breakdown
* Dependency ordering
* Architecture suggestions
* Key design decisions

This transforms the specification into an actionable roadmap.


## **4. /Tasks – Atomic Work Units & Checkpoints**
/sp.tasks converts the plan into a structured task list.

Each task is:
* Atomic (15–30 minutes of work)
* Clear with one acceptance criterion
* Verifiable with a concrete output
  
The task list also includes checkpoints, giving you explicit control during execution.

Instead of writing tasks manually, Spec-Kit Plus generates them.
Your job is to validate the structure and approve them not to create them from scratch.


 ## **5. /Implement – Guided, Collaborative Execution**
Implementation is not autonomous.

It is a collaborative, checkpoint-driven workflow where:
* You choose direction
* The AI executes tasks
* The system verifies results against the spec

When you run /sp.implement:

1. It reads tasks.md
2. Executes tasks in dependency order
3. Pauses at each checkpoint
4. Waits for your approval before moving forward

You stay in control; the AI handles the heavy lifting.

#

# In Essence
Spec-Kit Plus turns development into a two-layer process:

***Temporary Layer: Code that solves today’s problem***

***Permanent Layer: Reusable intelligence that compounds over time***

By capturing the thinking, not just the output, Spec-Kit Plus transforms AI tools into long-term knowledge partners and turns your development process into
a continuously evolving system of intelligence.







