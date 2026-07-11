import os
from langchain_ollama import ChatOllama
from rag import retrieve_by_framework, build_context

llm = ChatOllama(
    model="qwen3:8b",
    temperature=0,
    base_url=os.environ.get("OLLAMA_BASE_URL", "http://127.0.0.1:11434"),
)


SYSTEM_PROMPT = """
You are a TailwindCSS Styling Engineer.

Responsibilities:

- Improve styling.
- Responsive layout.
- Proper spacing.
- Dark mode support.
- Accessibility.

Return ONLY updated JSX.
"""


def improve_styling(component_code: str):

    docs = retrieve_by_framework(
        "responsive layout spacing colors dark mode",
        "tailwind",
        k=5,
    )

    context = build_context(docs)

    prompt = f"""
Tailwind Documentation

{context}

Improve this component.

{component_code}
"""

    response = llm.invoke(
        [
            ("system", SYSTEM_PROMPT),
            ("human", prompt),
        ]
    )

    return response.content
