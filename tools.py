import json
from rag import load_rag,rag_search

with open("hospital_data.json") as f:
    data=json.load(f)

db=load_rag()

def rag_tool(query):
    return rag_search(query,db)


def hospital_tool(query):
        query=query.lower()


## doctor information
        for doc in data["Doctor"]:

            if doc["Name"].lower() in query:
                
                return f"{doc['Name']}({doc['Specialization']}) -Timing:{doc['Timing']}-Fee:{doc['fee']}"
            
            ## Admission information
            if "admission" in query:
                return f"Admission charge is ₹{data['admission_charge']}"
            return "No Data Found"
