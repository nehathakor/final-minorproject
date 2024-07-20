import pickle
import string
import streamlit as st
import webbrowser

global Lrdetect_Model

LrdetectFile = open('model.pckl','rb')
Lrdetect_Model = pickle.load(LrdetectFile)
LrdetectFile.close()

st.markdown("""
    <style>
    .main {
        background-color: black;
        font-family: Arial, sans-serif;
    }
    .title {
        color: #4CAF50;
        text-align: center;
    }
    .text-input {
        border: 1px solid #ccc;
        border-radius: 4px;
        padding: 10px;
        width: 100%;
        box-sizing: border-box;
        font-size: 16px;
    }
    .button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 16px;
        text-align: center;
    }
    .button:hover {
        background-color: #45a049;
    }
    .footer {
        text-align: center;
        font-size: 14px;
        color: #777;
        margin-top: 20px;
    }
            
    .navbar {
        overflow: hidden;
        background-color: #333;
    }
    .navbar a {
        float: left;
        display: block;
        color: white;
        text-align: center;
        padding: 10px 16px;
        text-decoration: none;
    }
    .navbar a:hover {
        background-color: #ddd;
        color: black;
    }
            
    </style>
""", unsafe_allow_html=True)

# st.title("LangDetect: Language Detector")
# input_test = st.text_input("Enter text here:", 'Welcome to LangDetect ')

# res = Lrdetect_Model.predict([input_test])

# button_clicked = st.button("Detect Language")
# if button_clicked:
# 	st.text(f'The language "{input_test}" is {res[0]}')
	

# st.write(f'We supports given 5 languages: ')
# st.write(f'English')
# st.write(f'Hindi')
# st.write(f'Spanish')
# st.write(f'Arabic')
# st.write(f'Russian')

# st.markdown("<h3 style='text-align: center;'>Made by Neha and Sonika</h3>", unsafe_allow_html=True)

st.markdown("<h3 class='title'>LangDetect: Language Detector</h3>", unsafe_allow_html=True)

# Text input
input_test = st.text_input("Enter text here:", 'Welcome to LangDetect ', key="input", placeholder="Type your text here...")

# Button
button_clicked = st.button("Detect Language", key="button")

if button_clicked:
    res = Lrdetect_Model.predict([input_test])
    st.markdown(f"<h5 class='title'>The language '{input_test}' is {res[0]}</h5>", unsafe_allow_html=True)

st.markdown("<h3>We support the following 5 languages:</h3>", unsafe_allow_html=True)
st.markdown("<ul><li>English</li><li>Hindi</li><li>Spanish</li><li>Arabic</li><li>Russian</li></ul>", unsafe_allow_html=True)

st.markdown("<div class='footer'>Made by Neha and Sonika</div>", unsafe_allow_html=True)


