"""
cost_calculator.py - Week 01 mini project: LLM Cost Calculator

Every AI engineer eventually gets asked: "How much will this cost us per month?"
This script answers that question for a prompt you type in.

It practises everything from Week 01:
  - variables and constants
  - data types (str, int, float) and converting between them
  - string cleaning and f-strings
  - conditionals (if / elif / else)

Run it with:
    python cost_calculator.py

NOTE: if you type letters where a number is expected, we stop with a message.
In part 04 you'll learn try/except, which handles bad input more gracefully.
"""

import sys

# =============================================================================
# SETTINGS (constants)
# Names in ALL_CAPS tell other programmers: "set once, don't change later."
# =============================================================================

# EXAMPLE prices in US dollars per 1 million tokens. These are made-up numbers
# for practice. Real prices change often, so always check your provider's
# pricing page before budgeting for real.

SMALL_INPUT_PRICE = 0.50
SMALL_OUTPUT_PRICE = 2.00
MEDIUM_INPUT_PRICE = 3.00
MEDIUM_OUTPUT_PRICE = 15.00
LARGE_INPUT_PRICE = 15.00
LARGE_OUTPUT_PRICE = 75.00

CHARS_PER_TOKEN = 4                 # rough rule of thumb for English text
CONTEXT_LIMIT_TOKENS = 8000         # pretend the model can read at most this much
DAYS_PER_MONTH = 30


# =============================================================================
# STEP 0: Welcome message
# =============================================================================

print("=" * 50)
print(" LLM COST CALCULATOR")
print("=" * 50)
print("Answer a few question and get a monthly cost estimate")

# =============================================================================
# STEP 1: Get the prompt and clean it
# =============================================================================

prompt = input("Paster your prompt: ")

# .split() breaks the text into words and throws away extra spaces/newlines.
# " ".join(...) glues the words back together with exactly one space.
# Together they tidy messy whitespace.

prompt = " ".join(prompt.split())

# An empty string is "falsy", so this runs only when nothing was typed.
if prompt == "":
    sys.exiit("No prompt entered. Run the script again and type something")


# =============================================================================
# STEP 2: Expected response length (int)
# =============================================================================
# input() ALWAYS returns a string, even if you type digits.
# .strip() removes accidental spaces around what the user typed.

answer = input("Expected response length in tokens [press Enter for 500]: ").strip()

if answer == "":
    output_tokens = 500
elif answer.isdigit():
    output_tokens = int(answer)
else:
    sys.exit("Please enter a whole number like 300.")



# =============================================================================
# STEP 3: Model tier (decides which prices to use)
# =============================================================================
# .lower() makes "Small", "SMALL" and "small" all equal to "small".

tier = input("Model tier (small / medium / large): ").strip().lower()

if tier == "small":
    input_price = SMALL_INPUT_PRICE
    output_price = SMALL_OUTPUT_PRICE

elif tier == "medium":
    input_price = MEDIUM_INPUT_PRICE
    output_price = MEDIUM_OUTPUT_PRICE
elif tier == "large":
    input_price = LARGE_INPUT_PRICE
    output_price = LARGE_OUTPUT_PRICE
else:
    # f-string: {tier} is replaced with whatever the user typed.
    sys.exit(f"'{tier}' is not a valid tier. Choose small, medium or large.")



# =============================================================================
# STEP 4: Traffic and budget
# =============================================================================

answer = input("How many requests per day? ").strip()
if not answer.isdigit():
    sys.exit("Please enter a whole number like 1000.")
requests_per_day = int(answer)
if requests_per_day == 0:
    sys.exit("Requests per day must be at least 1.")

answer = input("Monthly budget in dollars (whole number)? ").strip()
if not answer.isdigit():
    sys.exit("Please enter a whole number like 50.")
budget = int(answer)



# =============================================================================
# STEP 5: The maths
# =============================================================================
# Estimate input tokens from the number of characters.
# // is "floor division": it throws away the decimal part.


input_tokens = len(prompt) // CHARS_PER_TOKEN
if input_tokens < 1:
    input_tokens = 1  # a prompt always costs at least a little

# Prices are per 1,000,000 tokens, so divide tokens by 1,000,000 first.
# (Underscores in numbers like 1_000_000 are ignored by Python; they just make
# big numbers easier to read.)
input_cost = input_tokens / 1_000_000 * input_price
output_cost = output_tokens / 1_000_000 * output_price

cost_per_request = input_cost + output_cost
daily_cost = cost_per_request * requests_per_day
monthly_cost = daily_cost * DAYS_PER_MONTH


# =============================================================================
# STEP 6: The report
# =============================================================================
# Inside an f-string, a format spec after the colon controls how numbers look:
#   :,     adds thousands separators      (1234567 -> 1,234,567)
#   :.2f   shows exactly 2 decimal places (3.14159 -> 3.14)
print("\n" + "=" * 50)
print("  COST REPORT")
print("=" * 50)
print(f"Model tier        : {tier}")
print(f"Prompt length     : {len(prompt):,} characters (about {input_tokens:,} tokens)")
print(f"Expected response : {output_tokens:,} tokens")
print(f"Cost per request  : ${cost_per_request:.6f}")
print(f"Cost per day      : ${daily_cost:,.2f}  ({requests_per_day:,} requests)")
print(f"Cost per month    : ${monthly_cost:,.2f}")
print(f"Monthly budget    : ${budget:,.2f}")
print()

# Warn if the prompt probably won't fit in the model's context window.
if input_tokens > CONTEXT_LIMIT_TOKENS:
    print(f"⚠️  Your prompt (~{input_tokens:,} tokens) may exceed the "
          f"{CONTEXT_LIMIT_TOKENS:,}-token context limit.")

# Budget verdict. Order matters: Python checks top to bottom and runs the
# FIRST branch that is True, so we test the strictest condition first.
if monthly_cost <= budget * 0.8:
    print("✅ Comfortably within budget.")
elif monthly_cost <= budget:
    print("⚠️  Within budget, but close. Traffic growth could push you over.")
else:
    overspend = monthly_cost - budget
    print(f"❌ Over budget by ${overspend:,.2f} per month.")
    if tier != "small":
        print("Tip: try the 'small' tier, or shorten the response length.")
    else:
        print("Tip: shorten the prompt, cap the response length, or reduce requests.")