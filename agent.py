import ollama
from config import MODEL
from tools import hospital_tool,rag_tool
from memory import Memory
from database import save_chat,create_table

class Agent:
    def __init__(self):
        create_table()
        self.memory=Memory()

    def think(self,user_input):
        prompt = f"""
        You are a helpful health expert.
        Decide:
        -hospital_tool(Doctor,fee,timimg,admission_charge)
        -rag_tool(disease,symptoms,treatment,medicine,prevention)
        -NONE(general health advice)

        Rules:
        1. Always answer in a concise and clear manner.
        2. Always provide accurate and up to date information.
        3. Reply in simple hindi and simple english language.
        4. Give advanced  health advice only
        
    

        Format:--
        Hindi:--
        English:--
        Action:-- hospital_tool
        Input:-- userquestion
    
        User: {user_input}

        """
        response = ollama.chat(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}]

        )
        return response["message"]["content"]
    def act(self,decision):
        if "hospital_tool" in decision:
            query=decision.split("Input:")[-1].strip()
            return hospital_tool(query)
        elif "rag_tool" in decision:
            query=decision.split("Input:")[-1].strip()
            return rag_tool(query)
        return "No Action"
    
    def respond(self,user_input,tool_result):
        context = self.memory.get_context()

        prompt= f"""
                 you are a helpful health Expert.
                 previous conversation : {context}
                 User: {user_input}
                 Tool Result: {tool_result}
                 Rules:
                 Reply In: Hindi and English
                 use past context if useful
                 give advanced health advice 
                 Format:
                 Hindi:--
                 English:--
                 """
        response= ollama.chat(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}])
        final_answer = response["message"]["content"]
        ## save chat
        save_chat(user_input,final_answer)
        return final_answer
    
    def run(self,user_input):
        decision=self.think(user_input)
        print("\n decision",decision)
        tool_result=self.act(decision)
        print("\n tool result",tool_result)
        final_answer=self.respond(user_input,tool_result)
        return final_answer




                 
