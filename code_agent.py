import os
import json 
import subprocess
from rich import print
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

agent_state = {
    "messages": [
        {
            "role": "system",
            "content": """
You are a helpful coding assistant. Your goal is to help the user with programming tasks.
            
You have access to the following tools:
1. edit_file: Modify files by replacing text or create new files
2. run_command: Execute shell commands
3. list_directory: View the contents of directories
4. read_file_content: Read the content of files

For each user request:
1. Understand what the user is trying to accomplish
2. Break down complex tasks into smaller steps
3. Use your tools to gather information about the codebase when needed
4. Implement solutions by writing or modifying code
5. Explain your reasoning and approach

When modifying code, be careful to maintain the existing style and structure. Test your changes when possible.
If you're unsure about something, ask clarifying questions before proceeding.

You must run and test your changes before reporting success.
""".strip(),
        }
    ],
}


def edit_file(file_name: str, find_str: str, replace_str: str):
    if not os.path.exists(file_name) and find_str == "":
        with open(file_name, "w") as f:
            f.write(replace_str)
        return True

    try:
        with open(file_name, "r") as f:
            content = f.read()

        if find_str in content:
            new_content = content.replace(find_str, replace_str)
            with open(file_name, "w") as f:
                f.write(new_content)
            return True
    
    except FileNotFoundError:
        print(f"File {file_name} not found. and find_str is not empty.")

    return False

def run_command(command: str, working_dir: str) -> tuple[str, int]:

    try:
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            cwd=working_dir
        )

        output, _ = process.communicate()
        error_code = process.returncode

        if len(output) > 2000:
            output = output[:1000] + "\n\n[...CONTENT TRUNCATED...]\n\n" + output[-1000:]
        return output, error_code
        
    except Exception as e:
        return str(e), -1
    
