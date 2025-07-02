AI-based Resume Screening System

This repository contains a machine learning and NLP-based project that automates the resume screening process using Python. The primary goal is to build a model that efficiently evaluates resumes and suggests the most suitable job category based on the content of the resume.



📚 Table of Contents

Why do we need Resume Screening?

Introduction

Modules & Libraries

Functionality of Application

Tools & Technologies Used

Tech Innovations in Resume Screening

Installation

Usage

Dataset

Model

Results

Contributing

License

Contact

🤔 Why do we need Resume Screening?

Companies receive thousands of resumes for every job posting.

Manual screening is time-consuming and prone to errors.

Screening involves categorizing resumes and shortlisting them by HR teams.

It's difficult to go through hundreds of resumes manually.

Automating resume screening helps reduce hiring time from days to minutes using ML and NLP.

📘 Introduction

Resume screening is the process of evaluating whether a candidate is suitable for a role based on their resume. It involves:

Extracting education, experience, and skills

Matching resume data to job requirements

Automating shortlisting using ML

The project aims to develop a model that can:

Read resumes in .pdf and .txt formats

Preprocess and extract features using NLP

Predict the most suitable job role using classification models

🧩 Modules & Libraries

🔢 Modules Used

TF-IDF: For feature extraction from text

Naive Bayes, Logistic Regression, SVM: For classification

BERT: For semantic text embeddings using Sentence Transformers

📚 Libraries Used

NumPy

Pandas

Scikit-learn

NLTK

SpaCy

sentence-transformers

PyPDF2

Streamlit

⚙️ Functionality of Application

Upload resumes in .pdf or .txt

Extract text content (PDF text extraction using PyPDF2)

Convert text to BERT embeddings

Classify resumes into categories like:

Data Science

Java Developer

HR

Sales

Blockchain

and many more

Display predicted job role using Streamlit UI

🛠️ Tools & Technologies Used

Python

Scikit-learn (ML models)

Streamlit (UI and Deployment)

BERT / Sentence Transformers (Semantic Embeddings)

NLTK / SpaCy (Text Preprocessing)

🤖 Tech Innovations in Resume Screening

Automating resume parsing and classification

Reducing HR workload using AI

Improving resume-job role matching accuracy

Providing near-instant predictions with BERT embeddings

💻 Installation

git clone https://github.com/veereshakm/ai-resume-screening.git
cd ai-resume-screening
pip install -r requirements.txt

🚀 Usage

Run streamlit run app.py

Upload a resume file (.pdf or .txt)

View the predicted job category

📂 Dataset

Collected from public resume samples

Contains columns like:

Category

Resume

Preprocessed using tokenization, stopword removal, TF-IDF, or BERT embeddings

🧠 Model

Models used:

Logistic Regression

SVM

Naive Bayes

BERT + Classifier (Final Model)

Evaluated with:

Accuracy

Precision

Recall

F1-Score

📊 Results

The BERT model showed significantly better performance

Achieved over 80% accuracy on resume classification

Real-time inference via Streamlit app

🤝 Contributing

Contributions are welcome! Feel free to fork the repo, create a new branch, and submit a pull request with improvements.

📄 License

This project is licensed under the MIT License.

📬 Contact

Veeresha Kadlibala Mathada
Final Year CSE StudentSir M Visvesvaraya Institute of Technology, Bengaluru
GitHub: veereshakm 
Email: kmveeresh283@gmail.com
