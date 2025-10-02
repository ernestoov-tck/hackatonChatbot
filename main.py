from fastapi import FastAPI
from pydantic import BaseModel
from models.chat_service import ChatService

# Instancia de la API
app = FastAPI(title="Azure OpenAI API", version="1.0")

# Inicializamos el servicio con un prompt inicial
chat_service = ChatService(prompt="Eres un asistente experto en programación y Python.")


# Definimos los modelos de request/response
class QuestionRequest(BaseModel):
    question: str


class AnswerResponse(BaseModel):
    answer: str


# Endpoint principal
@app.post("/ask", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):
    """
    Recibe una pregunta y devuelve una respuesta usando Azure OpenAI.
    """
    answer = chat_service.ask(request.question)
    return AnswerResponse(answer=answer)


# Punto de entrada para ejecutar con uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
