import os


class Config:
    # chromadb
    DOCUMENTS_DIR = "resumes"
    COLLECTION_NAME = "CVs"
    PERSISTENT_DIR = "data/chromadb"

    # Embeddings: "openai", "local" o "ollama"
    EMBEDDING_PROVIDER = "local"
    MODEL_NAME = "all-mpnet-base-v2"
    MODEL_PATH = "modelli/mio_modello"
    OPENAI_EMBEDDINGS_KEY = os.getenv("OPENAI_API_KEY")

    # Completamento (Ollama)
    LLM_MODEL = "llama3.2"
    LLM_MODEL_LOW = "llama3.2"
    AI_API_URL = "http://localhost:11434/v1"
    AI_API_KEY = "ollama"
    ### openai
    # LLM_MODEL = "gpt-4o"
    # LLM_MODEL_LOW = "gpt-4o-mini"
    # AI_API_URL = "https://api.openai.com/v1/"
    # AI_API_KEY = os.getenv("OPENAI_API_KEY")