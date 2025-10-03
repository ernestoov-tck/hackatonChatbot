from .azure_model import AzureOpenAiModel
from .prompt_manager import PromptManager


class ChatService:
    """
    Servicio que gestiona la comunicación entre el usuario y el modelo.
    """

    def __init__(self):
        self.model = AzureOpenAiModel().get_model()
        self.prompt_manager = PromptManager()

    def ask(self, question: str) -> str:
        """
        Envía una pregunta al modelo y devuelve la respuesta.
        """
        messages = self.prompt_manager.build_prompt(question)
        response = self.model.invoke(messages)
        return response.content
