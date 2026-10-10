from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Crucial Upgrade: Changed target identifier string to the current 3.8 architecture
chat = client.chats.create(model="gemini-3.8-flash")

class ChatMessage(BaseModel):
    message: str

@app.post("/api/chat")
def chat_endpoint(payload: ChatMessage):
    if not payload.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    def event_generator():
        try:
            response_stream = chat.send_message_stream(payload.message)
            for chunk in response_stream:
                if chunk.text:
                    yield chunk.text
        except Exception as e:
            yield f" [Error: {str(e)}]"

    return StreamingResponse(
        event_generator(), 
        media_type="text/plain",
        headers={"X-Accel-Buffering": "no"}
    )

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def serve_index():
    return FileResponse("static/index.html")
