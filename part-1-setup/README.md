# Setup

**Time needed:** 1-2 hours
**Prerequisites:** A computer and an internet connection
**Goal:** By the end, you can create a project, isolate its packages, write a script, run it, and push it to GitHub.

---

## Why this matters for AI engineering

Most "it doesn't work on my machine" problems in AI come from the environment, not the code. Wrong Python version, packages installed globally, a leaked API key. Get your setup right once and every later week gets easier.

---

## 1. Install Python

1. Download Python 3.11 or newer from [python.org/downloads](https://www.python.org/downloads/).
2. **Windows:** on the first installer screen, tick **"Add python.exe to PATH"** before clicking Install. Missing this is the most common beginner mistake.
3. Verify in a terminal:

```bash
python --version
```

You should see something like `Python 3.12.x`. On macOS/Linux you may need `python3 --version`.

---

## 2. Virtual environments

A **virtual environment** is a private folder of packages for one project. Without it, every project shares one pile of packages and versions eventually clash.

### Option A: `venv` (built into Python)

```bash
python -m venv .venv
```

Activate it:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# Windows CMD
.venv\Scripts\activate.bat

# macOS / Linux
source .venv/bin/activate
```

When active, your terminal prompt starts with `(.venv)`. Leave it with `deactivate`.

> **PowerShell error about scripts being disabled?** Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, then try again.

Install packages with `pip`:

```bash
pip install requests
pip freeze > requirements.txt
```

### Option B: `uv` (faster, modern)

[`uv`](https://docs.astral.sh/uv/) does the same job as `venv` + `pip`, but much faster.

```bash
pip install uv          # or follow the install guide in the uv docs
uv venv                 # creates .venv
uv pip install requests # installs into it
uv run hello_ai.py      # runs a script inside the environment
```

**Which should you use?** Start with `venv`, since it ships with Python and every tutorial assumes it. Switch to `uv` once you're comfortable. The concept is identical.

---

## 3. VS Code

1. Install [VS Code](https://code.visualstudio.com/).
2. Install these extensions (Extensions icon, left sidebar):
   - **Python** (Microsoft)
   - **Jupyter** (Microsoft)
3. Open the project folder: **File → Open Folder**.
4. Select your interpreter: `Ctrl+Shift+P` (`Cmd+Shift+P` on Mac), type **Python: Select Interpreter**, and choose the one inside `.venv`.
5. Open the built-in terminal with `` Ctrl+` ``.

---

## 4. Git and GitHub basics

Git tracks changes to your files. GitHub hosts your repo online.

1. Install Git from [git-scm.com](https://git-scm.com/downloads).
2. Tell Git who you are (once per computer):

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

3. The core loop:

```bash
git init                        # start tracking this folder
git add .                       # stage all changes
git commit -m "Add week 00"     # save a snapshot with a message
```

4. Create an empty repo on GitHub, then connect and push:

```bash
git branch -M main
git remote add origin https://github.com/<your-username>/python-for-ai-engineering.git
git push -u origin main
```

After the first push, your everyday routine is just `git add .`, `git commit -m "..."`, `git push`.

**Always check `.gitignore` before your first commit.** It keeps `.venv/` and `.env` (your secrets) out of GitHub.

---

## 5. Running a Python script

Open `hello_ai.py` in this folder and read it first. Every line is explained in comments. Then run it:

```bash
python hello_ai.py
```

It will ask for your name, then print a short summary of your setup. The same ideas are in `lesson.ipynb` if you prefer a notebook. Pick a kernel by clicking **Select Kernel** (top right) and choosing your `.venv`.

### Script vs notebook: when to use which

| | Script (`.py`) | Notebook (`.ipynb`) |
|---|---|---|
| Best for | Programs you run start to finish | Experimenting, exploring, teaching |
| Runs | Whole file, top to bottom | One cell at a time |
| In this course | Apps, tools, the capstone | Concept lessons, data exploration |

---

## Exercises

1. Create a new virtual environment called `.venv-test`, activate it, run `pip list`, and delete it afterwards. What do you notice about the package list?
2. Edit `hello_ai.py` to also ask for your favourite programming language and print it back.
3. Make a commit with a message that describes your change, then push it to GitHub.
4. Open `setup.ipynb`, run every cell, and add one cell of your own that does the given task.
5. Having issues? check the `solution-for-variable-task.ipynb` file.

---

## Common mistakes

- Forgetting to activate `.venv` before installing packages (they go to your global Python instead)
- Running `python` in the wrong folder, which gives "file not found"
- Committing `.env` or `.venv/` to GitHub
- Using different Python versions in the terminal and VS Code. Check the interpreter selection.

---

## Checklist

- [ ] `python --version` shows 3.11+
- [ ] I can create and activate a virtual environment
- [ ] VS Code uses my `.venv` interpreter
- [ ] I pushed my first commit to GitHub
- [ ] `python hello_ai.py` runs without errors

**Next:** Part 01, Python basics.
