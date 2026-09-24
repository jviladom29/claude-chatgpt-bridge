import os
from fastapi import FastAPI
from openai import OpenAI

app = FastAPI()
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

@app.get("/")
def home():
    return {"status": "Claude-ChatGPT bridge running"}

@app.post("/chat")
def chat(data: dict):
    response = client.responses.create(
        model="gpt-5",
        input=data.get("message", "")
    )
    return {"response": response.output_text}