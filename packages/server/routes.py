from controllers.chat_controller import ChatController, ChatRequest
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return "Hello World!"

@router.get("/api/hello")
async def hello():
    return {"message": "Hello World!"}

@router.post("/api/chat")
async def chat_endpoint(req: ChatRequest):
    return ChatController.sendMessage(req)
