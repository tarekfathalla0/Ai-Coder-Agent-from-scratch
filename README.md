# 🤖 AI Coding Agent (from Scratch)

An interactive **AI-powered coding assistant** built from scratch using LLMs and tool-calling.  
This agent can **read, modify, and execute code locally** while reasoning step-by-step to solve programming tasks.

---

## 🚀 Features

- 🧠 **LLM-powered reasoning loop**
- 🛠️ **Tool-based architecture**
- 📂 Read & explore project files
- ✏️ Edit existing files or create new ones
- ⚡ Execute shell commands
- 🔍 Inspect directories
- 🔐 User approval before critical actions
- 🔁 Iterative thinking (Agent loop)

---

## 🧩 Available Tools

The agent can use the following tools:

| Tool | Description |
|------|------------|
| `edit_file` | Modify or create files |
| `run_command` | Execute terminal commands |
| `list_directory` | View directory contents |
| `read_file_content` | Read file contents |

---

## 🏗️ How It Works

1. User provides a request
2. The agent:
   - Understands the task
   - Breaks it into steps
   - Calls tools when needed
3. Executes actions with **user approval**
4. Loops until the goal is achieved

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-coding-agent.git
cd ai-coding-agent
2. Install dependencies
pip install -r requirements.txt

Or manually:

pip install openai python-dotenv rich
3. Add your API Key

Create a .env file:

OPENROUTER_API_KEY=your_api_key_here
▶️ Run the Agent
python code_agent.py

Then type your request:

How can I help you?
> build a simple python calculator
🔐 Safety Features
Requires user confirmation before:
Editing files
Running shell commands
Prevents unintended system changes
🧠 Example Use Cases
Generate and modify code
Debug Python scripts
Explore unknown codebases
Automate development tasks
Build small projects interactively
⚠️ Limitations
Requires valid API key (OpenRouter)
May execute unsafe commands if approved blindly
Limited context window (~100 messages)
🛠️ Tech Stack
Python 🐍
OpenRouter API (LLM access)
Tool Calling (Function Calling)
Rich (CLI formatting)
📌 Future Improvements
Memory persistence
Multi-agent collaboration
GUI interface
Code diff visualization
Sandboxed execution
👨‍💻 Author

Built by Tarek Fathalla
AI Engineer | Agentic AI Enthusiast 🚀

⭐ Star This Repo

If you found this useful, give it a ⭐ on GitHub!