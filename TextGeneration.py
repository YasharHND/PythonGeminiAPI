import os
import json
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

config = genai.GenerationConfig(response_mime_type="application/json",
                                response_schema=list[str])

model = genai.GenerativeModel(model_name="gemini-1.5-pro", generation_config=config)

response = model.generate_content("List 7 fun facts about olympics 2024")
responseJson = json.loads(response.text)
print(json.dumps(responseJson, indent=2))
