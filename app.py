import pickle
import string
import streamlit as st
import webbrowser

global Lrdetect_Model

LrdetectFile = open('model.pckl','rb')
Lrdetect_Model = pickle.load(LrdetectFile)
LrdetectFile.close()
st.title("LangDetect: Language Detector")
input_test = st.text_input("Enter text here:", 'Welcome to LangDetect ')

res = Lrdetect_Model.predict([input_test])

button_clicked = st.button("Detect Language")
if button_clicked:
	st.text(f'The language "{input_test}" is {res[0]}')
	

st.write(f'We supports given 5 languages: ')
st.write(f'English')
st.write(f'Hindi')
st.write(f'Spanish')
st.write(f'Arabic')
st.write(f'Russian')

st.markdown("<h3 style='text-align: center;'>Made by Neha and Sonika</h3>", unsafe_allow_html=True)