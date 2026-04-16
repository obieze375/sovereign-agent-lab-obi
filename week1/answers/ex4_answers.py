"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ["search_venues",
    "get_venue_details"]

QUERY_1_VENUE_NAME    = "The Albanach"
QUERY_1_VENUE_ADDRESS = "2 Hunter Square, Edinburgh"
QUERY_2_FINAL_ANSWER  = "Okay, let me go through the user's query again. They wanted Edinburgh venues for 160 guests with vegan options and the full address of the best match.First, I used the search_venues function with min_capacity 160 and requires_vegan true. The initial error was because I didn't structure the arguments correctly. After fixing that, I got two venues: The Albanach and The Haymarket Vaults."

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True  # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
I changed the availabitly of the The Albanach from available to full and chnaged the final output to this 
Okay, the user is looking for Edinburgh venues that can accommodate 160 guests and have vegan options. They want the full address of the best match. Let me go through the steps again to see where things might be going wrong.
First, I called the search_venues function with min_capacity=160 and requires_vegan=true. The response came back with zero matches. That's unexpected. Maybe there are...
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 145 #count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 292 #count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
In Exercise 2, the tools are imported directly into the agent via from sovereign_agent.tools.venue_tools import check_pub_availability, ... etc. They are statically bound at import time, meaning any change requires restarting the agent process, and only Python/LangChain consumers can use them.
MCP buys you runtime discovery and protocol-level decoupling. In Exercise 4, discover_tools() connects to the server fresh each run and asks "what tools exist right now?", in short the agent never imports the tools directly. This means:
Any client can consume the same server — the Exercise 4 docstring explicitly calls this out: both a LangGraph agent and a Rasa action server can connect to mcp_venue_server.py simultaneously, without either knowing how the other works.
Changes propagate without touching agent code — swap a venue's status in mcp_venue_server.py, rerun the client, and the agent sees the updated data. 
Nothing in exercise4_mcp_client.py changes.
The tool boundary is a network contract, not a Python import — which means it's language-agnostic and composable across systems that can't share a codebase.
"""

# ── Week 5 architecture ────────────────────────────────────────────────────
# Describe your full sovereign agent at Week 5 scale.
# At least 5 bullet points. Each bullet must be a complete sentence
# naming a component and explaining why that component does that job.

WEEK_5_ARCHITECTURE = """
### Directory contents
There are 4 core scripts:
 
1. `sovereign_agent/agents/research_agent.py`
2. `sovereign_agent/tools/venue_tools.py`
3. `sovereign_agent/tools/mcp_venue_server.py`
4. `sovereign_agent/tests/test_week1.py`
 
---
 
### 1) `agents/research_agent.py` — main agent runtime (LangGraph ReAct loop)
 
This file is the orchestration layer (“agent brain”).
 
- Loads environment variables with `load_dotenv()`.
- Creates an LLM client (`ChatOpenAI`) against Nebius Token Factory:
  - `base_url = "https://api.tokenfactory.nebius.com/v1/"`
  - model from `RESEARCH_MODEL` (default: `Qwen/Qwen3-32B`)
- Registers four tools from `venue_tools.py`.
- Builds a ReAct agent once:
  - `_agent = create_react_agent(llm, TOOLS)`
 
#### Public API
```python
run_research_agent(task: str, max_turns: int = 8) -> dict
```

The Planner component breaks a user goal into ordered sub-tasks because high-level requests are too ambiguous for a single tool call and need explicit step sequencing.
The Research Executor component (LangGraph ReAct agent) handles iterative reasoning and tool use because it must adapt its next action based on live tool outputs instead of following a fixed script.
The Tooling Layer component (venue, weather, catering, flyer, file/search tools) performs external actions and data retrieval because the language model cannot directly access real-world systems on its own.
The Memory component stores prior decisions, constraints, and outcomes because the agent needs continuity across turns and sessions to avoid repeating work or contradicting earlier commitments.
The MCP Server component exposes reusable capabilities through a standard protocol because multiple clients (agent runtime, assistants, or other services) need a shared and discoverable tool interface.
The Handoff Bridge component routes conversation-centric tasks to the Rasa side because structured dialogue management and slot-driven confirmations are better handled by a dedicated conversational engine.
The Observability and Cost-Tracking component records traces, tool calls, and token usage because production agents need auditability, debugging visibility, and spend control.
The Safety and Guardrails component validates tool inputs/outputs and enforces policy checks because autonomous execution must prevent unsafe actions, hallucinated claims, and brittle failure behavior.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
Use LangGraph-style research agent for research tasks because research is open-ended, tool-heavy, and uncertain, so it benefits from iterative “think → call tools → revise” behavior.
Use the Rasa/CALM-style dialogue agent for call tasks because live calls need strict turn control, slot confirmation, predictable phrasing, and safe recovery paths under time pressure.
Swapping them feels wrong because their control models are opposite: the research agent is optimized for flexible exploration, while the call agent is optimized for deterministic conversation flow, so each performs poorly when forced into the other’s job.
"""
