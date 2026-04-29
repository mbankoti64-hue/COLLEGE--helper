import streamlit as st

import time

st.set_page_config(page_title="Graphic Era Smart Chatbot", layout="wide")

# -------------------------------
# SINGLE CSS BLOCK (ALL STYLES HERE)
# -------------------------------
st.markdown("""
<style>

/* Background */
.stApp {
    background:
        linear-gradient(rgba(10,10,30,0.85), rgba(20,20,50,0.9)),
        url("https://images.unsplash.com/photo-1550751827-4bd374c3f58b") no-repeat center center fixed;
    background-size: cover;
    color: #ffffff;
}

/* Heading */
h1 {
    text-align: left;
    color: #a855f7;
    text-shadow: 0 0 12px #a855f7;
}

/* Paragraph / normal text */
p {
    color: #ffffff;
    font-size: 20px;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-shadow: 0 0 3px rgba(255,255,255,0.5);
}

/* 🔵 GLASS CHAT BOX (FIXED) */
[data-testid="stChatMessage"] {
    border-radius: 15px;
    padding: 12px;
    margin: 8px;

    background: rgba(59, 130, 246, 0.22);   /* 🔥 transparent blue */
    backdrop-filter: blur(8px);             /* glass effect */

    border: 1px solid rgba(59,130,246,0.9); /* glowing line */

    box-shadow: 
        0 0 15px rgba(59, 130, 246, 0.6),
        inset 0 0 10px rgba(59,130,246,0.3);

    color: #ffffff;
}

/* 🔥 OUTPUT TEXT (Glow + Bold) */
[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] span,
[data-testid="stChatMessage"] div {
    font-weight: 700;   /* extra bold */

    color: #ffffff;

    text-shadow: 
        0 0 3px rgba(255,255,255,0.4),
        0 0 6px rgba(59,130,246,0.3),
       
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0f0c29;
}

/* Top spacing */
.block-container {
    padding-top: 3rem;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# HEADER
# -------------------------------
col1, col2 = st.columns([1, 4])

with col1:
    st.image("logo.jpg.jpeg", width=170)

with col2:
    st.markdown("""
    <h1 style='margin:0; padding:0;'>
    Graphic Era Smart Assistant
    </h1>

    <p style='margin-top:5px;'>
    Your 24/7 College Help Partner 🤖
    </p>
    """, unsafe_allow_html=True)

# -------------------------------
# WELCOME
# -------------------------------
if "welcome_shown" not in st.session_state:
    st.session_state.welcome_shown = True
    # st.info("👋 Welcome! Ask 

    st.info("👋 Welcome! Ask me anything about Graphic Era University.")

# -------------------------------
# Data

college_data = {
      
     "about": """\n
      Sure! Here's everything you need to know about the college\n\n
      
     - 📍LOCATION : 🏔️Dehadun , uttrakhand
     - 🏛️ESTABLISHED: 1997
     - 👨‍🏫Founder: Prof.(Dr.)Kamal Ghanshala
     - 🏛️Type: Private Deemed University
     - ⭐Accreditation: NAAC A+💯 Grade
     -  Approved by:🎓UGC, AICTE
      
      If there's anything else you'd like to explore or know in more detail, feel free to ask — I'm here to help you anytime!👍""",
     
   
    "courses": """\n
     Sure! Here's everything you need to know about the courses\n\n
     
- 🎓B.Tech: CSE / AI & Data science / Mehanical / Civil / Cyber Security
- 🎓BCA / MCA : AI & Data science / Cyber Security       
- 🎓BBA / MBA : AI/DS
- 🎓B.Com / M.Com / Pharmacy / LAW / Hotel Managment              
- 💯TOTAL 100+ course (UG + PG + PHD + Diploma)


If there's anything else you'd like to explore or know in more detail, feel free to ask — I'm here to help you anytime!👍""",
           
    "fees": """\n
     Sure! Here's everything you need to know about the college feesn\n
    - B.Tech :     ₹2.5–3.5 Per Year  
    - BCA   :     ₹1.2–1.5  Per Year 
    - MBA   :     ₹2–3 Per Year  
    - BBA   :     ₹2 Per Year

    
    If there's anything else you'd like to explore or know in more detail, feel free to ask — I'm here to help you anytime!👍""",
    
    "placement": """\n
     Sure! Here's everything you need to know about the college placement\n\n
    - Highest: ₹65+ LPA
    - Average Package: ₹5–8 LPA
    - Placement Rate: 90%+

    
    If there's anything else you'd like to explore or know in more detail, feel free to ask — I'm here to help you anytime!👍""",

    "facilities": """\n
     Sure! Here's everything you need to know about the college facilities\n\n
    - Smart Classrooms
    - Central Library
    - Computer Labs
    - Gym
    - Medical Facility

    
    If there's anything else you'd like to explore or know in more detail, feel free to ask — I'm here to help you anytime!👍""",
    
   
    "hostel":"""\n
     Sure! Here's everything you need to know about the college hostels\n\n
    - CHANDRA SHEKHER AZAD (https://maps.app.goo.gl/WMhw86j7jboNe8gVA?g_st=aw) 
    - ATLANTIS HOSTEL  (https://maps.app.goo.gl/HBC6HkfLzFtDTCzN9?g_st=aw)
    - NETAJI SUBHASH CHANDRA HOSTEL  (https://maps.app.goo.gl/JdoqmhvdqMnx2DKC7?g_st=aw)
    - SAI HOSTEL  (https://maps.app.goo.gl/K6mbtBZNLC2EHnLo9?g_st=aw)  
    - Hostel fees : 160000 These fees may vary for different hostels\
    - Hostel facilities: WiFi Rooms / Mess Facility / Laundry / 24/7 Security

    
    If there's anything else you'd like to explore or know in more detail, feel free to ask — I'm here to help you anytime!👍""",
    
    "companies":"""\n
     Sure! Here's everything you need to know about the companies\n\n
    - TCS
    - Infosys
    - Wipro
    - Micrisoft
    - Google 

    
    If there's anything else you'd like to explore or know in more detail, feel free to ask — I'm here to help you anytime!👍""",

    "block":"""\n
     Sure! Here's everything you need to know about the college block\n\n
    Total Block 6 Major Block are their
    1. KP.Nautiyal
    2. Chanakya block
    3. OLD MCA block
    4. Main(admission)/ Btech block  [https://maps.app.goo.gl/haAD6v2UiNW7oRFeA?g_st=aw]
    5. CS/IT  block    (BCA and MCA classes are held in the CS/IT block)  [https://maps.app.goo.gl/8PAvvyDCTchfH1rp6?g_st=aw]
    6. Paramedical block [https://maps.app.goo.gl/8PAvvyDCTchfH1rp6?g_st=aw]

    
    If there's anything else you'd like to explore or know in more detail, feel free to ask — I'm here to help you anytime!👍""",

    "syllabus":"""\n
     Sure! Here's everything you need to know about the BCA syllabus\n\n
    1. Computational Thinking and fundamentals of IT
    2. Fundamentals of Python
    3. Mathematics Foundation for AI
    4. Professional English Skills
    5. Principales and Practices of Managements 
   
    
    If there's anything else you'd like to explore or know in more detail, feel free to ask — I'm here to help you anytime!👍""",

    # "Bca 2 semester syllabus":"""Syllabus:\n
    # 1. Computational Thinking and fundamentals of IT
    # 2. Fundamentals of Python
    # 3. Mathematics Foundation for AI
    # 4. Professional English Skills
    # 5. Principales and Practices of Managements 
# https://github.com/mbankoti64-hue/COLLEGE--helper/blob/main/app.py 
    #                thes are major subjects""",
     
    "cabin":"""\n
     Sure! Here's everything you need to know about the faculty cabin\n\n
    - Mr. priyansh kumar           [ Faculty Cabin   (Paramedical 4th floor)]
    - Mr. Mohit Amoli              [ Faculty Cabin  (Paramedical 2th floor)]
    - Dr. Didvijay Tanwar          [ Faculty Cabin   (OLD MCA 2th floor)]
    - Ms. Aayushi Rana             [Faculty Cabin   (Paramedical 2th floor)]
    - Ms. Swati Pant               [Faculty Cabin   (Paramedical 4th floor)]
    - Ms. shurti Saini             [Faculty Cabin   (Paramedical 2th floor)]
    - Mr. Gautam Badoni            [Faculty Cabin   (Paramedical 2th floor)]

    If there's anything else you'd like to explore or know in more detail, feel free to ask — I'm here to help you anytime!👍""",
            
    
   
    "faculty":"""\n
     Sure! Here's everything you need to know about the faculty\n\n
    - MR. (Dr.) Dinesh Dohbal (HOD)
    - Mr. priyansh kumar   (Introduction to Data Science)            
    - Mr. Mohit Amoli      (Foundation of Artificial Intelligence)    
    - Dr. Didvijay Tanwar  (Probability and Statistics for Data Science)
    - Ms. Aayushi Rana     (Programming concepts using c language)   
    - Ms. Swati Pant       (Cyber security Essentials)                
    - Ms. shurti Saini     (LAB DS)                                  
    - Mr. Gautam Badoni    (LAb C )                                    
            
     All 600+ Faculty | PhD Holders Industry Exprts

     If there's anything else you'd like to explore or know in more detail, feel free to ask — I'm here to help you anytime!👍""",

    
    
   
}

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("📌 Quick Menu")
option = st.sidebar.selectbox(
    "Select Option",
    ["Chat Mode", "About", "Courses", "Fees", "Placement", "Hostel", "Faculty","Syllabus","Cabin","Block","Facilities","Companies"]
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
    st.info(college_data[option.lower()])

# -------------------------------
# Chat Input
# -------------------------------
user_input = st.chat_input("Ask something...")

# -------------------------------
# Chatbot Logic
# -------------------------------
def get_response(user_input):
    user_input = user_input.lower()

    if "fee" in user_input:
        return college_data["fees"]
    elif "course" in user_input:
        return college_data["courses"]
    elif "block" in user_input:
        return college_data["block"]
    elif "companies" in user_input:
        return college_data["companies"]
        
    elif "facilities" in user_input:
        return college_data["facilities"]
    elif "syllabus" in user_input:
        return college_data["syllabus"]
    elif "hostel" in user_input:
        return college_data["hostel"]
    elif "cabin" in user_input:
        return college_data["cabin"]
    elif "placement" in user_input:
        return college_data["placement"]
    elif "faculty" in user_input:
        return college_data["faculty"]
    elif "about" in user_input or "college" in user_input:
        return college_data["about"]
    elif "hi" in user_input or "hello" in user_input or "namste bhai jii" in user_input:
        return "AAGYA GANDU🤣🤣🤣🤣"
    else:
        return "❗   ARE BHOSDIKE TERI GAND MARU KUCH ACCHA PUCH Try asking about fees, courses, placement, hostel."

# -------------------------------
# Show old messages
# -------------------------------

# -------------------------------
# Typing Effect Function
# -------------------------------
def type_effect(text):
    placeholder = st.empty()
    typed = ""
    for char in text:
        typed += char
        placeholder.markdown(typed)
        time.sleep(0.008)

# -------------------------------
# New Message
# -------------------------------
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    response = get_response(user_input)

    st.session_state.messages.append({"role": "assistant", "content": response})

    type_effect(response)
