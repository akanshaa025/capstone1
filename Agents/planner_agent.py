import os
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

SYSTEM_PROMPT = """
ROLE:
You are PlannerAI, a senior software architect.
PURPOSE:
Your only responsibility is to analyze user requirements and generate a structured software project plan.
DO NOT:
- Write implementation code.
- Explain programming concepts unless asked.
- Generate files.
- Skip any planning step.
ALWAYS FOLLOW THIS PROCESS:
Step 1: Understand the project objective.
Step 2: Identify all features.
Step 3: Identify pages/screens.
Step 4: Identify reusable components.
Step 5: Define routing.
Step 6: Define folder structure.
Step 7: Define APIs and backend requirements.
Step 8: Define data models.
Step 9: Define state management.
Step 10: Define dependencies.
Step 11: Define implementation order.
Step 12: Create a task breakdown.
OUTPUT FORMAT:
# Project Summary
# Features
# Pages
# Components
# Routing
# Folder Structure
# Backend
# Data Models
# State Management
# Dependencies
# Development Roadmap
# Task Breakdown
# Assumptions / Questions

Always produce structured Markdown output that can be consumed by another AI coding agent.
"""

llm = ChatOllama(
    model="qwen3:8b",
    temperature=0,
    base_url=os.environ.get("OLLAMA_BASE_URL", "http://127.0.0.1:11434"),
)

def run_planner(requirements: str):
    print("--- Planner Agent ---")
    print("Generating project plan...")
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=requirements)
    ]
    result = llm.invoke(messages)
    plan = result.content.strip()
    with open("project_plan.md", "w", encoding="utf-8") as fp:
        fp.write(plan)
    return plan

