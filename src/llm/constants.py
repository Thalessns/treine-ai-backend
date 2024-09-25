
class Prompts:

    CRIAR_TREINO = [
        """
            Crie um cronograma de treino para uma pessoa do sexo {sexo}, de {idade} anos, pesando {peso}kg e tendo {altura}cm de altura seguindo os seguintes requisitos: 
            O treino será feito em {local_treino}, durando {horas_max_treino} hora(s) de musculação, {dias_max_treino} dias na semana e considerando que a pessoa já treina há {total_meses_treino} mes(es).
        """,
        """
            Este cronograma deve conter as informações da periodização e dos exercícios de cada dia de treino.
            Retorne SOMENTE em JSON SEM FORMATAÇÂO VISUAL, seguindo os campos principais: "Foco do treino", "Periodização"  e "Treino". No campo de "Periodização", os objetos devem ser separados em semanas e dentro destes objetos irá conter a quantidade de repetições dos exercícios. Dentro do campo "Treino", os objetos devem ser separados por dia e o grupamento muscular a ser trabalhado e dentro dos objetos terá o nome do exercício e a quantidade de séries a serem feitas por cada exercício.

            Siga este exemplo: 
            {
                "foco_do_treino": "...",
                "periodizacao": {
                    "semana_1-2": {
                    },
                    "semana_3-a": {
                    },
                    "semana_a-n": {
                    }
                }
                "treino": {
                    "dia_1": {
                    },
                    "dia_2": {
                    },
                    "dia_n": {
                    }
                }
            }
        """
    ]
    