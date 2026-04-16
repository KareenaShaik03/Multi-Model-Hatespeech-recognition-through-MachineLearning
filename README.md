# Hate Speech Detection Project

## 📌 Overview

This project focuses on detecting and classifying hate speech in text using machine learning / deep learning techniques. The model is designed to identify different types of harmful language such as explicit hate, profanity, identity-based hate, and indirect conversational hate.

---

## 🚀 Features

* Detects hate speech in user input text
* Classifies text into multiple categories:

  * Slurs / Explicit Hate
  * Profanity
  * Identity-based Hate
  * Conversational / Indirect Hate
* Preprocessing pipeline for cleaning and preparing text data
* Model training and evaluation

---

## 🛠️ Tech Stack

* Python
* FastAPI (for API deployment)
* Transformers (Hugging Face)
* PyTorch
* HTML/CSS (for simple UI)

---

## 📂 Project Structure

```
├── app.py              # FastAPI application
├── model/              # Trained model files
├── templates/          # HTML templates (UI)
├── static/             # CSS / static files
├── data/               # Dataset (if included)
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```

---

## ⚙️ Installation & Setup

1. Clone the repository:

```
git clone <your-repo-link>
cd <project-folder>
```

2. Create virtual environment:

```
python -m venv venv
```

3. Activate environment:

```
venv\Scripts\activate   # Windows
```

4. Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Start the FastAPI server:

```
uvicorn app:app --reload
```

Open in browser:

```
http://127.0.0.1:8000
```

---

## 🧠 Model Details

* Pretrained transformer model (e.g., T5 / BERT)
* Fine-tuned on hate speech dataset
* Handles both explicit and implicit hate patterns

---

## 📊 Example

**Input:**

> "Those people are always so annoying."

**Output:**

> Conversational Hate

---

## 🔮 Future Improvements

* Improve dataset size and diversity
* Add multilingual support
* Deploy on cloud (AWS / Render / Vercel)
* Enhance UI/UX

---

## 👩‍💻 Author

Your Name

---
