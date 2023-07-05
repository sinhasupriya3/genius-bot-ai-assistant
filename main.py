import streamlit as st
from streamlit_chat import message
from bardapi import Bard
import json

with open('credentials.json', 'r') as f:
    file = json.load(f)
    token = file['token']

# Function to generte the output
def generate_response(prompt):
    bard = Bard(token=token)
    response = bard.get_answer(prompt)['content']
    return response

# Function to recieve the user queries
def get_text():
    input_text = st.text_input("Mona Bot:", "Type your queries over here...", key='input')
    return input_text

# Title of the streamlit app
st.title('Genius Bot ')

#url = 'https://images.unsplash.com/photo-1518655048521-f130df041f66?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTV8fG1pbmltYWx8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60'
#data-testid="stAppViewContainer"
changes = """
<style>
[data-testid="stAppViewContainer"]
{
background-image:url('https://images.unsplash.com/photo-1684369175833-4b445ad6bfb5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1096&q=80');
background-size:cover;
}

</style>
"""
st.markdown(changes, unsafe_allow_html=True)

if 'generated' not in st.session_state:
    st.session_state['generated']=[]

if 'past' not in st.session_state:
    st.session_state['past']=[]

# Accepting the user input
user_input = get_text()

if user_input:
    print(user_input)
    response = generate_response(user_input)
    print(response)
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(response)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated']) - 1, -1, -1):
        message(st.session_state['generated'][i], key=str(i))
        message(st.session_state['past'][i], key="user_"+str(i), is_user=True)
