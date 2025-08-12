#!/bin/bash
# Script para instalar dependencias y ejecutar el servidor
echo "🚀 Instalando dependencias..."
pip install -r requirements.txt

echo "⚡ Iniciando servidor FastAPI..."
echo "📡 Servidor corriendo en: http://localhost:8001"
echo "📊 Documentación automática en: http://localhost:8001/docs"
echo "🔍 Para probar con Postman, usa: POST http://localhost:8001/chat"

uvicorn main:app --reload --host 0.0.0.0 --port 8001
