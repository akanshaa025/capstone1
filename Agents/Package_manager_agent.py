from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
from terminal_agent import execute_terminal_command
from langchain_core.messages import SystemMessage

llm = ChatOllama(
    model="qwen3:8b",
    temperature=0,
)

SYSTEM_PROMPT = """
You are a Package Manager Agent.
Your responsibility is to determine required npm or python dependencies based on the user's project plan or code and execute installation commands in an isolated environment.
You MUST use the `execute_terminal_command` tool to run commands like `npm install <packages>` or `pip install <packages>`.
Do NOT explain your thought process to the user, just execute the commands and report success or failure.
"""

tools = [execute_terminal_command]
package_manager_executor = create_react_agent(llm, tools, prompt=SYSTEM_PROMPT)

def install_dependencies(requirements: str):
    print(f"--- Package Manager Agent is analyzing dependencies ---\n")
    response = package_manager_executor.invoke({"messages": [("user", requirements)]})
    return response["messages"][-1].content
