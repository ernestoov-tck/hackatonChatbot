from os import getenv
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

load_dotenv()


class AzureOpenAiModel:
    def __init__(self):
        self.model = self._create_model()

    def _create_model(self) -> AzureChatOpenAI:
        """
        Crea e instancia el modelo AzureChatOpenAI con la configuración necesaria.
        """
        return AzureChatOpenAI(
            deployment_name=getenv('AZURE_OPENAI_DEPLOYMENT_NAME'),
            openai_api_version=getenv("OPENAI_API_VERSION"),
            azure_endpoint=getenv("AZURE_OPENAI_ENDPOINT"),
            openai_api_key=getenv("AZURE_OPENAI_API_KEY"),
            temperature=0.0,
            max_retries=3,
            verbose=True
        )

    def get_model(self) -> AzureChatOpenAI:
        """
        Devuelve la instancia del modelo.
        """
        return self.model
