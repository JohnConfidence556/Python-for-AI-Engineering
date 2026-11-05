# Python for AI Engineering

A free, practical, week-by-week path from **zero Python** to **building real AI applications**: calling LLMs, structured output, chatbots with memory, databases, and a deployed capstone.

New lessons are released **every week**. Follow along, run the code, do the exercises, and build something each week.

> Built in public. If this helps you, give the repo a ⭐ and share your progress.

---

## Who this is for

- Complete beginners who want to become AI engineers
- Developers from other languages who want the Python AI toolkit
- Students who learn best by building small projects

**No prior programming experience needed.** You only need a computer and curiosity.

---

## How the repo works

Every week lives in its own folder and follows the same layout:

```
week-XX-topic/
├── README.md        # concept, why it matters for AI, setup notes
├── lesson.ipynb     # explained, runnable walkthrough (notebook)
├── *.py             # script versions of the code
├── exercises.py     # practice tasks with TODOs
├── solutions.py     # try first, peek later
└── mini_project/    # a small build using the week's ideas
```

- **Notebooks** (`.ipynb`) are used when you need to experiment and see results step by step.
- **Scripts** (`.py`) are used when the code should run like a real program.

Each week's README tells you which file to open first.

---

## Roadmap

| Week | Topic | We will build | Status |
|---|---|---|---|
| [00](./week-00-setup) | Setup: Python, venv/uv, VS Code, Git, running a script | "Hello AI" script | ✅ Available |
| 01 | Python basics: variables, data types, strings, conditionals | to be updated | 🔜 Soon |
| 02 | Collections and loops: lists, tuples, dicts, sets, comprehensions | to be updated | 🔜 Soon |
| 03 | Functions: args, kwargs, scope, type hints, lambdas | to be updated | 🔜 Soon |
| 04 | Error handling and file handling: try/except, JSON, CSV, `pathlib` | to be updated | 🔜 Soon |
| 05 | Classes and OOP: methods, inheritance, dataclasses | to be updated | 🔜 Soon |
| 06 | APIs: HTTP, `requests`, auth, env vars, retries | to be updated | 🔜 Soon |
| 07 | Calling an LLM: SDKs, roles, tokens, streaming | to be updated | 🔜 Soon |
| 08 | Structured output: Pydantic, validation, retries | to be updated | 🔜 Soon |
| 09 | Chatbot with memory: history, context limits | Terminal chatbot that remembers | 🔜 Soon |
| 10 | Databases: SQL, SQLite, CRUD | to be updated | 🔜 Soon |
| 11 | AI tools: pandas, NumPy, embeddings, semantic search | to be updated | 🔜 Soon |
| 12 | Capstone: FastAPI, tests, deployment | to be updated | 🔜 Soon |

### Your progress

- [ ] Week 00: Setup
- [ ] Week 01: Python basics
- [ ] Week 02: Collections and loops
- [ ] Week 03: Functions
- [ ] Week 04: Error handling and files
- [ ] Week 05: Classes and OOP
- [ ] Week 06: APIs
- [ ] Week 07: Calling an LLM
- [ ] Week 08: Structured output
- [ ] Week 09: Chatbot with memory
- [ ] Week 10: Databases
- [ ] Week 11: AI tools
- [ ] Week 12: Capstone

---

## Quick start

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/python-for-ai-engineering.git
cd python-for-ai-engineering

# 2. Create and activate a virtual environment
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Copy the env template (you'll add API keys from Week 6 onward)
cp .env.example .env
```

Not sure about any of these steps? **Start with [Week 00](./week-00-setup)**. It explains every one of them.

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