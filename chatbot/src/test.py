import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key="AIzaSyCXqtakywnasffVsdLWSObKuMtoLOkGGDI")

# List available models
for model in genai.list_models():
    print(model.name)
