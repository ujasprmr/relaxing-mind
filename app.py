# relaxing-mind
# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.5-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""1. Full Name: Priya Sharma  
2. Email: priyasharma123@gmail.com, Phone: +91 9876543210, LinkedIn: linkedin.com/in/priyasharma  
3. Career Objective: Seeking a challenging role as a software developer where I can apply my coding and problem-solving skills to deliver innovative solutions.  
4. Work Experience:  
   - Job Title: Software Engineer  
     Company: Infosys, Bangalore  
     Duration: Jan 2022 – Present  
     Responsibilities:  
       • Developed scalable web applications using React and Node.js  
       • Integrated REST APIs and optimized frontend performance  
   - Job Title: Intern  
     Company: Wipro  
     Duration: June 2021 – Dec 2021  
     Responsibilities:  
       • Assisted in developing internal tools using Python and Flask  
       • Created test cases and supported QA team  

5. Education:  
   - B.Tech in Computer Science, VIT University, 2021, CGPA: 8.7  
   - 12th CBSE, Delhi Public School, 2017, 90%  

6. Skills: JavaScript, Python, React, Node.js, SQL, Git, Problem Solving, Communication  

7. Certifications:  
   - AWS Certified Cloud Practitioner, 2023  
   - Coursera: Full Stack Web Development, 2022  

8. Projects:  
   - Title: Task Manager App  
     Description: A full-stack task management app using MERN stack.  
     Technologies: MongoDB, Express, React, Node.js  

9. Languages: English, Hindi  

10. Hobbies: Reading Tech Blogs, Playing Chess  
"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""**Bypassing Initial Steps**

I've streamlined the process. The user's comprehensive input allows me to skip the preliminary stages and proceed directly to resume generation. I'm focusing on crafting the document efficiently, adhering to all instructions.


**Processing Direct Input**

My approach shifts to direct processing. I'm focusing on incorporating all user-provided information without redundant initial steps. I'm ensuring all sections (contact, summary, experience, education, skills, certifications, projects, languages, and hobbies) are present and formatted correctly, prioritizing chronological order where needed, and wrapping the final product in a Markdown code block.


"""),
                types.Part.from_text(text="""```
Priya Sharma
priyasharma123@gmail.com | +91 9876543210 | linkedin.com/in/priyasharma

CAREER OBJECTIVE
Seeking a challenging role as a software developer where I can apply my coding and problem-solving skills to deliver innovative solutions.

WORK EXPERIENCE

Software Engineer | Infosys, Bangalore | Jan 2022 – Present
* Developed scalable web applications using React and Node.js
* Integrated REST APIs and optimized frontend performance

Intern | Wipro | June 2021 – Dec 2021
* Assisted in developing internal tools using Python and Flask
* Created test cases and supported QA team

EDUCATION

B.Tech in Computer Science | VIT University | 2021 | CGPA: 8.7
12th CBSE | Delhi Public School | 2017 | 90%

SKILLS
JavaScript, Python, React, Node.js, SQL, Git, Problem Solving, Communication

CERTIFICATIONS

AWS Certified Cloud Practitioner | 2023
Coursera: Full Stack Web Development | 2022

PROJECTS

Task Manager App
* A full-stack task management app using MERN stack.
* Technologies: MongoDB, Express, React, Node.js

LANGUAGES
English, Hindi

HOBBIES
Reading Tech Blogs, Playing Chess
```"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
            thinking_budget=-1,
        ),
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""You are a professional Resume Builder Assistant.

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
"""),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()
