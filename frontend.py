#Setup UI with Streamlit(model provider, model, system_prompt, query)
import streamlit as st

st.set_page_config(page_title="Langgraph AI Agent UI", layout="wide")
st.title("AI Chatbot Agents")
st.write("Create and interact with AI Agents!")

system_prompt=st.text_area("Define your AI Agent:", height=70, placeholder="Type your system prompt here...")

MODEL_NAMES_GROQ = ["mixtral-8x7b-32768", "llama-3.3-70b-versatile"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider=st.radio("Select Model Provider", ("Groq", "OpenAI"))
if provider=="Groq":
    selected_model=st.selectbox("Select Model", MODEL_NAMES_GROQ)
else:
    selected_model=st.selectbox("Select Model", MODEL_NAMES_OPENAI)

allow_web_search=st.checkbox("Allow Web Search")

user_query=st.text_area("Enter your Query:", height=150, placeholder="Ask anything")

API_URL="http://127.0.0.1:8001/chat" 

if st.button("Ask Agent!"):
    if user_query.strip():
        #connect with backend via url

        import requests 

        payload={
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        response = requests.post(API_URL, json=payload)

        #get response from backend to show here
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"**Final Response:** {response_data['response']}")
        else:
            response = "Error: Unable to get a response from the AI Agent."

#