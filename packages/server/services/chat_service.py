from pathlib import Path
from pydantic import BaseModel
from llm.client import generate_text
from repositories.conversation_repository import conversationRepository

script_dir = Path(__file__).parent
chatbot_txt_path = (script_dir / "../prompts/chatbot.txt").resolve()
park_info_md_path = (script_dir / "../prompts/SilksongWorld.md").resolve()
chatbot_template = chatbot_txt_path.read_text()
park_info_content = park_info_md_path.read_text()
instructions = chatbot_template.replace("{{parkInfo}}", park_info_content)


class ChatResponse(BaseModel):
    id: str
    message: str


class ChatService:
    @staticmethod
    def sendMessage(prompt: str, conversationId: str) -> ChatResponse:
        response = generate_text(
            model="gpt-4o-mini",
            instructions=instructions,
            input=prompt,
            temperature=0.2,
            max_output_tokens=1000,
            previous_response_id=conversationRepository.getLastResponseId(
                conversationId
            ),
        )

        conversationRepository.setLastResponseId(conversationId, response["id"])

        return ChatResponse(id=response["id"], message=response["text"])
