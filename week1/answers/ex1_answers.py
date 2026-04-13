"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True   # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
Uses a strong Llama-3.3-70B model to test the dataset across 3 formats.
Successfully isolates the correct answers The Albanach and the Haymarket Stalls
All 3 formats passed the test indicating that signal-to-noise ratio is too high for the differing formats to cause an issue processing them. 
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
Holyrood Arms - Because it satisfies two out of 
three constraints:
It has capacity of exactly 160 and offers vegan options 
But fails only on status being 'full'. 
A model that skims the data rather than carefully 
evaluating all three constraints simultaneously is highly likely to pick this venue, 
since it appears immediately before the correct answer and looks almost identical to the actual answer
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True   # True or False

PART_C_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
Smaller models (meta-llama/Meta-Llama-3.1-8B-Instruct) work less effcetively compared
to larger models like  meta-llama/Llama-3.3-70B-Instruct models.
Larger models leverage format cues (XML/sandwich) to jump to the strongest answer
Smaller models tend to process more mechanically and linearly, ignoring the structural advantages those formats are supposed to provide
What this looks like in real life:
The 70B model is powerful enough to recognise The Albanach at the top of the list and confidently return it, especially with XML/sandwich formats that boost primacy attention.
The 8B model lacks that capacity. Instead of evaluating the full list and picking the most prominent valid answer, it appears to scan linearly through all constraints and settle 
on the first venue it can fully verify by the time it reaches the end of the list.
Which ends up being The Haymarket Vaults.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Context formatting matters most when the signal-to-noise ratio is low.
Especially when prompts contain values such as near-miss distractors, long lists of similar items, or ambiguous 
data that requires evaluating multiple constraints simultaneously. 
Smaller models are significantly more affected by poor formatting than larger models, 
which have the ability to brute-force correct answers even from unstructured plain text. 
However, as datasets grow larger and tasks become more complex, even powerful models begin to degrade without clear 
signals like XML tags or sandwich-style query repetition to anchor their attention 
to the correct criteria via strong signals throughout the entiierity of the context window.
"""
