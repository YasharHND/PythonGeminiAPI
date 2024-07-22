import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
FILE_PATH = "resources/PARIS.jpg"

genai.configure(api_key=GOOGLE_API_KEY)

file = genai.upload_file(FILE_PATH, display_name="Paris Olympics")
print(f"Name: {file.name}, Display Name: {file.display_name}, URI: {file.uri}")

model = genai.GenerativeModel(model_name="gemini-1.5-flash")
response = model.generate_content([file, "Describe the image"])
print(response.text)
