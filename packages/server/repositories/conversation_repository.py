conversations = {}
class conversationRepository:
    @staticmethod
    def getLastResponseId(conversationId: str):
        return conversations.get(conversationId)
    
    @staticmethod
    def setLastResponseId(conversationId: str, responseId: str):
        conversations[conversationId] = responseId
