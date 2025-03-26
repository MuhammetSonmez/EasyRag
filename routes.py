from fastapi import APIRouter, UploadFile, File, HTTPException, WebSocket
from langchain_ollama import OllamaLLM
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from config import settings
from models import AskRequest, AskResponse
from services import RagService
from config import settings


router = APIRouter()
ollama = OllamaLLM(model=settings.OLLAMA_MODEL)

user_sessions = {}


@router.post(f"{settings.API_PREFIX}/create_rag")
async def create_rag(file: UploadFile = File(...)):
    text = RagService.extract_text(file)
    
    if not text.strip():
        raise HTTPException(status_code=400, detail="File content is empty or cannot be read.")

    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = text_splitter.create_documents([text])

    vector_db = FAISS.from_documents(split_docs, HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"))

    user_sessions["vector_db"] = vector_db

    return {"message": "RAG model successfully created"}


@router.websocket(settings.WEBSOCKET_URL)
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    vector_db = user_sessions.get("vector_db")
    
    while vector_db:
        data = await websocket.receive_text()
        docs = vector_db.similarity_search(data, k=3)
        context = "\n".join([doc.page_content for doc in docs])
        prompt = f"User question: {data}\n\nContext:\n{context}\n\nAnswer:"
        response = ""
        async for word in ollama.astream(prompt):
            response += word
            await websocket.send_text(word)


@router.post(f"{settings.API_PREFIX}/ask", response_model=AskResponse)
async def ask_question(data: AskRequest):
    vector_db = user_sessions.get("vector_db")
    if not vector_db:
        return {"response": "Please create a RAG model first."}

    docs = vector_db.similarity_search(data.question, k=3)
    context = "\n".join([doc.page_content for doc in docs])
    prompt = f"User question: {data.question}\n\nContext:\n{context}\n\nAnswer:"
    
    response = ollama.invoke(prompt)
    return {"response": response}
