from dotenv import load_dotenv
from repositories.conversation_repository import conversationRepository
from openai import OpenAI
from pathlib import Path
from pydantic import BaseModel
import os

script_dir = Path(__file__).parent  
chatbot_txt_path = (script_dir / "../prompts/chatbot.txt").resolve()
park_info_md_path = (script_dir / "../prompts/SilksongWorld.md").resolve()  
chatbot_template = chatbot_txt_path.read_text()
park_info_content = park_info_md_path.read_text()
instructions = chatbot_template.replace("{{parkInfo}}", park_info_content)

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
            instructions=instructions,
            input=prompt,
            temperature=0.2,
            max_output_tokens=1000,  
            previous_response_id=conversationRepository.getLastResponseId(conversationId),
        )

        conversationRepository.setLastResponseId(conversationId, response.id)

        return ChatResponse(id=response.id, message=response.output_text)

