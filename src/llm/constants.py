
class Prompts:

    TESTE = """ Quero saber quais foram os últimos 5 Presidentes do Brasil.
                Responda EXATAMENTE em JSON no seguinte formato, sem a formatação visual:
                {"presidentes":
                    [
                        {"nome": ..., "ano_eleito": ...},
                        {"nome": ..., "ano_eleito": ...},
                        ...
                        {"nome": ..., "ano_eleito": ...}
                    ]
                }
            """