import streamlit as st

st.title("Chai Taste Poll")

col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image("https://images.pexels.com/photos/230490/pexels-photo-230490.jpeg?auto=compress&cs=tinysrgb&w=600", width=200)
    vote1 = st.button("Vote Masala Chai")

with col2:
    st.header("Adrak Chai")
    st.image("https://images.pexels.com/photos/1872904/pexels-photo-1872904.jpeg?auto=compress&cs=tinysrgb&w=600", width=200)
    vote2 = st.button("Vote Adrak Chai")

if vote1:
    st.success("Thanks for voting Masala Chai")

elif vote2:
    st.success("Thanks for voiting Adrak Chai")

name = st.sidebar.text_input("Enter your Name")
tea = st.sidebar.selectbox("Choose Your Chai", ["Masala","Kesar","Adrak"])
if name and tea :
  st.sidebar.write(f"Welcome {name} your {tea} chai is getting ready")

with st.expander("Show Chai Making Instructions"):
    st.write("""
    1. Boil water with tea leaves 
    2. Add milk and spices
    3. Serve Hot
""")
    
st.markdown('### Welcome to Chai App')
st.markdown('> Blockquote')
