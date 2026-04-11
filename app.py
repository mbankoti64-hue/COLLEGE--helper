import streamlit as st
import time

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="Graphic Era Smart Chatbot", page_icon="🎓", layout="wide")

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

h1 {
    text-align: center;
    color: #4CAF50;
}

[data-testid="stChatMessage"] {
    border-radius: 15px;
    padding: 12px;
    margin: 8px;
    background-color: #1e293b;
}

section[data-testid="stSidebar"] {
    background-color: #020617;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Header
# -------------------------------
st.markdown("""
<h1>🎓 Graphic Era Smart Assistant</h1>
<p style='text-align:center;'>Your 24/7 College Help Partner 🤖</p>
""", unsafe_allow_html=True)

# -------------------------------
# Welcome Message (only once)
# -------------------------------
if "welcome_shown" not in st.session_state:
    st.session_state.welcome_shown = True
    st.info("👋 Welcome! Ask me anything about Graphic Era University.")

# -------------------------------
# Data
# -------------------------------
# def get_college_info(user_input):

    college_data = {
        "about": """LOCATION: Dehradun, Uttarakhand \n
ESTABLISHED: 1997 \n
Founder: Prof.(Dr.) Kamal Ghanshala \n
Type: Private Deemed University \n
Accreditation: NAAC A+ Grade \n
Approved by: UGC, AICTE""",

        "courses": "B.Tech, BCA, MBA, BBA, B.Com, MCA (100+ courses including UG, PG, PhD, Diploma)",

        "fees": "B.Tech: ₹2.5–3.5 LPA | BCA: ₹1.2–1.5 LPA per year",

        "placement": "Highest: ₹65+ LPA | Average: ₹5–8 LPA",

        "hostel": """Hostels Available:\n
Chandra Shekhar Azad Hostel\n
Sardar Patel Hostel\n
Netaji Subhash Chandra Hostel\n
Sai Hostel\n
Fees: ₹1,60,000 (may vary)""",

        "faculty": "600+ Faculty | Mostly PhD Holders"
    }

   
   

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("📌 Quick Menu")
option = st.sidebar.selectbox(
    "Select Option",
    ["Chat Mode", "About", "Courses", "Fees", "Placement", "Hostel", "Faculty"]
)

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# -------------------------------
# Session
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------------
# Sidebar Output
# -------------------------------
if option != "Chat Mode":
    st.success(college_data[option.lower()])

# -------------------------------
# Chat Input
# -------------------------------
user_input = st.chat_input("Ask something...")

# -------------------------------
# Chatbot Logic
# -------------------------------
def get_response(user_input):
    user_input = user_input.lower()

   if "fees" in user_input:
        return college_data["fees"]
    elif "courses" in user_input:
        return college_data["courses"]
    elif "hostel" in user_input:
        return college_data["hostel"]
    elif "placement" in user_input:
        return college_data["placement"]
    elif "faculty" in user_input:
        return college_data["faculty"]
    elif "about" in user_input or "college" in user_input:
        return college_data["about"]
    else:
        return "Sorry, I didn't understand your query.

# -------------------------------
# Show old messages
# -------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------------------
# Typing Effect Function
# -------------------------------
def type_effect(text):
    placeholder = st.empty()
    typed = ""
    for char in text:
        typed += char
        placeholder.markdown(typed)
        time.sleep(0.01)

# -------------------------------
# New Message
# -------------------------------
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    response = get_response(user_input)

    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        type_effect(response)
