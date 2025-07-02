# AI-based Resume Screening System

This repository contains a machine learning project focused on automating the resume screening process using Python and NLP. The application uses BERT embeddings and classification algorithms to predict job roles based on the content of resumes uploaded in PDF or TXT formats.

---

## 📚 Table of Contents

* [Why Resume Screening?](#why-resume-screening)
* [Introduction](#introduction)
* [Modules & Libraries](#modules--libraries)
* [Functionality](#functionality)
* [Tools & Technologies](#tools--technologies)
* [Innovations](#innovations)
* [Installation](#installation)
* [Usage](#usage)
* [Dataset](#dataset)
* [Model](#model)
* [Results](#results)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)

---

## 🔍 Why Resume Screening?

* Companies receive thousands of resumes for each job role.
* Manual screening is time-consuming and error-prone.
* Resume categorization by HR is often inefficient.
* AI-based resume screening dramatically speeds up the process and improves consistency.

---

## 📘 Introduction

Resume screening is the process of evaluating candidate qualifications based on resume data. This project applies machine learning and NLP to match resume content with suitable job roles efficiently.

---

## ⚙️ Modules & Libraries

### Modules

* BERT for contextual text embeddings
* Logistic Regression, SVM for classification

### Libraries

* Pandas
* NumPy
* Scikit-learn
* NLTK
* Spacy
* SentenceTransformers
* PyPDF2
* Streamlit

---

## 🚀 Functionality

* Upload resumes (PDF or TXT)
* Extract resume content
* Convert to BERT embeddings
* Predict and display job role

---

## 🛠 Tools & Technologies

* Python 3.x
* Streamlit (for web UI)
* Scikit-learn
* SentenceTransformers
* PyPDF2
* GitHub for version control

---

## 🧠 Innovations in Resume Screening

* Replaces manual resume sorting with AI-based classification
* Real-time prediction via Streamlit interface
* Uses pre-trained transformer embeddings for better accuracy

---

## ⚙️ Installation

```bash
git clone https://github.com/veereshakm/resume-screening-app.git
cd resume-screening-app
pip install -r requirements.txt
```

---

## 📂 Usage

1. Launch the Streamlit app:

```bash
streamlit run app.py
```

2. Upload a `.pdf` or `.txt` resume
3. View the predicted job role on-screen

---

## 📊 Dataset

* Dataset includes labeled resumes in text format
* Job categories: Data Science, HR, Java Developer, Sales, etc.

---

## 🧪 Model

* BERT embeddings via `sentence-transformers`
* Trained using Logistic Regression / SVM / Naive Bayes
* Model saved as `bert_resume_classifier.pkl`

---

## 📈 Results

* Accuracy: \~85% on test set
* Evaluation metrics: Precision, Recall, F1-Score, Confusion Matrix

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and create a pull request.

---

## 📄 License

MIT License. See the LICENSE file for details.

---

## 📬 Contact

Author: Your Name
GitHub: [veereshakm](https://github.com/your-username)
Email: [kmveeresh283@gmail.com](mailto:your.email@example.com)
