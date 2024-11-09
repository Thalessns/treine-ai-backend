import json

from sqlalchemy import insert, select
from typing import List
from uuid import uuid4

from src.database.utils import database
from src.database.treino.schemas import Treino, SalvarTreino, SelecionarUsuario
from src.database.treino.tables import treino_table
from src.llm.schemas import NovoTreino
from src.database.treino.exceptions import UsuarioSemTreino


class TreinoService:
    
    async def criar_treino(self, data: SalvarTreino) -> None:
        insert_query = insert(treino_table).values(
            codigo = uuid4(),
            usuario = data.usuario,
            treino = data.treino.model_dump_json()
        )
        await database.execute(insert_query)

    async def selecionar_treinos_usuario(self, data: SelecionarUsuario) -> List[Treino]:
        select_query = select(treino_table).where(treino_table.usuario==data.usuario)
        treinos = await database.fetch_all(select_query)
        if treinos is None:
            raise UsuarioSemTreino
        result = list()
        for treino in treinos:
            treino["treino"] = NovoTreino(**json.loads(treino["treino"]))
            result.append(Treino(**treino))
        return result


treino_service = TreinoService()

{
    "objetivo": "Perda de peso",
    "periodizacao": {
        "semana_1-4": {
            "Repetições": "8-12"
        },
        "semana_5-8": {
            "Repetições": "6-8"
        },
        "semana_9-12": {
            "Repetições": "4-6"
        },
        "semana_13-16": {
            "Repetições": "8-12"
        },
        "semana_17-20": {
            "Repetições": "6-8"
        },
        "semana_21-24": {
            "Repetições": "4-6"
        },
        "semana_25-26": {
            "Repetições": "8-12"
        }
    },
    "treino": {
        "dia_1": {
            "Peito": [
                {
                    "Exercício": "Supino Inclinado",
                    "Séries": 3
                },
                {
                    "Exercício": "Crucifixo Inclinado",
                    "Séries": 3
                },
                {
                    "Exercício": "Flexões Inclinadas",
                    "Séries": 3
                }
            ],
            "Tríceps": [
                {
                    "Exercício": "Triceps Testa",
                    "Séries": 3
                },
                {
                    "Exercício": "Extensões de Tríceps",
                    "Séries": 3
                }
            ]
        },
        "dia_2": {
            "Costas": [
                {
                    "Exercício": "Puxada Alta",
                    "Séries": 3
                },
                {
                    "Exercício": "Remada Curvada",
                    "Séries": 3
                },
                {
                    "Exercício": "Remada Baixa",
                    "Séries": 3
                }
            ],
            "Biceps": [
                {
                    "Exercício": "Rosca Direta",
                    "Séries": 3
                },
                {
                    "Exercício": "Rosca Inversa",
                    "Séries": 3
                },
                {
                    "Exercício": "Rosca Concentrada",
                    "Séries": 3
                }
            ]
        },
        "dia_3": {
            "Pernas": [
                {
                    "Exercício": "Agachamento Livre",
                    "Séries": 3
                },
                {
                    "Exercício": "Leg Press",
                    "Séries": 3
                },
                {
                    "Exercício": "Extensão de Quadríceps",
                    "Séries": 3
                },
                {
                    "Exercício": "Flexora de Joelho",
                    "Séries": 3
                }
            ],
            "Ombros": [
                {
                    "Exercício": "Elevação Lateral",
                    "Séries": 3
                },
                {
                    "Exercício": "Elevação Frontal",
                    "Séries": 3
                },
                {
                    "Exercício": "Remada Alta",
                    "Séries": 3
                }
            ]
        },
        "dia_4": {
            "Descanso": []
        },
        "dia_5": {
            "Abdomen": [
                {
                    "Exercício": "Abdominal Supino",
                    "Séries": 3
                },
                {
                    "Exercício": "Abdominal Invertido",
                    "Séries": 3
                },
                {
                    "Exercício": "Prancha",
                    "Séries": 3
                }
            ],
            "Panturrilhas": [
                {
                    "Exercício": "Panturrilha em pé",
                    "Séries": 3
                },
                {
                    "Exercício": "Panturrilha sentada",
                    "Séries": 3
                }
            ]
        }
    },
    "cardio": {
        "dia_1": {
            "Exercício": "Esteira ou Bicicleta",
            "Tempo": "30 minutos",
            "Intensidade": "Moderada"
        },
        "dia_2": {
            "Exercício": "Natação",
            "Tempo": "30 minutos",
            "Intensidade": "Moderada"
        },
        "dia_3": {
            "Exercício": "Caminhada rápida",
            "Tempo": "30 minutos",
            "Intensidade": "Moderada"
        },
        "dia_4": {
            "Exercício": "Descanso",
            "Tempo": "0 minutos",
            "Intensidade": "N/A"
        },
        "dia_5": {
            "Exercício": "Elíptico",
            "Tempo": "30 minutos",
            "Intensidade": "Moderada"
        }
    }
}