import streamlit as st

# Function to display a message bubble
def message_bubble(message, is_user=True):
    alignment = "end" if is_user else "start"
    bubble_color = "#dcf8c6" if is_user else "#ffffff"
    st.markdown(f"""
    <div style="display: flex; justify-content: {alignment}; margin: 10px 0;">
        <div style="background-color: {bubble_color}; padding: 10px 15px; border-radius: 15px; max-width: 60%;">
            {message}
        </div>
    </div>
    """, unsafe_allow_html=True)

# Initialize session state for storing messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the chat messages
st.title("WhatsApp-like Chat Interface")
st.markdown("### Chat History")

for msg in st.session_state.messages:
    message_bubble(msg["message"], msg["is_user"])

# Input area for new messages
st.markdown("### Send a message")
user_input = st.text_input("Your message", "")

if st.button("Send"):
    if user_input:
        # Store user message
        st.session_state.messages.append({"message": user_input, "is_user": True})
        # Add bot response (for demo purposes, echo the user message)
        st.session_state.messages.append({"message": f"Bot: {user_input}", "is_user": False})
        st.experimental_rerun()  # Rerun to update the chat display



       

            
