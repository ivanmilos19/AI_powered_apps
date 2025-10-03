from dotenv import load_dotenv
from repositories.conversation_repository import conversationRepository
from openai import OpenAI
from pydantic import BaseModel
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ChatResponse(BaseModel):
    id: str
    message: str

class ChatService:
    @staticmethod
    def sendMessage(prompt: str, conversationId: str) -> ChatResponse:
        response = client.responses.create(
            model="gpt-4o-mini",
            input=prompt,
            temperature=0.2,
            max_output_tokens=200,  
            previous_response_id=conversationRepository.getLastResponseId(conversationId),
        )

        conversationRepository.setLastResponseId(conversationId, response.id)

        return ChatResponse(id=response.id, message=response.output_text)

