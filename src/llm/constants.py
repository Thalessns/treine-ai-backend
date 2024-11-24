
class Prompts:

    CRIAR_TREINO = [
        """
            Crie um cronograma de treino considerando as seguintes informações:
                objetivo: {objetivo}
                sexo: {sexo}
                idade: {idade}
                peso (kg): {peso}
                altura (cm): {altura}
                local de treino: {local_treino}
                horas para treinar (dia): {horas_max_treino}
                dias para treinar (por semana): {dias_max_treino}
                meses treinando: {total_meses_treino}
        """,
        """
            Este cronograma deve conter as informações da periodização e dos exercícios de cada dia de treino.
            Seguindo os campos principais: "objetivo", "periodizacao", "treino" e "cardio". 
            No campo de "Periodização", os objetos devem ser separados em semanas e dentro destes objetos irá conter a quantidade de repetições dos exercícios. Dentro do campo "Treino", os objetos devem ser separados por dia e o grupamento muscular a ser trabalhado e dentro dos objetos terá o nome do exercício e a quantidade de séries a serem feitas por cada exercício.
            Siga o seguinte exemplo e CERTIFIQUE-SE DE RETORNAR SEM FORMATAÇÃO VISUAL: 
            {
                "objetivo": "...",
                "treino": {
                    "dia_1": {
                        "musculo_1": {
                            "exercicio_1": {
                                "series": "x",
                                "repeticoes: "Entre x e y"
                            },
                            "exercicio_n": {
                                "series": "x",
                                "repeticoes: "Entre x e y"
                            }
                        },
                        "musculo_n":{
                            "exercicio_1": {
                                "series": "x",
                                "repeticoes: "Entre x e y"
                            },
                            "exercicio_n": {
                                "series": "x",
                                "repeticoes: "Entre x e y"
                            }
                        },
                        "cardio":{
                            "intensidade": "baixa, moderada ou alta",
                            "duracao": "x minutos"
                        }
                    },
                    "dia_2": {
                        "musculo_1": {
                            "exercicio_1": {
                                "series": "x",
                                "repeticoes: "Entre x e y"
                            },
                            "exercicio_n": {
                                "series": "x",
                                "repeticoes: "Entre x e y"
                            }
                        },
                        "musculo_n":{
                            "exercicio_1": {
                                "series": "x",
                                "repeticoes: "Entre x e y"
                            },
                            "exercicio_n": {
                                "series": "x",
                                "repeticoes: "Entre x e y"
                            }
                        },
                        "cardio":{
                            "intensidade": "baixa, moderada ou alta",
                            "duracao": "x minutos"
                        }
                    },
                    "dia_n": {
                        "musculo_1": {
                            "exercicio_1": {
                                "series": "x",
                                "repeticoes: "Entre x e y"
                            },
                            "exercicio_n": {
                                "series": "x",
                                "repeticoes: "Entre x e y"
                            }
                        },
                        "musculo_n":{
                            "exercicio_1": {
                                "series": "x",
                                "repeticoes: "Entre x e y"
                            },
                            "exercicio_n": {
                                "series": "x",
                                "repeticoes: "Entre x e y"
                            }
                        },
                        "cardio":{
                            "intensidade": "baixa, moderada ou alta",
                            "duracao": "x minutos"
                        }
                    }
                }
                
            }
            Retorne SOMENTE em JSON SEM FORMATAÇÂO VISUAL.
        """
    ]
    