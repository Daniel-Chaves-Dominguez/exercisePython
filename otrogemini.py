# import random
# import time

# from dotenv import load_dotenv
# from google import genai
# from google.genai.errors import APIError
# import numpy as np

# load_dotenv()

# client = genai.Client()

# #Esto del esquema es algo aparte para que nos de un JSON
# esquema = {
#     "type": "OBJECT",
#     "properties": {
#         "titulo": {
#             "type": "STRING",
#             "description": "Un resumen breve de la frase que tiene que analizar"
#         },
#         "sentimiento": {
#             "type": "STRING",
#             "enum": ["positivo", "negativo", "neutro"]
#         },
#         "puntuacion": {
#             "type": "INTEGER",
#             "description": "Puntuación del 0 al 10, donde 10 es lo más positivo"
#         }
#     },
#     "required": ["titulo", "sentimiento", "puntuacion"]
# }

# config = genai.types.GenerateContentConfig(
#     # Quitamos esto para lo del JSON
#     # system_instruction='Eres un Neandertal que acaba de llegar a la ciudad y la ve por primera vez, pero sabes español de forma chapurreada',
#     # temperature=0.2,
#     # max_output_tokens=500
#     response_schema=esquema,
#     response_mime_type='application/json'
# )

# def embed_content(text):
#     result = client.models.embed_content(
#         model='gemini-embedding-001',
#         content=text
#     )
#     return np.array(result.embeddings[0].values)

# def cosine_similarity(v1,v2):
#     return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

# cache = []
# threshold = 0.8

# def generate_retry_jitter(prompt, max_retries=5, base_delay=1):
#     for attempt in range(max_retries):
#         try:
#             prompt_vector = embed_content(prompt)
#             best_score = 0
#             best_match = None

#             for entry in cache:
#                 score = cosine_similarity(entry['vector'], prompt_vector)
#                 if score > best_score:
#                     best_score = score
#                     best_match = entry

#             if best_match and best_score >= threshold:
#                 print(f'¿¿COINCIDENCIA!! {best_score}')
#                 print(best_match['response'])
#                 return

#             print('NO COINCIDENCIA : (')
#             response = client.models.generate_content(
#                 model='gemini-3.1-flash-lite',
#                 contents=prompt,
#                 config=config
#             )



#             response = client.models.generate_content_stream(
#                 model="gemini-8-flash-lite",
#                 # contents='Te gusta hablar. Intentas socializar pero la gente te evita y te tiene miedo. Tu por supuesto tambien tienes miedo de toda la ciudad, tanto coches como luces, como  ruido. Dime que harías, cómo te sentirías...',
#                 contents='Analiza esta frase: Es el vecino el que elige al alcalde y es el alcalde el que quiere que sean los vecinos el alcalde ',
#                 config=config
#             )
#             print(response.text)
#             break
#         except APIError as e:
#             print(e)
#             delay = base_delay * (2 ** attempt)
#             jitter = random.uniform(0, delay)
#             sleep_time = delay + jitter
#             print(f'Durmiendo: {sleep_time}')
#             time.sleep(sleep_time)

# generate_retry_jitter('Analiza esta frase: Me encanta el módulo de IA')
# generate_retry_jitter('Analiza esta frase: Me apasiona mucho el módulo de inteligencia artificial')




# # for chunk in response:
# #     print(chunk.text, end='', flush=True)
