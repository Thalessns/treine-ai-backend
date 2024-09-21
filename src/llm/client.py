from httpx import AsyncClient
from typing import List, Dict, Any

from src.llm.config import settings
from src.llm.schemas import CriarTreino
from src.llm.utils import format_prompt, get_response_content
from src.llm.exceptions import RequestException


class Client:

    client = AsyncClient(verify=False)


    async def request_gemini(self, data: CriarTreino, prompt: List[str]) -> Dict[str, Any]:
        try:
            response = await self.client.post(
                url=settings.GEMINI_ENDPOINT,
                params={"key": settings.GEMINI_API_KEY},
                json={"contents":[{"parts":[{"text": format_prompt(data, prompt)}]}]},
                headers={"Content-Type": "application/json"}
            )
            return get_response_content(response.json())
        except Exception as error:
            raise RequestException(detail=f"Erro ao fazer requisição ao Gemini: {error}")


client = Client()