from fastapi import FastAPI
from pydantic import BaseModel
from models.chat_service import ChatService
import uvicorn

app = FastAPI(title="Azure OpenAI API", version="1.0")

chat_service = ChatService()


class QuestionRequest(BaseModel):
    question: str


class AnswerResponse(BaseModel):
    answer: str


@app.post("/ask", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):
    """
    Recibe una pregunta y devuelve una respuesta usando Azure OpenAI.
    """
    answer = chat_service.ask(request.question)
    return AnswerResponse(answer=answer)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
