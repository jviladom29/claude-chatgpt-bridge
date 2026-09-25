import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from openai import OpenAI

app = FastAPI()

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


@app.get("/")
def home():
    return {"status": "Claude-ChatGPT bridge running"}


@app.post("/chat")
def chat(data: dict):
    message = data.get("message", "")

    response = client.responses.create(
        model="gpt-5",
        input=message
    )

    return JSONResponse({
        "response": response.output_text
    })