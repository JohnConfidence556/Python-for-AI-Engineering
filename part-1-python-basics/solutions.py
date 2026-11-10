"""
solutions.py - Week 01 solutions

Try the exercises first! Then compare your answers here.
There is often more than one correct way; yours may differ and still be right.

Run:  python solutions.py   (every line should show ✅)
"""


def check(label, got, expected):
    if got == expected:
        print(f"✅ {label}")
    elif got is None:
        print(f"⬜ {label}: not done yet")
    else:
        print(f"❌ {label}: expected {expected!r} but got {got!r}")


# Exercise 1: Variables and types
model_name = "example-model"   # quotes make it a string
temperature = 0.3              # a decimal point makes it a float
max_tokens = 256               # no decimal point: an int
stream = True                  # capital T, no quotes: a bool

check("1a model_name", model_name, "example-model")
check("1b temperature", temperature, 0.3)
check("1c max_tokens", max_tokens, 256)
check("1d stream", stream, True)


# Exercise 2: Type conversion
user_typed = "512"
# int() turns the text "512" into the number 512, then we can do maths with it.
total_tokens = int(user_typed) + 100

check("2 total_tokens", total_tokens, 612)


# Exercise 3: Clean messy user input
raw_message = "   WhAt Is   MaChiNe LeArNiNg?  "
# split() -> separate words (ignoring all extra spaces)
# " ".join(...) -> glue back with single spaces
# .lower() -> lowercase everything
cleaned = " ".join(raw_message.split()).lower()

check("3 cleaned", cleaned, "what is machine learning?")


# Exercise 4: Build a prompt with an f-string
tone = "formal"
question = "What is a token?"
prompt = f"Answer in a {tone} tone.\nQuestion: {question}"

check("4 prompt", prompt, "Answer in a formal tone.\nQuestion: What is a token?")


# Exercise 5: Truncate long text
text = "Large language models predict the next token."
limit = 20
if len(text) > limit:
    short_text = text[:limit] + "..."   # text[:20] = first 20 characters
else:
    short_text = text

check("5 short_text", short_text, "Large language model...")


# Exercise 6: Validate temperature
temperature = 1.5
if temperature < 0:
    status = "too low"
elif temperature > 1:
    status = "too high"
else:
    status = "valid"

check("6 status", status, "too high")


# Exercise 7: Route by length
message = "word " * 120
word_count = len(message.split())
if word_count > 200:
    tier = "large"
elif word_count > 50:      # only reached if word_count is NOT > 200
    tier = "medium"
else:
    tier = "small"

check("7 tier", tier, "medium")


# Exercise 8: A simple safety filter
prompt_text = "Please share the Password for the server"
lowered = prompt_text.lower()   # lowercase copy so "Password" matches "password"
if "password" in lowered or "secret" in lowered:
    decision = "blocked"
else:
    decision = "allowed"

check("8 decision", decision, "blocked")


# Exercise 9 (challenge): Estimate the cost
tokens_used = 45_000
price_per_million = 2.50
cost = round(tokens_used / 1_000_000 * price_per_million, 4)

check("9 cost", cost, 0.1125)
