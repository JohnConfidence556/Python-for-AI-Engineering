# Part 02: Collections and Loops

**Time needed:** 4-5 hours
**Prerequisites:** [Part 01](../part-01-python-basics) (variables, types, strings, conditionals)
**Goal:** Store groups of data, repeat work over it, and read the nested data that LLM APIs send and receive.

---

## Why this matters for AI engineering

In Part 01 each variable held one value. Real AI work deals in **groups**:

| In AI engineering you handle... | ...stored as a |
|---|---|
| a conversation (many messages) | **list** |
| one message (`role` + `content`) | **dictionary** |
| token usage `(input, output)` | **tuple** |
| unique labels or tags | **set** |
| "do this for every document" | **loop** |

The single most important shape to remember is this one. It is how chat APIs represent a conversation:

```python
conversation = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is a token?"},
    {"role": "assistant", "content": "A token is a small chunk of text."},
]
```

A **list of dictionaries**. By the end of this part you'll be able to loop over it, count things in it, filter it and trim it.

---

## What's in this folder

| File | What to do with it |
|---|---|
| `lesson.ipynb` | **Start here.** Run it cell by cell and change the code as you go |
| `exercises.py` | 10 practice tasks with TODOs. Run `python exercises.py` to check yourself |
| `mini_project/chat_log_analyzer.py` | Read, run, then extend the Chat Log Analyzer |
| `solutions.py` | Peek only after you've tried each exercise |

---

## What you'll learn

1. **Lists**: indexing, slicing, `append`, `insert`, `remove`, `pop`, `sorted`, copying safely
2. **Tuples**: fixed bundles and unpacking (`input_tokens, output_tokens = usage`)
3. **Dictionaries**: `[]` vs `.get()`, adding, deleting, `.items()`, merging with `|`, nested data
4. **Sets**: removing duplicates, `&` `|` `-` set maths, fast membership checks
5. **Loops**: `for`, `while`, `range`, `enumerate`, `zip`, `break`, `continue`, nested loops
6. **Loop patterns**: accumulate, filter, count with a dict, batch with `range` + slice
7. **Comprehensions**: list, dict and set versions
8. **Putting it together**: trimming a chat history to fit a token budget

---

## How to work through this part

1. Open `lesson.ipynb` in VS Code and select your `.venv` kernel. Run every cell and **change values to see what happens**.
2. Open `exercises.py`, replace each `None` (or fill in the TODO), and run:

   ```bash
   python exercises.py
   ```

   You'll see ⬜ for anything unstarted, ❌ for wrong answers, and ✅ as you get them right.
3. Run the mini project:

   ```bash
   python mini_project/chat_log_analyzer.py
   ```

4. Compare with `solutions.py`.

---

## Mini project: Chat Log Analyzer

Takes a conversation (a list of message dictionaries) and reports:

- messages and estimated tokens **per role**
- the **longest** message
- the **top 5 words** (ignoring common stop words), with a bar chart
- how many **different words** were used
- what would be left if you **kept only the last 4 messages**

Sample output:

```
MESSAGES AND ESTIMATED TOKENS PER ROLE
--------------------------------------------------------
system       1 messages   ~  15 tokens
user         3 messages   ~  27 tokens
assistant    3 messages   ~  88 tokens
TOTAL        7 messages   ~ 130 tokens

TOP 5 WORDS (stop words and the system prompt excluded)
--------------------------------------------------------
token         4  ████
cost          3  ███
tokens        3  ███
answers       2  ██
longer        2  ██
```

You can type in your own message when the script starts, and watch the numbers change.

**Stretch goals:**
- Replace the sample conversation with your own 6+ message chat.
- Also show the **average** message length per role.
- Treat `token` and `tokens` as the same word (hint: look at how a word ends).
- Print the top 10 instead of the top 5.

---

## Common mistakes

- `my_list[3]` on a 3-item list: valid positions are 0, 1 and 2 (`IndexError`)
- `my_dict["missing"]` crashes (`KeyError`). Use `.get("missing", default)`
- `items = items.sort()` sets `items` to `None`. Call `.sort()` alone or use `sorted()`
- `b = a` doesn't copy a list or dict. Use `a.copy()`
- `{}` is an empty **dict**; use `set()` for an empty set
- `for k, v in my_dict:` fails. You need `my_dict.items()`
- A `while` loop whose condition never changes runs forever. Add a maximum count
- Removing items from a list while looping over it skips items

---

## Checklist

- [ ] I can explain the difference between a list, tuple, dict and set
- [ ] I can read a value from nested data like `response["choices"][0]["content"]`
- [ ] I can use `.get()` to avoid a `KeyError`
- [ ] I can write the counting pattern from memory
- [ ] I can turn a loop-and-append into a list comprehension
- [ ] All 10 exercises show ✅
- [ ] I ran the Chat Log Analyzer and tried my own message

**Next:** Part 03, functions (arguments, return values, scope, type hints, lambdas).
