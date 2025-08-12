from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
import os

class SimpleAgent:
    """
    Agente básico que usa LangChain para conectarse a OpenAI
    Esta es la versión más simple posible para probar la integración
    """
    
    def __init__(self):
        """
        Inicializar el agente con LangChain + OpenAI
        """
        # Verificar que tenemos la API key
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY no encontrada en variables de entorno")
        
        # Crear el modelo LLM usando LangChain
        self.llm = ChatOpenAI(
            model="gpt-3.5-turbo",  # Modelo más barato para testing
            temperature=0.7,
            api_key=api_key
        )
        
    async def process_message(self, message: str) -> str:
        """
        Procesar un mensaje enviándolo al LLM y devolviendo la respuesta
        
        Args:
            message: El mensaje del usuario
            
        Returns:
            str: La respuesta del LLM
        """
        try:
            # Crear el mensaje usando LangChain
            human_message = HumanMessage(content=message)
            
            # Enviar al LLM y obtener respuesta
            response = await self.llm.ainvoke([human_message])
            
            # Extraer el contenido de la respuesta
            return response.content
            
        except Exception as e:
            return f"Error procesando mensaje: {str(e)}"
