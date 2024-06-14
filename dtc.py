import streamlit as st
st.title("IDEN")
csv_data = st.sidebar.file_uploader("Upload your Data", type="csv")
