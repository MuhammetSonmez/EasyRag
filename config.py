from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    VECTOR_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    OLLAMA_MODEL: str = "gemma3:1b"
    CHUNK_SIZE: int = 200
    CHUNK_OVERLAP: int = 20
    WEBSOCKET_URL: str = "/ws"
    API_PREFIX: str = "/api"
    HUGGINGFACE_TOKEN: str


    class Config:
        env_file = ".env"

settings = Settings()
