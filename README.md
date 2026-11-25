# AI Git Committer Agent

An automated CLI tool powered by Python, n8n, and DeepSeek AI that inspects local Git changes, groups modified files into logical **atomic commits**, generates semantic commit messages following the **Conventional Commits** standard, and automatically commits and pushes them to your remote repository.

---

## Features

- **Automated Git Inspection:** Captures `git status`, `git diff`, and recent `git log` history to provide full context to the AI.
- **Atomic Commit Grouping:** Splits unrelated changes into separate, logical commits instead of a single generic commit.
- **Conventional Commits Enforcement:** Strictly follows standard prefixes (`feat`, `fix`, `docs`, `refactor`, `chore`, `style`) with imperative titles and structured bullet-point bodies.
- **n8n + LLM Integration:** Connects to an n8n workflow using **DeepSeek** (`deepseek-flash`) with conversation memory per project and a Structured Output Parser.
- **Hands-Free Execution:** Automatically stages (`git add`), commits (`git commit`), and pushes (`git push origin main`) the generated changes.

---

## Project Structure

```text
├── src/
│   ├── api.py              # Handles HTTP POST requests to the n8n webhook
│   ├── cmd.py              # Executes Git commands (status, diff, add, commit) via subprocess
│   └── system_message.txt  # System prompt defining atomic commit rules and project context
├── main.py                 # Main entry point orchestrating inspection, AI request, and Git execution
├── n8n-workflow.json       # Exported n8n workflow (Webhook + DeepSeek AI Agent + Output Parser)
├── .env                    # Environment variables (target repo path and webhook URL)
└── README.md               # Project documentation
```

---

## Prerequisites
- Python 3.10+
- Git installed and configured in your terminal
- n8n instance (self-hosted or cloud) with a DeepSeek API credential configured
- ngrok (or similar tunnel) if running n8n locally

---

## Installation & Setup
Clone the repository & install dependencies

```bash
git clone <your-repository-url>
cd <your-repository-folder>
pip install -r requirements.txt
```

---

## Configure the n8n Workflow
1. Open your n8n dashboard and create a new workflow.
2. Import the n8n-workflow.json file included in this repository.
3. Open the DeepSeek node and select/add your DeepSeek API credentials.
4. Activate the workflow and copy the Webhook URL from the Webhook node.

---

## Customize Project Context (Optional)
Edit src/system_message.txt to update the <contexto_do_projeto> tag so the AI understands the specific tech stack and architecture of your target repository.

## Usage
Once you have made changes to your target repository, simply run:

```bash
python main.py
```