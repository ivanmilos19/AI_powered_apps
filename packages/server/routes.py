from controllers.chat_controller import ChatController, ChatRequest
from fastapi import APIRouter
from controllers.reviews_controller import ReviewController

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


@router.get("/api/products/{id}/reviews")
async def reviews_endpoint(id: int):
    return await ReviewController.getReviews(id)
