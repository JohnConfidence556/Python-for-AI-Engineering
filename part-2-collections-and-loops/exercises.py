"""
exercises.py - Part 02 practice

How to use this file:
  1. Read each exercise.
  2. Replace every `None` with your own code (look for the TODO comments).
  3. Run:  python exercises.py
  4. Each exercise prints ✅ (correct), ❌ (wrong) or ⬜ (not done yet).

Try every exercise before opening solutions.py. Getting stuck is part of learning.
"""


# -----------------------------------------------------------------------------
# Helper: checks your answer. Functions are covered in Part 03, so just use it as
# is: check(label, your_answer, expected)
# -----------------------------------------------------------------------------
def check(label, got, expected):
    if got == expected:
        print(f"✅ {label}")
    elif got is None:
        print(f"⬜ {label}: not done yet")
    else:
        print(f"❌ {label}: expected {expected!r} but got {got!r}")


# -----------------------------------------------------------------------------
# Exercise 1: List operations
# Start from the list below, then do these steps IN ORDER by changing `prompts`:
#   a) add "translate" to the END
#   b) insert "classify" at position 0 (the start)
#   c) remove "summarise"
# Then fill in `first_two` (the first two items, using a slice)
# and `last_item` (the last item, using a negative index).
# Hint: .append(), .insert(index, item), .remove(item)
# -----------------------------------------------------------------------------
prompts = ["summarise", "extract", "rewrite"]
# TODO: steps a, b, c go here (they are statements, not assignments to None)

first_two = None   # TODO
last_item = None   # TODO

check("1a prompts", prompts, ["classify", "extract", "rewrite", "translate"])
check("1b first_two", first_two, ["classify", "extract"])
check("1c last_item", last_item, "translate")


# -----------------------------------------------------------------------------
# Exercise 2: Tuple unpacking
# An API reports token usage as a tuple. Unpack it into two variables in ONE
# line, then compute the total.
# -----------------------------------------------------------------------------
usage = (1200, 350)
input_tokens = None    # TODO: unpack usage into input_tokens and output_tokens
output_tokens = None   # (hint: a, b = some_tuple)
total_tokens = None    # TODO: input_tokens + output_tokens

check("2a input_tokens", input_tokens, 1200)
check("2b output_tokens", output_tokens, 350)
check("2c total_tokens", total_tokens, 1550)


# -----------------------------------------------------------------------------
# Exercise 3: Dictionaries
# Starting from `request`, do these steps IN ORDER by changing the dictionary:
#   a) add a new key "stream" with the value True
#   b) change "temperature" to 0.2
#   c) delete the key "debug"
# Then set `top_p` to the value stored under "top_p", or 1.0 if the key is
# missing. Hint: .get(key, default)
# -----------------------------------------------------------------------------
request = {"model": "example-model", "temperature": 0.9, "debug": True}
# TODO: steps a, b, c go here

top_p = None   # TODO

check("3a request", request, {"model": "example-model", "temperature": 0.2, "stream": True})
check("3b top_p", top_p, 1.0)


# -----------------------------------------------------------------------------
# Exercise 4: Nested data
# An API response is a dictionary that contains a list that contains a dictionary.
# Reach in and pull out the reply text and the output token count.
# -----------------------------------------------------------------------------
response = {
    "id": "resp_001",
    "choices": [
        {"role": "assistant", "content": "Tokens are chunks of text."}
    ],
    "usage": {"input_tokens": 12, "output_tokens": 6},
}
reply_text = None     # TODO: first item of "choices", then its "content"
output_count = None   # TODO: the "output_tokens" value inside "usage"

check("4a reply_text", reply_text, "Tokens are chunks of text.")
check("4b output_count", output_count, 6)


# -----------------------------------------------------------------------------
# Exercise 5: Loop and accumulate
# Add up the "tokens" value of every message with a for loop.
# -----------------------------------------------------------------------------
history = [
    {"role": "user", "tokens": 12},
    {"role": "assistant", "tokens": 85},
    {"role": "user", "tokens": 9},
    {"role": "assistant", "tokens": 120},
]
history_total = 0
# TODO: write a for loop that adds each message's "tokens" to history_total

check("5 history_total", history_total, 226)


# -----------------------------------------------------------------------------
# Exercise 6: Filter with a comprehension
# Build a list of ONLY the content of the user messages, using a list
# comprehension (one line, in square brackets).
# -----------------------------------------------------------------------------
chat = [
    {"role": "system", "content": "Be concise."},
    {"role": "user", "content": "Hi"},
    {"role": "assistant", "content": "Hello! How can I help?"},
    {"role": "user", "content": "Explain RAG"},
]
user_texts = None   # TODO: [... for m in chat if ...]

check("6 user_texts", user_texts, ["Hi", "Explain RAG"])


# -----------------------------------------------------------------------------
# Exercise 7: Count words with a dictionary
# Count how many times each word appears in `sentence`.
# Use the counting pattern: counts[word] = counts.get(word, 0) + 1
# -----------------------------------------------------------------------------
sentence = "to be or not to be"
word_counts = {}
# TODO: loop over sentence.split() and fill word_counts

check("7 word_counts", word_counts, {"to": 2, "be": 2, "or": 1, "not": 1})


# -----------------------------------------------------------------------------
# Exercise 8: Sets
# Two documents have these tags. Use set operations to find:
#   shared      : tags that appear in BOTH documents
#   all_tags    : every tag that appears in EITHER document
#   only_in_a   : tags in doc_a that are NOT in doc_b
# Hint: &  |  -
# -----------------------------------------------------------------------------
doc_a = {"ai", "python", "nlp", "llm"}
doc_b = {"python", "llm", "data"}
shared = None      # TODO
all_tags = None    # TODO
only_in_a = None   # TODO

check("8a shared", shared, {"python", "llm"})
check("8b all_tags", all_tags, {"ai", "python", "nlp", "llm", "data"})
check("8c only_in_a", only_in_a, {"ai", "nlp"})


# -----------------------------------------------------------------------------
# Exercise 9: A retry loop with while
# These are the results of simulated API calls, in order. Keep "calling"
# until you get "ok". Count how many attempts it took.
# Hint: use an index variable, and break out of the loop when you see "ok".
# -----------------------------------------------------------------------------
results = ["error", "error", "ok", "ok"]
attempts = 0
# TODO: while loop. On each pass: look at results[attempts], add 1 to attempts,
#       and break if that result was "ok"

check("9 attempts", attempts, 3)


# -----------------------------------------------------------------------------
# Exercise 10 (challenge): Batching
# APIs often limit how many items you can send at once. Split `documents` into
# batches of 4, giving a list of lists.
# Hint: range(0, len(documents), 4) counts 0, 4, 8, and documents[i:i+4] is a slice.
# -----------------------------------------------------------------------------
documents = ["d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10"]
batches = None   # TODO: start with [], then loop and append slices

check("10 batches", batches, [["d1", "d2", "d3", "d4"], ["d5", "d6", "d7", "d8"], ["d9", "d10"]])
