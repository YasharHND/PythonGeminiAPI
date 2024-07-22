import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
FILE_PATH = "resources/Audio Test.mp3"

genai.configure(api_key=GOOGLE_API_KEY)

file = genai.upload_file(FILE_PATH)

model = genai.GenerativeModel(model_name="gemini-1.5-flash")
response = model.generate_content([file, "Provide the transcript of the audio from 00:11 to 00:19"])
print(response.text)
