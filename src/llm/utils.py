import json

from pydantic import BaseModel
from typing import List, Dict, Any


def format_prompt(data: BaseModel, prompt: List[str]) -> str:
    prompt_info = prompt[0].format(**data.model_dump())
    return prompt_info + prompt[1]


def get_response_content(response: dict) -> Dict[str, Any]:
    content = response.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
    return json.loads(content)
