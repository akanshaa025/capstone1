from langchain_ollama import ChatOllama
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from terminal_agent import execute_terminal_command

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

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

tools = [execute_terminal_command]

agent = create_tool_calling_agent(llm, tools, prompt)
package_manager_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

def install_dependencies(requirements: str):
    print(f"--- Package Manager Agent is analyzing dependencies ---\n")
    response = package_manager_executor.invoke({"input": requirements})
    return response["output"]
