import streamlit as st
import time


st.title("Introduction to Programming with Python")
st.header("Examination Paper")
st.subheader(f"\n{time.strftime("%d/%b/%Y")}")
st.write("<b>Time Allowed: One Hour</b>", unsafe_allow_html=True)

name = st.text_input("", placeholder="Enter your full name")
student_no = st.text_input("", placeholder="Enter your student number")
if len(student_no) > 9:
    st.write(f"Examination Number: {student_no}/{time.strftime("%Y")}A")


st.divider()

if "answers" not in st.session_state:
    st.session_state["answers"] = {}

if "correct_answers" not in st.session_state:
    st.session_state["correct_answers"] = []


#Question1
question = st.write("<b>Question 1.</b>", unsafe_allow_html=True)

radio = st.radio("Which ONE (1) of the following is not a high-level programming language?",
                 ["Python", "VB.NET", "Binary", "Java"], key="option1")
action = st.button("Check Answer1")

if action:
    if st.session_state["option1"] == "Binary":
        st.badge("Correct!", color="green")
        st.session_state["answers"]["result1"] = "True"
        st.session_state["correct_answers"].append("True")
    else:
        st.badge("Wrong!", color="red")
        st.session_state["answers"]["result1"] = "False"


#Question2

question = st.write("<b>Question 2.</b>", unsafe_allow_html=True)

radio = st.radio("Select the commands used for exception handling in Python.", ["""try: except: """, """try: catch: """, """test:
except:""", """test: catch:"""], key="option2")
action = st.button("Check Answer2")

if action:
    if st.session_state["option2"] == """try: except: """:
        st.badge("Correct!", color="green")
        st.session_state["answers"]["result2"] = "True"
        st.session_state["correct_answers"].append("True")
    else:
        st.badge("Wrong!", color="red")
        st.session_state["answers"]["result2"] = "False"


#Question3
question = st.write("<b>Question 3.</b>", unsafe_allow_html=True)

radio = st.radio("Select the example of a logic error.", ["Spelling a key word incorrectly",
                                                          "Using addition instead of multiplication in a calculation",
                                                          "Attempting to multiply a string with an integer",
                                                          "Reading from a text file that does not exist"], key="option3")
action = st.button("Check Answer3")

if action:
    if st.session_state["option3"] == "Using addition instead of multiplication in a calculation":
        st.badge("Correct!", color="green")
        st.session_state["answers"]["result3"] = "True"
        st.session_state["correct_answers"].append("True")
    else:
        st.badge("Wrong!", color="red")
        st.session_state["answers"]["result3"] = "False"

#Question4
question = st.write("<b>Question 4.</b>", unsafe_allow_html=True)

radio = st.radio("Which ONE (1) of the following is not a reason for a program using an external text file.", ["To load a previous program state",
                                                                                                               "To store inputs for use in the program",
                                                                                                               "To store data for future use",
                                                                                                               "To store data permanently"], key="option4")
action = st.button("Check Answer4")

if action:
    if st.session_state["option4"] == "To store inputs for use in the program":
        st.badge("Correct!", color="green")
        st.session_state["answers"]["result4"] = "True"
        st.session_state["correct_answers"].append("True")
    else:
        st.badge("Wrong!", color="red")
        st.session_state["answers"]["result4"] = "False"


#Question5
question = st.write("<b>Question 5.</b>", unsafe_allow_html=True)

radio = st.radio("Which ONE (1) of the following is a definition of the implementation stage of the software development lifecycle?",
                 ["Installing the program in the final place to be used",
                  "Writing the program code ",
                  "Creating a flowchart for part of the system ",
                  "Making sure the program meets requirements "], key="option5")
action = st.button("Check Answer5")

if action:
    if st.session_state["option5"] == "Installing the program in the final place to be used":
        st.badge("Correct!", color="green")
        st.session_state["answers"]["result5"] = "True"
        st.session_state["correct_answers"].append("True")

    else:
        st.badge("Wrong!", color="red")
        st.session_state["answers"]["result5"] = "False"

submit = st.button("Submit")

if submit:
    try:
        st.text(f"Congratulations {name.title()}, you have completed the exam!")

        total_questions = len(st.session_state["answers"].values())
        st.write(f"total questions = {total_questions}")

        correct_answers = len(st.session_state["correct_answers"])
        st.write(f"correct answers = {correct_answers}")

        percentage = float((correct_answers/total_questions)*100)
        st.write(f"<b>Your total score is: {correct_answers}/{total_questions} which is {percentage}%</b>", unsafe_allow_html=True)
    except ZeroDivisionError:
        st.write("Please answer a question first")