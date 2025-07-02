import streamlit as st
import joblib
from sentence_transformers import SentenceTransformer

st.set_page_config(page_title="AI Resume Screening")

st.title("🧠 AI Resume Screening System")
st.markdown("Upload a resume file (in plain text format) and get the predicted job role.")

try:
    clf = joblib.load("bert_resume_classifier.pkl")
    bert_model = SentenceTransformer('all-MiniLM-L6-v2')
except Exception as e:
    st.error(f"🚨 Error loading model or BERT: {e}")
    st.stop()

uploaded_file = st.file_uploader("Upload a resume (.txt)", type=["txt"])

if uploaded_file is not None:
    try:
        # Read resume text
        text = uploaded_file.read().decode("utf-8")
        
        # Convert to BERT embedding
        embedding = bert_model.encode([text])
        
        # Predict
        prediction = clf.predict(embedding)[0]
        
        # Show result
        st.success(f"🎯 Predicted Job Role: **{prediction}**")
    
    except Exception as e:
        st.error(f"⚠️ Error during prediction: {e}")
