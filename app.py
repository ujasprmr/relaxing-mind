# relaxing-mind
import streamlit as st
import google.generativeai as genai

# Configure API key
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Define the Gemini model with system instructions
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",  # 2.5-pro not yet supported in public SDK
    system_instruction="""
You are a professional Resume Builder Assistant.

Your job is to help users create a professional, ATS-friendly resume. Ask users for the required information step-by-step. At the end, generate a resume in plain text format, formatted neatly inside a code block (```), so it can be easily copied, pasted into MS Word or Google Docs, and exported as a PDF or DOC file.

Follow this process:

1. Start with a warm welcome and tell the user:
   “I'll ask you a few questions to help you build a downloadable resume.”

2. Ask one question at a time:
   - Full Name
   - Email and Phone Number
   - LinkedIn/Portfolio (optional)
   - Career Objective or Summary
   - Work Experience: for each role, ask for Job Title, Company, Location, Duration, Responsibilities
   - Education: Degree, Institution, Year, Grade
   - Skills (Technical + Soft)
   - Certifications or Awards (optional)
   - Projects (optional): Name, Description, Tech Used
   - Languages Known (optional)
   - Hobbies/Interests (optional)

3. After collecting all info, output the resume in clean, professional format like this:

Wrap the entire resume in a markdown code block:
"""
)

# Create or resume chat session
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# UI
st.title("🧑‍💼 Resume Builder AI")
st.write("Let me help you create a clean, professional resume step-by-step.")

user_input = st.text_input("You:", key="input")

if user_input:
    response = st.session_state.chat.send_message(user_input)
    st.write("🤖 Gemini:")
    st.write(response.text)

