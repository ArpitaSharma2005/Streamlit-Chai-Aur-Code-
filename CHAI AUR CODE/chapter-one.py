import streamlit as st

st.title("Hello!!! PROGRAMMER")
st.subheader("Brewed with Streamlit")
st.text("Welcome to Code-World")
st.write("Choose your favorite Language")

LANG = st.selectbox("Your fav Languages: ", ["JAVA","JAVA-SCRIPT","PYTHON","C++"])

st.write(f"You choose {LANG}. Excellent choise")

st.success("LANGUAGE IS CHOOSED SUCCESSFULLY")