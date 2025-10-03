from fastapi import HTTPException
from pydantic import BaseModel, StringConstraints, field_validator
from services.chat_service import ChatService
from typing import Annotated
from uuid import UUID

class ChatRequest(BaseModel):
    prompt: Annotated[str, StringConstraints(min_length=1, max_length=1000)]
    conversationId: UUID

    @field_validator("prompt")
    def strip_prompt(cls, v: str):
        v = v.strip()  
        if len(v) < 1:
            raise ValueError("Prompt cannot be empty.")
        return v

class ChatController:
    @staticmethod
    def sendMessage(req: ChatRequest):
        try:
            response = ChatService.sendMessage(req.prompt, req.conversationId)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error: {e}")
        return {"response": response.message}
