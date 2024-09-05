import streamlit as st

st.title("Teacher's Day Greeting Program")
st.write("Enter your name below to receive a personalized message:")

# Input field for the name
name = st.text_input("Enter your first name:")

# Function to show the personalized message
def show_message(name):
    name = name.lower()
    if name == "paramita":
        return "Happy teacher's day! You are the reason I am able to write this program. Your teaching is like magic."
    elif name == "anumada":
        return "Thank you for all those efforts that you made for me. All the credit of my marks goes to you. Happy teacher's day!"
    elif name in ["ravneet", "nagi"]:
        return "Happy teacher's day! Your way of teaching is very interesting and you have made sure that I understood every concept."
    elif name == "sukhwinder":
        return "You are the best teacher in the world! Your lectures help us to understand everything and we are able to learn new things."
    elif name == "rachit":
        return "Happy teacher's day! You work hard so that we don't have to."
    elif name in ["monica", "monika"]:
        return "Happy teacher's day! You explain all the chapters in an easy way. You explained my favourite poem 'The Ball Poem' in the best way."
    elif name == "mamta":
        return "धन्यवाद। आप हर कहानी और कविता को बेहतरीन तरीके से समझाती हैं और हमारे सभी संदेह दूर करती हैं।"
    elif name == "lucky":
        return "Happy teacher's day 😄"
    elif name == "akhilesh":
        return "Click here: https://en.wikipedia.org/wiki/Thank_you"
    else:
        return "Try entering only your first name or this name may not be available yet."

# Display the personalized message when the user enters their name
if st.button("Submit"):
    message = show_message(name)
    st.write(message)