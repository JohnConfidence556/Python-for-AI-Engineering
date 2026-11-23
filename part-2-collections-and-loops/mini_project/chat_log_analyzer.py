"""
chat_log_analyzer.py - Part 02 mini project: Chat Log Analyzer

Real LLM apps store a conversation as a LIST of DICTIONARIES, one dict per
message, each with a "role" and "content". This is the exact format most LLM
APIs use, so learning to analyse it now pays off in every later part.

This script reads a conversation and reports:
  - how many messages each role sent         (dict + loop)
  - an estimate of tokens per role           (loop + arithmetic)
  - the longest message                      (loop + conditional)
  - the most common words                    (dict + set + tuples + sorting)
  - what would remain if we trimmed history  (list slicing)

Run it with:
    python mini_project/chat_log_analyzer.py

Everything here uses only ideas from Parts 00 to 02. No functions yet (Part 03).
"""

# =============================================================================
# THE DATA: a conversation, exactly as an LLM API expects it
# =============================================================================
messages = [
    {"role": "system", "content": "You are a helpful assistant that explains AI concepts simply."},
    {"role": "user", "content": "What is a token in a language model?"},
    {"role": "assistant", "content": "A token is a small chunk of text, like a word or part of a word. Models read and write text one token at a time."},
    {"role": "user", "content": "Why do tokens matter for cost?"},
    {"role": "assistant", "content": "Providers charge per token, so longer prompts and longer answers cost more. Keeping prompts short saves money."},
    {"role": "user", "content": "How can I reduce the number of tokens I send?"},
    {"role": "assistant", "content": "Remove filler words, trim old messages from the history, and ask for short answers. Fewer tokens means lower cost and faster replies."},
]

print("=" * 56)
print("  CHAT LOG ANALYZER")
print("=" * 56)

CHARS_PER_TOKEN = 4  # rough rule of thumb for English text

# =============================================================================
# 1. MESSAGES AND TOKENS PER ROLE
# =============================================================================
# Two dictionaries, both keyed by role name. They start empty and fill up as we loop.

message_counts = {}
token_counts = {}

for message in messages:            # message is one dict at a time
    role = message["role"]          # read a value by its key
    content = message["content"]

    tokens = len(content) // CHARS_PER_TOKEN # estimate tokens from characters
    if tokens < 1:
        tokens = 1

    # THE COUNTING PATTERN, one of the most useful in Python:
    # .get(role, 0) returns the current count, or 0 if this role is new.
    # We add 1 and store it back.
    message_counts[role] = message_counts.get(role, 0) + 1
    token_counts[role] = token_counts.get(role, 0) + tokens

print("\nMESSAGES AND ESTIMATED TOKENS PER ROLE")
print("-" * 56)
total_tokens = 0
for role, count in message_counts.items():      # .items() gives (key, value) pairs
    tokens = token_counts[role]
    total_tokens += tokens
    # Format specs: <10 left-aligns in 10 spaces, >3 right-aligns in 3 spaces.
    print(f"{role:<10} {count:>3} messages   ~{tokens:>4} tokens")
print(f"{'TOTAL':<10} {len(messages):>3} messages   ~{total_tokens:>4} tokens")



# =============================================================================
# 2. THE LONGEST MESSAGE
# =============================================================================
# Pattern: remember the best-so-far, and replace it whenever we find a better one.
longest = messages[0]
for message in messages:
    if len(message["content"]) > len(longest["content"]):
        longest = message

print("\nLONGEST MESSAGE")
print("-" * 56)
print(f"Role   : {longest['role']}")
print(f"Length : {len(longest['content'])} characters")
print(f"Preview: {longest['content'][:60]}...")   # slice: first 60 characters


# =============================================================================
# 3. WORD FREQUENCY
# =============================================================================
# A set of "stop words": very common words that tell us nothing about the topic.
# Sets are fast for "is this item in the collection?" checks.
stop_words = {
    "a", "the", "is", "of", "to", "and", "in", "it", "for", "can", "i", "you",
    "that", "are", "or", "so", "by", "on", "with", "as", "be", "this", "how",
    "what", "why", "like", "one", "from", "do", "me", "my", "we",
}

word_counts = {}
for message in messages:
    if message["role"] == "system":
        continue                                    # skip the system prompt, go to the next message
    # lower() so "Tokens" and "tokens" count together; split() makes a list of words.
    for word in message["content"].lower().split():
        word = word.strip(".,?!")              # remove punctuation from both ends
        if word == "" or word in stop_words:
            continue
        word_counts[word] = word_counts.get(word, 0) + 1

# Turn the dictionary into a list of (sort_key, word) tuples and sort it.
# A SORTING TRICK: Python sorts tuples by their first item, smallest first.
# Storing the count as a NEGATIVE number puts the biggest counts first,
# and words with equal counts fall into alphabetical order.

pairs = []
for word, count in word_counts.items():
    pairs.append((-count, word))
pairs.sort()

print("\nTOP 5 WORDS (stop words and the system prompt excluded)")
print("-" * 56)
for negative_count, word in pairs[:5]:         # slice: first five pairs
    count = -negative_count                    # flip back to positive for display
    bar = "█" * count                          # a string times a number repeats it
    print(f"{word:<12} {count:>2}  {bar}")

# set() keeps only unique items, so len() of the set = number of different words.
print(f"\nDifferent words used: {len(set(word_counts))}")



# =============================================================================
# 4. TRIMMING HISTORY (a preview of Part 09: chatbots with memory)
# =============================================================================
# Models can only read so many tokens, so chatbots often keep just the newest
# messages. Negative slicing grabs the last N items of a list.
KEEP_LAST = 4
conversation_only = [m for m in messages if m["role"] != "system"]   # list comprehension
recent = conversation_only[-KEEP_LAST:]

recent_tokens = 0
for message in recent:
    recent_tokens += max(1, len(message["content"]) // CHARS_PER_TOKEN)

print("\nIF WE KEPT ONLY THE LAST", KEEP_LAST, "MESSAGES")
print("-" * 56)
print(f"Messages kept : {len(recent)} of {len(conversation_only)}")
print(f"Tokens kept   : ~{recent_tokens} of ~{total_tokens}")
