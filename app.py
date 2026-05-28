import streamlit as st
from agent import Agent
st.sidebar.title("About")
st.sidebar.info("Health AI Expert")
st.set_page_config(page_title="Health AI Expert")
st.title("Health AI Expert")
st.write("Ask your health questions in Hindi or English")

## Initializwe Agent
if "agent" not in st.session_state:
    st.session_state.agent=Agent()
## chat history
if "messages" not in st.session_state:
    st.session_state.messages=[]

## Display old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
## User_Input
user_input=st.chat_input("Type your Health Question here")
if user_input:
    ## Show user message
    st.session_state.messages.append({"role":"user","content":user_input})
    with st.chat_message("user"):
        st.write(user_input)

## Agent Processing
decision=st.session_state.agent.think(user_input)
tool_result=st.session_state.agent.act(decision)
response=st.session_state.agent.respond(user_input,tool_result)
## Show Agent response
with st.chat_message("Health Expert"):
    st.write(response)
st.session_state.messages.append({"role":"Health Expert","content":response})