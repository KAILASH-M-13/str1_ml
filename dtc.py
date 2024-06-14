import streamlit as st
from streamlit_chat import message
st.title("IDEN")
csv_data = st.sidebar.file_uploader("Upload your Data", type="csv")
