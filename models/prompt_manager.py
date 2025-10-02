class PromptManager:
    """
    Maneja el prompt inicial y la construcción de mensajes para el modelo.
    """

    def __init__(self, initial_prompt: str = "Eres un asistente útil y experto en Python."):
        self.initial_prompt = initial_prompt

    def build_prompt(self, user_question: str) -> list:
        """
        Construye el historial de mensajes con el prompt inicial y la pregunta del usuario.
        """
        return [
            {"role": "system", "content": self.initial_prompt},
            {"role": "user", "content": user_question}
        ]
