# genai-production-rag

The following project is a **Production-Ready RAG (Retrieval-Augmented Generation) System**, which is the industry standard for creating AI applications that can chat with custom private data (like PDFs or internal databases).

---

## 1. Project Folder Structure

A professional structure ensures scalability and easy maintenance.

```text
genai-production-rag/
├── config/                  # Externalize model parameters & app settings
│   └── settings.yaml
├── data/                    # Local storage for docs and vector indexes
│   ├── input_docs/          # Place your PDFs/txt files here
│   └── vector_store/        # Persistent vector database files
├── src/
│   ├── core/                # Core logic: LLM and Embedding setup
│   │   ├── llm_factory.py
│   │   └── embedder.py
│   ├── services/            # Business logic for RAG
│   │   ├── ingestion_service.py
│   │   └── retrieval_service.py
│   └── utils/               # Helper functions
│       └── logger.py
├── tests/                   # Unit and integration tests
├── requirements.txt         # Project dependencies
├── .env                     # API Keys (OpenAI, Anthropic, etc.) - DO NOT COMMIT
├── main.py                  # API entry point (FastAPI)
└── app.py                   # UI entry point (Streamlit)
```

---

## 2. Core Tools & Tech Stack

- **Orchestration:** LangChain or LlamaIndex for connecting LLMs to data.
- **LLM:** OpenAI GPT-4 or Mistral 7B for generation.
- **Vector Database:** ChromaDB or FAISS for semantic search.
- **API Framework:** FastAPI for high-performance backends.
- **Frontend:** Streamlit for a quick, interactive UI.
- **Observability:** LangSmith or MLflow for tracking prompts and performance.