import json

from pydantic import BaseModel
from typing import List, Dict, Any

from src.llm.schemas import NovoTreino


class Utils:

    @classmethod
    def validate_new_workout(cls, response: Dict[str, Any]) -> bool:
        try:
            NovoTreino(**response)
            return True
        except Exception:
            return False

    @classmethod
    def format_prompt(cls, data: BaseModel, prompt: List[str]) -> str:
        prompt_info = prompt[0].format(**data.model_dump())
        return prompt_info + prompt[1]

    @classmethod
    def get_response_content(cls, response: dict) -> Dict[str, Any]:
        content = response.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
        return json.loads(content)
