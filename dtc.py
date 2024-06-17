import streamlit as st
st.title("IDEN")

csv_data = st.sidebar.file_uploader("Upload your Data", type="csv")
if csv_data :
    st.write("Please wait for a time, your data is in processing stage")
    if 'user' not in st.session_state:
        st.session_state['user'] = ["Hey there"]

    if 'assistant' not in st.session_state:
        st.session_state['assistant'] = ["Hello I am IDEN and I am a new emmerging chatbot which was created by 3 college students Kailash.M,Praveen.S and Dinesh Babu.K.\nThe word IDEN stands for Interactive Data Exploration With NLP.\nIf you upload your csv file and ask question from it, I will provide answer to you.\nEven though I'm a text based bot i can do some basic visualization like bar char,pie chart etc" ]

    container = st.container()
    with container:
        with st.form(key='eda_form', clear_on_submit=True):

            user_input = st.text_input("", placeholder="Place Your Query here", key='input')
            submit = st.form_submit_button(label='Kick')

       

            
