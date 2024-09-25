
TEMPERATURA_PROMPT = "Contexto: Es una prueba de 40 preguntas para determinar el temperamento de las personas, ya sea sanguineo, colérico, flemático o melancólico. Puedes generar un reporte que sea ameno en base a los siguientes resultados: "
TEMPERATURA_PROMPT_PARTE_2 = ", haciendo énfasis en los temperamentos con los 2 valores más altos"

def build_prompt(resultados):
    return TEMPERATURA_PROMPT + resultados + TEMPERATURA_PROMPT_PARTE_2 + ' convierte to respuesta en html, utiliza h3 para los titulos';