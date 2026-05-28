from database import get_history
class Memory:
    def __init__(self):
        pass
    def get_context(self):
        history = get_history()
        context = ""
        for q,r in history:
            context += f"User: {q}\n Assistant: {r}\n"
            return context
    