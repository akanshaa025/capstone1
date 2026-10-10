# AI Multi-Agent Development System 

An end-to-end, multi-agent artificial intelligence workflow that transforms a simple project idea into generated, styled, and reviewed UI code. 

Built entirely for **local CPU inference** using Ollama, this system leverages specialized small language models (SLMs) and Retrieval-Augmented Generation (RAG) to ensure fast, accurate, and framework-compliant code generation for both React (with Tailwind & shadcn/ui) and plain HTML/CSS/JS.

##  Features

* **100% Local & Private:** Powered by local models via Ollama (Qwen, Phi-4, Nomic). No API keys or cloud dependencies required.
* **Agentic Workflow:** Divides the complex task of software creation across specialized AI agents (Planner, Architect, Coder, Stylist, Reviewer, Package Manager).
* **RAG-Powered Accuracy:** Uses ChromaDB to ground code generation in actual documentation for React, Tailwind, and shadcn/ui, minimizing hallucinations.
* **CPU-Optimized Model Routing:** dynamically assigns tasks to appropriately sized models (e.g., 1.5b for styling, 3b for coding) to maximize speed without needing a massive GPU.
* **Auto-Execution:** Not only writes code but automatically installs required dependencies (`npm` or `pip`) using a secure terminal agent.
* **Parallel UI Generation:** Generates multiple React components simultaneously using multi-threading.
* **Self-Contained Outputs:** Packages every generation run into clean, timestamped project directories.

##  The Agent Workflow

1. **Clarification Agent** (`clarification.py`): Chats with you to gather requirements until it has enough context to build the software.
2. **Planner Agent** (`planneragent.py`): Acts as a senior architect, taking the requirements and drafting a comprehensive Markdown blueprint (features, routes, data models).
3. **Package Manager Agent** (`package_manager_agent.py`): Scans the plan, identifies necessary libraries, and safely executes terminal commands to install them.
4. **UI Architect Agent** (`ui_architectagent.py`): Breaks the project plan down into a JSON specification of individual components.
5. **Component & Styling Agents** (`component_agent.py`, `styling_agent.py`): 
   * **React Mode:** Queries the local RAG database for specific component docs, generates JSX, and refines it with Tailwind.
   * **HTML Mode:** Generates semantic HTML, CSS, and Vanilla JS in a unified structure without RAG overhead.
6. **Reviewer Agent** (`reviewer.py`): Inspects the generated code for syntax errors, missing imports, and bugs, outputting a final QA report.

## 🛠️ Prerequisites

* **Python 3.10+**
* **Ollama** installed and running locally (`http://127.0.0.1:11434`)
* **Required Local Models:** Pull the following models via Ollama:
  ```bash
  ollama pull qwen3:1.7b
  ollama pull phi4-mini
  ollama pull qwen2.5-coder:3b
  ollama pull qwen2.5-coder:1.5b
  ollama pull nomic-embed-text
  ```

##  Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ai-multi-agent-dev-system.git
   cd ai-multi-agent-dev-system
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the Knowledge Base (RAG):**
   Place your framework documentation markdown files inside the `rag_sources/` directory (e.g., `react.dev`, `tailwindcss.com`, `ui/apps/v4/content/docs`), then run the ingestion script to populate the local ChromaDB vector store:
   ```bash
   python ingest_docs.py
   ```

##  Usage

Start the main orchestrator:

```bash
python main.py
```

1. **Chat:** The terminal will prompt you. Describe what you want to build (e.g., "I need a personal portfolio website with a dark mode hero section and a contact form").
2. **Confirm:** Answer the clarification agent's questions. Once it confirms the requirements, type "yes" to proceed.
3. **Watch:** The system will automatically plan, install dependencies, generate components, and review the code.
4. **Collect:** Find your finished project, complete with code files, project plan, and review notes, inside the `generated_projects/` directory under a newly created timestamped folder.

## 📁 Project Structure

```text
├── main.py                  # Main orchestrator script
├── llm_factory.py           # Model routing and instantiation logic for Ollama
├── rag.py                   # Vector search and RAG retrieval helper
├── ingest_docs.py           # ChromaDB document embedding pipeline
├── utils.py                 # LangChain helpers, JSON extraction, retry logic
├── terminal_agent.py        # LangChain tool for terminal command execution
├── requirements.txt         # Python dependencies
├── *agent.py                # Individual AI agent logic files
├── chroma_db/               # Local vector database storage (generated)
└── generated_projects/      # Output directory for generated code (generated)
```

## 🏗️ Technologies Used

* **LangChain:** Framework for orchestrating LLM chains and tools.
* **Ollama:** Local model runner.
* **ChromaDB:** Local vector database for Retrieval-Augmented Generation.
* **Python `concurrent.futures`:** For parallelizing UI component generation.
* **Regex & AST parsing:** For robust JSON and code-block extraction from SLM outputs.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
