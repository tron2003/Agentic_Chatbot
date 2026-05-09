
from pathlib import Path

PROJECT_STRUCTURE = {
    "backend": {
        "app": {
            "api": {
                "routes": [
                    "chat.py",
                    "health.py",
                    "documents.py"
                ],
                "middleware": [
                    "logging.py",
                    "auth.py",
                    "rate_limit.py"
                ],
                "dependencies": []
            },

            "core": [
                "config.py",
                "settings.py",
                "constants.py",
                "logger.py",
                "security.py"
            ],

            "schemas": [
                "api_schema.py",
                "graph_schema.py",
                "rag_schema.py",
                "tool_schema.py",
                "response_schema.py"
            ],

            "graph": {
                "nodes": [
                    "chat_node.py",
                    "rag_node.py",
                    "tool_node.py",
                    "response_node.py"
                ],

                "subgraphs": [],

                "__files__": [
                    "builder.py",
                    "state.py",
                    "router.py"
                ]
            },

            "services": {
                "llm": [
                    "base.py",
                    "vllm_service.py",
                    "ollama_service.py"
                ],

                "embeddings": [
                    "embedding_service.py"
                ],

                "retrieval": [
                    "retriever.py",
                    "reranker.py",
                    "compressor.py"
                ],

                "memory": [
                    "memory_service.py"
                ],

                "tools": [
                    "registry.py",
                    "filesystem_tools.py",
                    "git_tools.py"
                ],

                "mcp": {
                    "adapters": [],
                    "__files__": [
                        "client.py",
                        "registry.py"
                    ]
                }
            },

            "rag": {
                "ingestion": [
                    "loader.py",
                    "parser.py"
                ],

                "chunking": [
                    "chunker.py"
                ],

                "indexing": [
                    "indexer.py"
                ],

                "vectorstore": [
                    "pgvector_store.py",
                    "queries.py"
                ],

                "pipelines": [
                    "ingestion_pipeline.py",
                    "retrieval_pipeline.py"
                ]
            },

            "database": {
                "repositories": [],
                "migrations": [],

                "__files__": [
                    "postgres.py",
                    "session.py",
                    "models.py"
                ]
            },

            "prompts": [
                "system.txt",
                "router.txt",
                "rag.txt",
                "tool_calling.txt"
            ],

            "observability": [
                "tracing.py",
                "metrics.py",
                "monitoring.py",
                "langsmith.py"
            ],

            "utils": [
                "helpers.py",
                "validators.py",
                "tokenizer.py",
                "formatting.py"
            ],

            "__files__": [
                "main.py"
            ]
        },

        "tests": {
            "unit": [],
            "integration": [],
            "e2e": []
        },

        "docker": {
            "backend": [],
            "postgres": [],
            "vllm": []
        },

        "scripts": [
            "ingest_docs.py",
            "create_embeddings.py",
            "reset_db.py"
        ],

        "data": {
            "documents": [],
            "uploads": []
        },

        "config": [
            "config.yaml",
            "params.yaml",
            "tools.yaml"
        ],

        "__files__": [
            ".env",
            ".env.example",
            "docker-compose.yml",
            "requirements.txt",
            "pyproject.toml",
            "README.md"
        ]
    }
}


def create_structure(base_path: Path, structure: dict):
    for name, content in structure.items():

        if name == "__files__":
            for file_name in content:
                file_path = base_path / file_name
                file_path.parent.mkdir(parents=True, exist_ok=True)

                if not file_path.exists():
                    file_path.touch()

            continue

        current_path = base_path / name
        current_path.mkdir(parents=True, exist_ok=True)

        init_file = current_path / "__init__.py"

        if not init_file.exists():
            init_file.touch()

        if isinstance(content, dict):
            create_structure(current_path, content)

        elif isinstance(content, list):
            for item in content:

                if "." in item:
                    file_path = current_path / item

                    if not file_path.exists():
                        file_path.touch()

                else:
                    folder_path = current_path / item
                    folder_path.mkdir(parents=True, exist_ok=True)

                    nested_init = folder_path / "__init__.py"

                    if not nested_init.exists():
                        nested_init.touch()


if __name__ == "__main__":
    root = Path.cwd()

    create_structure(root, PROJECT_STRUCTURE)

    print("Production backend structure created successfully.")
