# part 01: Python Basics

**Time needed:** 3-4 hours
**Prerequisites:** [Week 00](../week-00-setup) (Python installed, `.venv` working)
**Goal:** Read and write the building blocks of every Python program, using examples from real AI work.

---

## Why this matters for AI engineering

Every LLM call is built from these four ideas:

| Concept | Where it shows up in AI work |
|---|---|
| **Variables** | model name, temperature, `max_tokens`, API settings |
| **Data types** | token counts (`int`), prices and scores (`float`), `stream=True` (`bool`), a missing API key (`None`) |
| **Strings** | prompts, system instructions, model replies, cleaning user input |
| **Conditionals** | validate settings, route to a model, block bad input, handle a missing key |

If these feel solid, the rest of the course gets much easier.

---

## What's in this folder

| File | What to do with it |
|---|---|
| `lesson.ipynb` | **Start here.** Run it cell by cell and change the code as you go |
| `exercises.py` | 9 practice tasks with TODOs. Run `python exercises.py` to check yourself |
| `mini_project/cost_calculator.py` | Build and run an LLM cost calculator |
| `solutions.py` | Peek only after you've tried each exercise |

---

## What you'll learn

1. **Variables**: naming rules, `snake_case`, `ALL_CAPS` constants, updating with `+=`
2. **Data types**: `str`, `int`, `float`, `bool`, `None`, and converting with `int()`, `float()`, `str()`
3. **Numbers**: `/`, `//`, `%`, `**`, why `0.1 + 0.2` isn't `0.3`, and chunking a document
4. **Strings**: f-strings and number formatting, indexing, slicing, `strip()`, `lower()`, `split()`, `join()`, `replace()`, `in`
5. **Conditionals**: `if` / `elif` / `else`, comparisons, `and` / `or` / `not`, truthiness, `is None`
6. **Pulling it together**: a "pre-flight check" that validates a prompt before it would be sent to a model

---

## How to work through this week

1. Open `1.1_lesson.ipynb`, `1.2_data_type.ipynb`, `1.3_conditionals.ipynb`, `1.4_mini_task.ipynb`  in VS Code and select your `.venv` kernel.
2. Run every cell. **Change values and rerun** to see what happens.
3. Open `exercises.py`, replace each `None` with your answer, and run:

   ```bash
   python exercises.py
   ```

   You should see ⬜ for every unfinished exercise and ✅ as you complete them.
4. Run the mini project:

   ```bash
   python cost_calculator.py
   ```

5. Compare with `solutions.py`.

---

## Mini project: LLM Cost Calculator

Every AI engineer gets asked, *"What will this cost per month?"* This script asks for your prompt, expected reply length, model tier, daily requests and budget, then prints a cost report and a budget verdict.

Sample run:

```
Paste your prompt: Explain how transformers work in simple terms
Expected response length in tokens [press Enter for 500]: 300
Model tier (small / medium / large): medium
How many requests per day? 1000
Monthly budget in dollars (whole number)? 50

Cost per request  : $0.004533
Cost per day      : $4.53  (1,000 requests)
Cost per month    : $135.99
Monthly budget    : $50.00

❌ Over budget by $85.99 per month.
Tip: try the 'small' tier, or shorten the response length.
```

> **The prices in the script are made up for practice.** Real prices change often. Always check your provider's pricing page before budgeting.

**Stretch goals:**
- Add a fourth tier called `"tiny"` with your own prices.
- Print the cost per 1,000 requests as well.
- Warn when the response length is over 2,000 tokens.

---

## Common mistakes

- Using `=` instead of `==` inside an `if`
- Forgetting the `:` after `if` / `elif` / `else`
- Wrong indentation (use 4 spaces)
- Adding text and numbers (`"5" + 5`). Convert first: `int("5") + 5`
- Writing `text.strip()` without storing the result. Strings never change in place
- Writing `"True"` or `"None"` with quotes, which makes them text

---

## Checklist

- [ ] I can explain the difference between `str`, `int`, `float` and `bool`
- [ ] I can build a prompt with an f-string
- [ ] I can clean text with `strip()`, `lower()` and `split()`
- [ ] I can write an `if` / `elif` / `else` and explain why order matters
- [ ] All 9 exercises show ✅
- [ ] I ran the cost calculator with my own numbers

**Next:** part 02, collections and loops (lists, tuples, dicts, sets, `for`/`while`, comprehensions).