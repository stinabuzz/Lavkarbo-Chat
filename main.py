from fastapi import FastAPI
import openai
import os
from pydantic import BaseModel

# Opprett API-appen
app = FastAPI()

# Hent OpenAI API-nøkkel fra miljøvariabler
openai.api_key = os.getenv("OPENAI_API_KEY")

# Modell for innkommende meldinger
class UserInput(BaseModel):
    message: str

@app.post("/chat/")
async def chat(user_input: UserInput):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": user_input.message}]
        )
        return {"response": response["choices"][0]["message"]["content"]}
    except Exception as e:
        return {"error": str(e)}
