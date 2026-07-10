import os
from langchain_ollama import ChatOllama
from rag import retrieve_by_framework, build_context

llm = ChatOllama(
    model="qwen3:8b",
    temperature=0,
    base_url=os.environ.get("OLLAMA_BASE_URL", "http://127.0.0.1:11434"),
)


SYSTEM_PROMPT = """
You are a Senior React Component Engineer.

Your responsibility:

- Generate React components.
- Use React best practices.
- Use shadcn/ui whenever appropriate.
- Do NOT explain.
- Return ONLY valid JSX/TSX.
"""


def generate_component(component_spec: str):

    react_docs = retrieve_by_framework(
        component_spec,
        "react",
        k=4,
    )

    shadcn_docs = retrieve_by_framework(
        component_spec,
        "shadcn",
        k=4,
    )

    context = build_context(
        react_docs + shadcn_docs
    )

    prompt = f"""
Documentation:

{context}

Task:

{component_spec}

Return only the component code.
"""

    response = llm.invoke(
        [
            ("system", SYSTEM_PROMPT),
            ("human", prompt),
        ]
    )

    content = response.content.strip()
    if content.startswith("```"):
        lines = content.split('\n')
        if len(lines) > 1 and lines[-1].strip() == "```":
            content = '\n'.join(lines[1:-1])

    return content
