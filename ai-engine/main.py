from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from agents.simple_agent import SimpleAgent
import os

# Cargar variables de entorno
load_dotenv()

# Crear la aplicación FastAPI
app = FastAPI(
    title="AI Marketplace Engine - MVP",
    description="Versión mínima para probar LangChain + OpenAI",
    version="0.1.0"
)

# Modelo para el request del chat
class ChatRequest(BaseModel):
    message: str

# Modelo para la respuesta del chat
class ChatResponse(BaseModel):
    response: str
    agent_used: str

# Inicializar el agente simple
simple_agent = SimpleAgent()

@app.get("/")
async def root():
    """Endpoint básico para verificar que la API funciona"""
    return {"message": "AI Engine está funcionando!", "status": "ok"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "openai_configured": bool(os.getenv("OPENAI_API_KEY"))}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Endpoint principal para chat
    Recibe un mensaje y devuelve la respuesta del LLM
    """
    try:
        response = await simple_agent.process_message(request.message)
        return ChatResponse(
            response=response,
            agent_used="simple_agent"
        )
    except Exception as e:
        return ChatResponse(
            response=f"Error: {str(e)}",
            agent_used="error_handler"
        )

# Para correr con: uvicorn main:app --reload --host 0.0.0.0 --port 8001
