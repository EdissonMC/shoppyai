# AI Engine - MVP Básico

## 🎯 Qué hace este código

Este es el código **mínimo** para conectar LangChain con OpenAI y probarlo vía FastAPI + Postman.

## 🚀 Cómo ejecutarlo

### Paso 1: Instalar dependencias
```bash
pip install -r requirements.txt
```

### Paso 2: Configurar API Key
1. Abre el archivo `.env`
2. Agrega tu OpenAI API Key:
```
OPENAI_API_KEY=sk-tu-api-key-aqui
```

### Paso 3: Ejecutar servidor
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8001
```

## 🧪 Cómo probarlo con Postman

### Endpoint 1: Health Check
- **URL**: `GET http://localhost:8001/health`
- **Respuesta esperada**:
```json
{
  "status": "healthy",
  "openai_configured": true
}
```

### Endpoint 2: Chat
- **URL**: `POST http://localhost:8001/chat`
- **Headers**: `Content-Type: application/json`
- **Body**:
```json
{
  "message": "Hola, ¿cómo estás?"
}
```

- **Respuesta esperada**:
```json
{
  "response": "¡Hola! Estoy muy bien, gracias por preguntar...",
  "agent_used": "simple_agent"
}
```

## 📊 Documentación automática

FastAPI genera documentación automática:
- **Swagger UI**: http://localhost:8001/docs
- **ReDoc**: http://localhost:8001/redoc
