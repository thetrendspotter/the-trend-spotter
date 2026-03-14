from fastapi import FastAPI
import torch

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Trend Spotter AI Backend is Running"}

@app.post("/generate-video")
async def generate_video(prompt: str):
    # Yahan hum Stable Diffusion aur Voice Cloning ka logic add karenge
    return {"message": f"AI Video for {prompt} is being generated..."}

