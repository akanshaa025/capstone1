import os
from langchain_ollama import ChatOllama
import json

from component_agent import generate_component
from styling_agent import improve_styling

llm = ChatOllama(
    model="qwen3:8b",
    temperature=0,
    base_url=os.environ.get("OLLAMA_BASE_URL", "http://127.0.0.1:11434"),
)


SYSTEM = """
You are a UI Architect.

Given a page request,
produce a JSON specification.

Only output JSON.

Example

{
  "components":[
      {
        "name":"Navbar",
        "description":"responsive navbar"
      },
      {
        "name":"Hero",
        "description":"hero section"
      }
  ]
}
"""


def build_page(user_request):

    response = llm.invoke(
        [
            ("system", SYSTEM),
            ("human", user_request),
        ]
    )

    plan = json.loads(response.content)

    completed = []

    for component in plan["components"]:

        jsx = generate_component(
            component["description"]
        )

        styled = improve_styling(jsx)

        completed.append(
            {
                "name": component["name"],
                "code": styled,
            }
        )

    return completed
