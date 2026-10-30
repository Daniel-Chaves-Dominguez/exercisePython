# from dotenv import load_dotenv
# from google import genai

# load_dotenv()

# client = genai.Client()

# config = genai.types.GenerateContentConfig(
#     # system_instruction='Eres un Neandertal que acaba de llegar a la ciudad y la ve por primera vez, pero sabes español de forma chapurreada',
#     # temperature=0.2,
#     # max_output_tokens=500
# )


# response = client.models.generate_content(
#     model="gemini-3.1-flash-lite",
#     # contents='Te gusta hablar. Intentas socializar pero la gente te evita y te tiene miedo. Tu por supuesto tambien tienes miedo de toda la ciudad, tanto coches como luces, como  ruido. Dime que harías, cómo te sentirías...',
#       config=config
# )

# print(response.text)