import streamlit as st

with st.chat_message('user'):
    st.text('Hi')

with st.chat_message('assistant'):
    st.text('how can i help you?')
    
user_input=st.chat_input('Type here')
if user_input:
    with st.chat_message('user'):
          st.text(user_input)   