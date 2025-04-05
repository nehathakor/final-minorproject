import pickle
import streamlit as st
import numpy as np
from googletrans import Translator

# Load Model
with open('model.pckl', 'rb') as LrdetectFile:
    Lrdetect_Model = pickle.load(LrdetectFile)

translator = Translator()

# Custom CSS for Background & Styling
st.markdown("""
    <style>
        /* Background Image */
        /* Title Styling */
        .title {
            color: white;
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
        /* Button Styling */
        .stButton>button {
            background-color: #250674;
            color: white;
            font-size: 16px;
            padding: 10px;
            border-radius: 10px;
        }
        .stButton>button:hover {
            background-color: #1b07ac;
            color: white;
        }
        /* Footer */
         .footer {
        text-align: center;
        font-size: 14px;
        color: #777;
        margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>Customer Support Language Assistant</h1>", unsafe_allow_html=True)

# Store detected language in session state
if 'detected_lang' not in st.session_state:
    st.session_state['detected_lang'] = None
if 'translated_text' not in st.session_state:
    st.session_state['translated_text'] = None
if 'converted_reply' not in st.session_state:
    st.session_state['converted_reply'] = None

# Step 1: Detect Language
input_text = st.text_area("📩 Enter received message:", placeholder="Paste the customer's message here...")

if st.button("🔍 Detect Language"):
    res = Lrdetect_Model.predict([input_text])  # Predict language
    detected_lang = res[0]
    confidence = np.max(Lrdetect_Model.predict_proba([input_text]))

    # Store detected language
    st.session_state['detected_lang'] = detected_lang
    st.success(f"**Detected Language:** {detected_lang}")

# List of supported languages
specified_languages = {
    'English': 'en', 'Hindi': 'hi', 'Gujarati': 'gu', 'Punjabi': 'pa', 'Tamil': 'ta', 
    'Telugu': 'te', 'Kannada': 'kn', 'Malayalam': 'ml', 'Bengali': 'bn', 'Marathi': 'mr', 
    'Urdu': 'ur', 'Odia': 'or', 'Assamese': 'as', 'Maithili': 'mai', 'Santali': 'sat',
    'French': 'fr', 'Spanish': 'es', 'Portuguese': 'pt', 'Italian': 'it', 'Russian': 'ru', 
    'Swedish': 'sv', 'Dutch': 'nl', 'Arabic': 'ar', 'Turkish': 'tr', 'German': 'de', 
    'Danish': 'da', 'Greek': 'el'
}

# Step 2: Translate Detected Language to Known Language
if st.session_state['detected_lang']:
    target_language = st.selectbox("🌍 Translate to:", list(specified_languages.keys()), key="translate_lang")
    
    if st.button("🔄 Translate"):
        st.session_state['translated_text'] = translator.translate(input_text, dest=specified_languages[target_language]).text
        st.success(f"**Translated Text:** {st.session_state['translated_text']}")

# Step 3: Convert Reply Back to Detected Language
if st.session_state['detected_lang']:
    reply_text = st.text_area("📝 Enter your reply:", placeholder="Type your response here...")

    if st.button("💬 Convert to Customer's Language"):
        detected_code = specified_languages.get(st.session_state['detected_lang'], 'en')  # Get language code
        st.session_state['converted_reply'] = translator.translate(reply_text, dest=detected_code).text
        st.success(f"**Reply in {st.session_state['detected_lang']}:** {st.session_state['converted_reply']}")

st.markdown("""
    <h3 style="color:white;">🌐 Supported Languages:</h3>
""", unsafe_allow_html=True)

st.markdown("<ul><li>French</li><li>Spanish</li><li>Portugese</li><li>Italian</li><li>Russian</li><li>Sweedish</li><li>Malayalam</li><li>Dutch</li><li>Arabic</li><li>Turkish</li><li>German</li><li>Tamil</li><li>English</li><li>Danish</li><li>Kannada</li><li>Greek</li><li>Hindi</li></ul>", unsafe_allow_html=True)

st.markdown("<div class='footer'>🚀 Made by Neha and Sonika</div>", unsafe_allow_html=True)
