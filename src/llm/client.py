from httpx import AsyncClient

from src.llm.config import settings
from src.llm.constants import Prompts


class Client:

    client = AsyncClient(verify=False)


    async def request_gemini(self) -> None:
        try:
            response = await self.client.post(
                url=settings.GEMINI_ENDPOINT,
                params={"key": settings.GEMINI_API_KEY},
                json={"contents":[{"parts":[{"text": Prompts.TESTE}]}]},
                headers={"Content-Type": "application/json"}
            )
            return response.json()
        except Exception as error:
            print(f"Erro ao fazer requisição ao Gemini: {error}")


client = Client()