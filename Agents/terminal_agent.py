import subprocess
from langchain.tools import tool

@tool
def execute_terminal_command(command: str) -> str:
    """
    Executes a shell command on the terminal and returns the output.
    Useful for installing packages, creating directories, and running tests.
    """
    try:
        result = subprocess.run(
            command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        return result.stdout if result.stdout else "Command executed successfully with no output."
    except subprocess.CalledProcessError as e:
        return f"Error executing command:\nSTDOUT: {e.stdout}\nSTDERR: {e.stderr}"
