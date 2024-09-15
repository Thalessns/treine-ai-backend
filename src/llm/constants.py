
class Prompts:

    CRIAR_TREINO = [
        """
            Crie um cronograma de treino para uma pessoa do sexo {sexo}, de {idade} anos, pesando {peso}kg e tendo {altura}cm de altura seguindo os seguintes requisitos: 
            O treino será feito em {local_treino}, durando {tempo_max_treino} hora(s) de musculação, {dias_max} dias na semana e considerando que a pessoa já treina a {tempo_total_treino} ano(s).
        """,
        """
            Este cronograma deve conter as informações da periodização e dos exercícios de cada dia de treino.
            Retorne SOMENTE em JSON SEM FORMATAÇÂO VISUAL, seguindo os campos principais: "Foco do treino", "Periodização"  e "Treino". No campo de "Periodização", os objetos devem ser separados em semanas e dentro destes objetos irá conter a quantidade de repetições dos exercícios. Dentro do campo "Treino", os objetos devem ser separados por dia e o grupamento muscular a ser trabalhado e dentro dos objetos terá o nome do exercício e a quantidade de séries a serem feitas por cada exercício.

            Siga este exemplo: 
            {
                "Foco do treino": "...",
                "Periodização": {
                    "Semana 1-2": {
                    },
                    "Semana 3-a": {
                    },
                    "Semana a-n": {
                    }
                }
                "Treino": {
                    "Dia 1": {
                    },
                    "Dia 2": {
                    },
                    "Dia n": {
                    }
                }
            }
        """
    ]
    