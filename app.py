import streamlit as st
import joblib
from sentence_transformers import SentenceTransformer
import PyPDF2

# Set Streamlit page config
st.set_page_config(page_title="AI Resume Screening System")

st.title("🧠 AI Resume Screening System")
st.markdown("Upload a resume file (in **PDF** or **TXT** format) and get the predicted job role.")

# Load model and BERT embedding
try:
    clf = joblib.load("bert_resume_classifier.pkl")
    bert_model = SentenceTransformer('all-MiniLM-L6-v2')
except Exception as e:
    st.error(f"🚨 Model loading error: {e}")
    st.stop()

# Upload file (PDF or TXT)
uploaded_file = st.file_uploader("Upload a resume (.pdf or .txt)", type=["pdf", "txt"])

if uploaded_file is not None:
    try:
        # Extract text from PDF or TXT
        if uploaded_file.type == "application/pdf":
            reader = PyPDF2.PdfReader(uploaded_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
        else:
            text = uploaded_file.read().decode("utf-8")

        # Get BERT embedding
        embedding = bert_model.encode([text])

        # Predict job role
        prediction = clf.predict(embedding)[0]

        # Display result
        st.success(f"🎯 Predicted Job Role: **{prediction}**")

    except Exception as e:
        st.error(f"⚠️ Error processing file: {e}")
