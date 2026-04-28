import streamlit as st

st.set_page_config(page_title="Graphic Era Smart Chatbot", layout="wide")

# -------------------------------
# SINGLE CSS BLOCK (ALL STYLES HERE)
# -------------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b, #0ea5e9);
    color: white;
}

h1 {
    text-align: left;
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
    <h1 style='margin:0; padding:0; color:#22c55e;'>
    Graphic Era Smart Assistant
    </h1>

    <p style='color:#cbd5f5; margin-top:5px;'>
    Your 24/7 College Help Partner 🤖
    </p>
    """, unsafe_allow_html=True)



# -------------- -----------------
# Welcome Message (only once)
# -------------------------------
if "welcome_shown" not in st.session_state:
    st.session_state.welcome_shown = True
    st.info("👋 Welcome! Ask me anything about Graphic Era University.")

# -------------------------------
# Data

college_data = {
     "about": """\n
   📍LOCATION" : 🏔️Dehadun , uttrakhand\n
     ESTABLISHED: 1997\n
     Founder: Prof.(Dr.)Kamal Ghanshala\n
     Type: Private Deemed University\n
     Accreditation: NAAC A+💯 Grade\n
     Approved by:🎓UGC, AICTE""",
    
    "courses": """\n
🎓 B.Tech: CSE / AI & Data science / Mehanical / Civil / Cyber Security\n
                          
🎓BCA / MCA : AI & Data science / Cyber Security\n  
            
🎓BBA / MBA : AI/DS\n

🎓B.Com / M.Com / Pharmacy / LAW / Hotel Managment\n
                
💯 TOTAL 100+ course (UG + PG + PHD + Diploma)""" ,
           
    "fees": """\n
    .B.Tech: ₹2.5–3.5 Per Year  \n 
    .BCA:    ₹1.2–1.5  Per Year \n
    .MBA:    ₹2–3 Per Year  \n 
    .BBA:    ₹2 Per Year""",
    
    "placement": """\n
    Highest: ₹65+ LPA\n 
    Average Package: ₹5–8 LPA\n
    Placement Rate: 90%+.""",

    "facilities": """\n
    .Smart Classrooms\n
    .Central Library\n
    .Computer Labs\n
    .Gym\n
    .Medical Facility""",
    
   
    "hostel":"""\n
    1. CHANDRA SHEKHER AZAD   (https://maps.app.goo.gl/WMhw86j7jboNe8gVA?g_st=aw)\n  
    
    2. ATLANTIS HOSTEL  (https://maps.app.goo.gl/HBC6HkfLzFtDTCzN9?g_st=aw)\n 
    
    3. NETAJI SUBHASH CHANDRA HOSTEL  (https://maps.app.goo.gl/JdoqmhvdqMnx2DKC7?g_st=aw)\n
    
    4. SAI HOSTEL  (https://maps.app.goo.gl/K6mbtBZNLC2EHnLo9?g_st=aw)  \n
    .Hostel fees : 160000 These fees may vary for different hostels\n 
    .Hostel facilities: WiFi Rooms / Mess Facility / Laundry / 24/7 Security""", 
    
    "companies":"""\n
    .TCS\n
    .Infosys\n
    .Wipro\n
    .Micrisoft\n
    .Google""",

    "block":"""\n
    Total Block 6 Major Block are their
    1. KP.Nautiyal
    2. Chanakya block
    3. OLD MCA block
    4. Main(admission)/ Btech block
    5. CS/IT  block    (BCA and MCA classes are held in the CS/IT block)
    6. Paramedical block""",

    "syllabus":"""\n
    1. Computational Thinking and fundamentals of IT
    2. Fundamentals of Python
    3. Mathematics Foundation for AI
    4. Professional English Skills
    5. Principales and Practices of Managements 

    thes are major subjects""",

    # "Bca 2 semester syllabus":"""Syllabus:\n
    # 1. Computational Thinking and fundamentals of IT
    # 2. Fundamentals of Python
    # 3. Mathematics Foundation for AI
    # 4. Professional English Skills
    # 5. Principales and Practices of Managements 

    #                thes are major subjects""",
     
    "cabin":"""\n
    Mr. priyansh kumar          🧑‍🏫Faculty Cabin   (Paramedical 4th floor)\n
    Mr. Mohit Amoli             🧑‍🏫 Faculty Cabin  (Paramedical 2th floor)\n
    Dr. Didvijay Tanwar         🧑‍🏫Faculty Cabin   (OLD MCA 2th floor)\n
    Ms. Aayushi Rana            👩‍🏫Faculty Cabin   (Paramedical 2th floor)\n
    Ms. Swati Pant              👩‍🏫Faculty Cabin   (Paramedical 4th floor)\n
    Ms. shurti Saini            👩‍🏫Faculty Cabin   (Paramedical 2th floor)\n
    Mr. Gautam Badoni           🧑‍🏫Faculty Cabin   (Paramedical 2th floor)""",
            
    
   
    "faculty":"""\n
    Mr. priyansh kumar   (Introduction to Data Science)             
    Mr. Mohit Amoli      (Foundation of Artificial Intelligence)     
    Dr. Didvijay Tanwar  (Probability and Statistics for Data Science)\n
    Ms. Aayushi Rana     (Programming concepts using c language)    
    Ms. Swati Pant       (Cyber security Essentials)                  
    Ms. shurti Saini     (LAB DS)                                   
    Mr. Gautam Badoni    (LAb C )                                     
            
     All 600+ Faculty | PhD Holders Industry Exprts"""
    
   
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
