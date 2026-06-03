from google import genai 
from google.genai import types


client = genai.Client()

def askGemini(prompt):

    response = client.models.generate_content(
            model='gemini-3.1-flash-lite',
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.0
                )
            )

    return response.text


