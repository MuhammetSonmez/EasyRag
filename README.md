# Custom Purpose RAG-Powered LLM

This project is a **Retrieval-Augmented Generation (RAG)** powered **LLM** application that generates responses for specific purposes using information from CSV files uploaded by users. **FastAPI** is used as the backend, and **Ollama** is used for running the model.

## Features
- **CSV Upload:** Users can upload custom CSV files to the system.
- **RAG Technique:** Generates answers by retrieving information from uploaded CSV data.
- **Small-Scale LLM Usage:** Lightweight and fast response generation model integration.
- **FastAPI Backend:** Supports fast and asynchronous API requests.
- **Ollama Integration:** Runs the model and generates responses.
- **WebSocket Support:** Enables real-time responses.

## Installation
### Requirements
- Python 3.9+
- FastAPI
- LangChain
- FAISS
- HuggingFace Embeddings

## Usage
### Starting the Server
```sh
python main.py
```

### API Endpoints
#### **1. Create RAG Model**
**Endpoint:** `POST {API_PREFIX}/create_rag`
- **Description:** Processes the uploaded CSV file and creates a vector database.
- **Input:** CSV file (UploadFile)
- **Output:** `{"message": "RAG model successfully created"}`

#### **2. Ask a Question**
**Endpoint:** `POST {API_PREFIX}/ask`
- **Description:** Returns a response generated using the created RAG model.
- **Input:** `{"question": "..."}` (JSON format)
- **Output:** `{"response": "..."}`

#### **3. Real-Time Query via WebSocket**
**Endpoint:** `WEBSOCKET {WEBSOCKET_URL}`
- **Description:** Used to receive real-time responses.
- **Input:** User's text message.
- **Output:** Response from the LLM model.

## Technical Details
- **LLM Management:** Runs an Ollama-based LLM model using `langchain_ollama`.
- **Vector Database:** Stores data using `FAISS` and vectorizes texts with `HuggingFaceEmbeddings`.
- **Text Splitting:** Uses `CharacterTextSplitter` to split texts into predefined sizes.
- **Real-Time Processing:** Implements WebSocket integration for instant responses.

## Development
- **Backend:** Developed using FastAPI.
- **Model:** Uses a small LLM and RAG technique.
- **Data Processing:** CSV data is processed with FAISS and HuggingFace Embeddings.

## Contributing
You can contribute to the project by submitting a pull request. For bug reports and improvement suggestions, please open an issue.

## License
This project is licensed under the MIT license.

![Ekran görüntüsü 2025-03-27 023525](https://github.com/user-attachments/assets/cebf545c-066a-4f6e-a70f-a142b6cfbcb7)
