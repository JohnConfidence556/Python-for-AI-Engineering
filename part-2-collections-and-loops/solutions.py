"""
solutions.py - Part 02 solutions

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


# Exercise 1: List operations
prompts = ["summarise", "extract", "rewrite"]
prompts.append("translate")        # add to the end
prompts.insert(0, "classify")      # insert at position 0
prompts.remove("summarise")        # remove by value

first_two = prompts[:2]            # slice: index 0 up to (not including) 2
last_item = prompts[-1]            # -1 is the last item

check("1a prompts", prompts, ["classify", "extract", "rewrite", "translate"])
check("1b first_two", first_two, ["classify", "extract"])
check("1c last_item", last_item, "translate")


# Exercise 2: Tuple unpacking
usage = (1200, 350)
input_tokens, output_tokens = usage     # first item -> first name, second -> second
total_tokens = input_tokens + output_tokens

check("2a input_tokens", input_tokens, 1200)
check("2b output_tokens", output_tokens, 350)
check("2c total_tokens", total_tokens, 1550)


# Exercise 3: Dictionaries
request = {"model": "example-model", "temperature": 0.9, "debug": True}
request["stream"] = True           # new key: just assign to it
request["temperature"] = 0.2       # existing key: assigning replaces the value
del request["debug"]               # delete a key (request.pop("debug") also works)

top_p = request.get("top_p", 1.0)  # key is missing, so we get the default 1.0

check("3a request", request, {"model": "example-model", "temperature": 0.2, "stream": True})
check("3b top_p", top_p, 1.0)


# Exercise 4: Nested data
response = {
    "id": "resp_001",
    "choices": [
        {"role": "assistant", "content": "Tokens are chunks of text."}
    ],
    "usage": {"input_tokens": 12, "output_tokens": 6},
}
# Read it from the outside in: dict -> "choices" list -> item 0 (a dict) -> "content"
reply_text = response["choices"][0]["content"]
output_count = response["usage"]["output_tokens"]

check("4a reply_text", reply_text, "Tokens are chunks of text.")
check("4b output_count", output_count, 6)


# Exercise 5: Loop and accumulate
history = [
    {"role": "user", "tokens": 12},
    {"role": "assistant", "tokens": 85},
    {"role": "user", "tokens": 9},
    {"role": "assistant", "tokens": 120},
]
history_total = 0
for message in history:
    history_total += message["tokens"]

check("5 history_total", history_total, 226)


# Exercise 6: Filter with a comprehension
chat = [
    {"role": "system", "content": "Be concise."},
    {"role": "user", "content": "Hi"},
    {"role": "assistant", "content": "Hello! How can I help?"},
    {"role": "user", "content": "Explain RAG"},
]
# Read it as: "give me m['content'] for every m in chat, but only if m is a user message"
user_texts = [m["content"] for m in chat if m["role"] == "user"]

check("6 user_texts", user_texts, ["Hi", "Explain RAG"])


# Exercise 7: Count words with a dictionary
sentence = "to be or not to be"
word_counts = {}
for word in sentence.split():
    word_counts[word] = word_counts.get(word, 0) + 1

check("7 word_counts", word_counts, {"to": 2, "be": 2, "or": 1, "not": 1})


# Exercise 8: Sets
doc_a = {"ai", "python", "nlp", "llm"}
doc_b = {"python", "llm", "data"}
shared = doc_a & doc_b       # intersection: in both
all_tags = doc_a | doc_b     # union: in either
only_in_a = doc_a - doc_b    # difference: in a but not in b

check("8a shared", shared, {"python", "llm"})
check("8b all_tags", all_tags, {"ai", "python", "nlp", "llm", "data"})
check("8c only_in_a", only_in_a, {"ai", "nlp"})


# Exercise 9: A retry loop with while
results = ["error", "error", "ok", "ok"]
attempts = 0
while attempts < len(results):       # safety: never run past the end of the list
    result = results[attempts]       # look at this attempt's outcome
    attempts += 1                    # count the attempt BEFORE we decide to stop
    if result == "ok":
        break                        # success: leave the loop immediately

check("9 attempts", attempts, 3)


# Exercise 10 (challenge): Batching
documents = ["d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10"]
batch_size = 4
batches = []
for start in range(0, len(documents), batch_size):    # start = 0, 4, 8
    batches.append(documents[start:start + batch_size])
    # The last slice (8 to 12) just stops at the end of the list: no error.

check("10 batches", batches, [["d1", "d2", "d3", "d4"], ["d5", "d6", "d7", "d8"], ["d9", "d10"]])
