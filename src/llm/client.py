from httpx import AsyncClient, RequestError
from typing import List, Dict, Any
from json import JSONDecodeError

from src.llm.config import settings
from src.llm.schemas import CriarTreino, Teste
from src.llm.utils import Utils
from src.llm.exceptions import RequestException, ResponseException


class Client:

    client = AsyncClient(verify=False, timeout=10)

    async def request_gemini_treino(self, data: CriarTreino, prompt: List[str]) -> Dict[str, Any]:
        try:
            response = await self.client.post(
                url=settings.GEMINI_ENDPOINT,
                params={"key": settings.GEMINI_API_KEY},
                json={"contents":[{"parts":[{"text": Utils.format_prompt(data, prompt)}]}]},
                headers={"Content-Type": "application/json"}
            )
            content = Utils.get_response_content(response.json())
            if not content or not Utils.validate_new_workout(content):
                raise ResponseException()
            return content
        except RequestError as error:
            raise RequestException(
                detail=f"Erro ao fazer requisição ao Gemini: {error.__dict__}")
        except JSONDecodeError:
            ResponseException()

    async def request_gemini(self, data: Teste, prompt: List[str]) -> Dict[str, Any]:
        try:
            response = await self.client.post(
                url=settings.GEMINI_ENDPOINT,
                params={"key": settings.GEMINI_API_KEY},
                json={"contents":[{"parts":[{"text": Utils.format_prompt(data, prompt)}]}]},
                headers={"Content-Type": "application/json"}
            )
            content = Utils.get_response_content(response.json())
            if not content:
                raise ResponseException()
            return content
        except RequestError as error:
            raise RequestException(
                detail=f"Erro ao fazer requisição ao Gemini: {error.__dict__}")
        except JSONDecodeError:
            ResponseException()


client = Client()
