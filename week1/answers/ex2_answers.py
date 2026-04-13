"""
Exercise 2 — Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

# ── Task A ─────────────────────────────────────────────────────────────────

# List of tool names called during Task A, in order of first appearance.
# Look at [TOOL_CALL] lines in your terminal output.
# Example: ["check_pub_availability", "get_edinburgh_weather"]

TASK_A_TOOLS_CALLED = ["check_pub_availability","get_edinburgh_weather", "generate_event_flyer"]

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 5600.0

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = True

TASK_A_NOTES = ( "The agent checked both venues in parallel in a single turn rather than "
    "sequentially, which was unexpected. Both The Albanach and The Haymarket Vaults "
    "passed all constraints, so the agent defaulted to The Albanach as it appeared "
    "first. The flyer generation failed as expected due to the stub TODO. "
    "The <think> blocks were empty after adding the system prompt, confirming the "
    "prompt successfully suppressed Qwen3's extended reasoning mode.")  # optional — anything unexpected

# ── Task B ─────────────────────────────────────────────────────────────────

# Has generate_event_flyer been implemented (not just the stub)?
TASK_B_IMPLEMENTED = False   # True or False

# The image URL returned (or the error message if still a stub).
TASK_B_IMAGE_URL_OR_ERROR = "STUB — see TODO in sovereign_agent/tools/venue_tools.py"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "Professional event flyer for Edinburgh AI Meetup, tech professionals, modern venue at The Haymarket Vaults, Edinburgh. 160 guests."

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
Okay, let's see. The user wanted to check The Bow Bar for 160 vegan guests. The response says the capacity is 80, which is less than 160. So it doesn't meet the capacity requirement. The vegan option is available, but since the capacity is insufficient, the overall status is "full" and meets_all_constraints is false.
Now, the user asked to check other venues if The Bow Bar doesn't work. The next step is to check another pub. The known venues are The Albanach, The Haymarket Vaults, The G...

"""

SCENARIO_1_FALLBACK_VENUE = "The Haymarket Vaults"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False   # True or False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
Okay, let me go through the user's request again. They need a venue in Edinburgh for 300 people with vegan options. The known venues are The Albanach, The Haymarket Vaults, The Guilford Arms, and The Bow Bar. I checked all four.

The Albanach has a capacity of 180, which is under 300. Haymarket Vaults is 160, also too small. Guilford Arms can hold 200, still not enough. Bow Bar has 80, which is even smaller. None of them meet the 300-person requirement. Plus, even though some have vegan ...       
"""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = False   # True or False

SCENARIO_3_RESPONSE = """Since there's no function for train times, I can't use any of the provided tools to answer this. I need to inform t...
So to summarise theres's no available tools relevant to the training process for the request being given
"""

# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
Yes, the agent recognised the limtation of it's tool set and refused to answer the question as opposed
to hallucinating a train time or attempting to misuse an unrelated tool.
This acts like a prod-level agent as it acknowledged when a request felll outside it's scope. As making 
"""

# ── Task D ─────────────────────────────────────────────────────────────────

# Paste the Mermaid output from `python exercise2_langgraph.py task_d` here.
TASK_D_MERMAID_OUTPUT = """
---
config:
  flowchart:
    curve: linear
---
graph TD;
        __start__([<p>__start__</p>]):::first
        agent(agent)
        tools(tools)
        __end__([<p>__end__</p>]):::last
        __start__ --> agent;
        agent -.-> __end__;
        agent -.-> tools;
        tools --> agent;
        classDef default fill:#f2f0ff,line-height:1.2
        classDef first fill-opacity:0
        classDef last fill:#bfb6fc
"""

# Compare the LangGraph graph to exercise3_rasa/data/rules.yml. Min 30 words.
TASK_D_COMPARISON = """

LangGraph
----------
__start__ → agent ⇢ tools → agent ⇢ __end__
It decides things at runtime -> the thinking -> which tool to choose -> when to stop -> Are the order to do things
You can't read the graph to an get an insight on what is going on
Thus quite unpredictable, though I do see flexibility in the design

flows.yaml (RASA Calm)
----------------------

confirm_booking → collect guest_count → collect vegan_count 
               → collect deposit → action_validate_booking

handle_out_of_scope → utter_out_of_scope

- Every possible path is written down in advance
- The LLM only makes one decision — which flow to trigger
- After that, Rasa executes steps deterministically in order
- It's Readable, auditable, predictable
"""

# ── Reflection ─────────────────────────────────────────────────────────────

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
The agent checked both venues in parallel in a single turn rather than
sequentially, which was unexpected. Both The Albanach and The Haymarket Vaults
passed all constraints, so the agent defaulted to The Albanach as it appeared first.
The task implied a conditional logic: 'check The Albanach, and if it works use that one.' 
A sequential approach would have been the expected pattern, stopping at the 
first passing venue. 
Instead the agent batched both calls together, which is 
actually more efficient but not the behaviour most developers would anticipate 
when creating the prompt.
"""
