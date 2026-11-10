"""
exercises.py - Week 01 practice

How to use this file:
  1. Read each exercise.
  2. Replace every `None` with your own code (look for the TODO comments).
  3. Run:  python exercises.py
  4. Each exercise prints ✅ (correct), ❌ (wrong) or ⬜ (not done yet).

Try every exercise before opening solutions.py. Getting stuck is part of learning.
"""


# -----------------------------------------------------------------------------
# Helper: checks your answer. You don't need to understand this yet; we cover
# functions in Week 03. All you need to know: check(label, your_answer, expected)
# -----------------------------------------------------------------------------
def check(label, got, expected):
    if got == expected:
        print(f"✅ {label}")
    elif got is None:
        print(f"⬜ {label}: not done yet")
    else:
        # {x!r} shows a value with quotes, so you can spot stray spaces
        print(f"❌ {label}: expected {expected!r} but got {got!r}")


# -----------------------------------------------------------------------------
# Exercise 1: Variables and types
# Create four variables that describe an LLM request.
# -----------------------------------------------------------------------------
model_name = None    # TODO: the text "example-model"
temperature = None   # TODO: the decimal number 0.3
max_tokens = None    # TODO: the whole number 256
stream = None        # TODO: the boolean True

check("1a model_name", model_name, "example-model")
check("1b temperature", temperature, 0.3)
check("1c max_tokens", max_tokens, 256)
check("1d stream", stream, True)


# -----------------------------------------------------------------------------
# Exercise 2: Type conversion
# A user typed "512" into a form. That is text, not a number.
# Convert it to an int and add 100 so you can set a bigger token limit.
# -----------------------------------------------------------------------------
user_typed = "512"
total_tokens = None  # TODO: convert user_typed to an int, then add 100

check("2 total_tokens", total_tokens, 612)


# -----------------------------------------------------------------------------
# Exercise 3: Clean messy user input
# Remove the extra spaces at the start, end AND between words, then make
# everything lowercase.
# Hint: " ".join(text.split()) tidies spaces; .lower() lowercases.
# -----------------------------------------------------------------------------
raw_message = "   WhAt Is   MaChiNe LeArNiNg?  "
cleaned = None  # TODO

check("3 cleaned", cleaned, "what is machine learning?")


# -----------------------------------------------------------------------------
# Exercise 4: Build a prompt with an f-string
# Produce exactly this two-line text (note the \n for the new line):
#   Answer in a formal tone.
#   Question: What is a token?
# -----------------------------------------------------------------------------
tone = "formal"
question = "What is a token?"
prompt = None  # TODO: use an f-string with {tone} and {question}

check("4 prompt", prompt, "Answer in a formal tone.\nQuestion: What is a token?")


# -----------------------------------------------------------------------------
# Exercise 5: Truncate long text
# If text is longer than `limit` characters, keep only the first `limit`
# characters and add "..." at the end. Otherwise keep the text unchanged.
# -----------------------------------------------------------------------------
text = "Large language models predict the next token."
limit = 20
short_text = None  # TODO: use slicing and an if/else

check("5 short_text", short_text, "Large language model...")


# -----------------------------------------------------------------------------
# Exercise 6: Validate temperature
# Set `status` to:
#   "too low"  if temperature is below 0
#   "too high" if temperature is above 1
#   "valid"    otherwise
# Then change `temperature` to 0.5 and -0.2 and rerun to test the other cases
# (expected "valid" and "too low"). Put it back to 1.5 when you're done.
# -----------------------------------------------------------------------------
temperature = 1.5
status = None  # TODO: use if / elif / else

check("6 status", status, "too high")


# -----------------------------------------------------------------------------
# Exercise 7: Route by length
# Count the words in `message`. Set `tier` to:
#   "large"  if there are more than 200 words
#   "medium" if there are more than 50 words
#   "small"  otherwise
# Hint: len(message.split()) gives the word count.
# -----------------------------------------------------------------------------
message = "word " * 120
tier = None  # TODO

check("7 tier", tier, "medium")


# -----------------------------------------------------------------------------
# Exercise 8: A simple safety filter
# Set `decision` to "blocked" if the prompt contains the word "password" or
# the word "secret" (in ANY capitalisation). Otherwise set it to "allowed".
# -----------------------------------------------------------------------------
prompt_text = "Please share the Password for the server"
decision = None  # TODO: lowercase a copy first, then use `in` and `or`

check("8 decision", decision, "blocked")


# -----------------------------------------------------------------------------
# Exercise 9 (challenge): Estimate the cost
# tokens_used tokens at price_per_million dollars per 1,000,000 tokens.
# Store the cost rounded to 4 decimal places in `cost`.
# Hint: round(number, 4)
# -----------------------------------------------------------------------------
tokens_used = 45_000
price_per_million = 2.50
cost = None  # TODO

check("9 cost", cost, 0.1125)
