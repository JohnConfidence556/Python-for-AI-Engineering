# Python for AI Engineering

A free, practical, part-by-part path from **zero Python** to **building real AI applications**: calling LLMs, structured output, chatbots with memory, databases, and a deployed capstone.

New parts are released **every week**. Follow along, run the code, do the exercises, and build something in each part.

> Built in public. If this helps you, give the repo a ⭐ and share your progress.

---

## Who this is for

- Complete beginners who want to become AI engineers
- Developers from other languages who want the Python AI toolkit
- Students who learn best by building small projects

**No prior programming experience needed.** You only need a computer and curiosity.

---

## How the repo works

Every part lives in its own folder and follows the same layout:

```
part-XX-topic/
├── README.md        # concept, why it matters for AI, setup notes
├── lesson.ipynb     # explained, runnable walkthrough (notebook)
├── *.py             # script versions of the code
├── exercises.py     # practice tasks with TODOs
├── solutions.py     # try first, peek later
└── mini_project/    # a small build using the part's ideas
```

- **Notebooks** (`.ipynb`) are used when you need to experiment and see results step by step.
- **Scripts** (`.py`) are used when the code should run like a real program.

Each part's README tells you which file to open first.

---

## Roadmap

| Part | Topic | You will build | Status |
|---|---|---|---|
| [00](./part-00-setup) | Setup: Python, venv/uv, VS Code, Git, running a script | "Hello AI" script | ✅ Available |
| [01](./part-01-python-basics) | Python basics: variables, data types, strings, conditionals | LLM cost calculator | ✅ Available |
| [02](./part-02-collections-and-loops) | Collections and loops: lists, tuples, dicts, sets, loops, comprehensions | Chat log analyzer | ✅ Available |
| 03 | Functions: args, kwargs, scope, type hints, lambdas | Text-cleaning toolkit | 🔜 Soon |
| 04 | Error handling and file handling: try/except, JSON, CSV, `pathlib` | Expense tracker saving to JSON | 🔜 Soon |
| 05 | Classes and OOP: methods, inheritance, dataclasses | `Message` and `Conversation` classes | 🔜 Soon |
| 06 | APIs: HTTP, `requests`, auth, env vars, retries | Weather/news fetcher | 🔜 Soon |
| 07 | Calling an LLM: SDKs, roles, tokens, streaming | CLI Q&A tool | 🔜 Soon |
| 08 | Structured output: Pydantic, validation, retries | Info extractor for messy text | 🔜 Soon |
| 09 | Chatbot with memory: history, context limits | Terminal chatbot that remembers | 🔜 Soon |
| 10 | Databases: SQL, SQLite, CRUD | Chatbot with saved conversations | 🔜 Soon |
| 11 | AI tools: pandas, NumPy, embeddings, semantic search | Search over your own notes | 🔜 Soon |
| 12 | Capstone: FastAPI, tests, deployment | An end-to-end AI app | 🔜 Soon |

### Your progress

- [ ] Part 00: Setup
- [ ] Part 01: Python basics
- [ ] Part 02: Collections and loops
- [ ] Part 03: Functions
- [ ] Part 04: Error handling and files
- [ ] Part 05: Classes and OOP
- [ ] Part 06: APIs
- [ ] Part 07: Calling an LLM
- [ ] Part 08: Structured output
- [ ] Part 09: Chatbot with memory
- [ ] Part 10: Databases
- [ ] Part 11: AI tools
- [ ] Part 12: Capstone

---

## Quick start

```bash
# 1. Clone the repo
git clone https://github.com/JohnConfidence556/Python-for-AI-Engineering.git
cd Python-for-AI-Engineering

# 2. Create and activate a virtual environment
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Copy the env template (you'll add API keys from Part 6 onward)
cp .env.example .env
```

Not sure about any of these steps? **Start with [Part 00](./part-00-setup)**. It explains every one of them.

---

## Rules of the road

1. **Type the code yourself.** Copy-pasting teaches you very little.
2. **Do the exercises before opening solutions.**
3. **Never commit API keys.** Keys live in `.env`, which is git-ignored.
4. **Stuck?** Open a GitHub Issue or start a Discussion. Questions help the next learner too.

---

## Contributing

Found a typo, a broken command, or a clearer way to explain something? Pull requests and issues are welcome.

## License

MIT. Use it, learn from it, and share it.
