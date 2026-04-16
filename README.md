# Hate Speech Detection Project

## 📌 Overview

This project focuses on detecting and classifying hate speech in text using machine learning / deep learning techniques. The system analyzes user input and categorizes it into different types of harmful language such as explicit hate, profanity, identity-based hate, and indirect conversational hate.

---

## 🚀 Features

* Detects hate speech in user input text
* Classifies text into multiple categories:

  * Slurs / Explicit Hate
  * Profanity
  * Identity-based Hate
  * Conversational / Indirect Hate
* Clean and simple web interface using Django
* Preprocessing pipeline for text cleaning and normalization
* Model integration for real-time predictions

---

## 🛠️ Tech Stack

* Python
* Django (Web Framework)
* Transformers (Hugging Face)
* PyTorch / TensorFlow
* HTML, CSS

---

## 📂 Project Structure

```
├── manage.py              # Django project manager
├── project/               # Main project settings
│   ├── settings.py
│   ├── urls.py
├── app/                   # Main application
│   ├── views.py
│   ├── models.py
│   ├── urls.py
├── templates/             # HTML templates
├── static/                # CSS / JS files
├── model/                 # Trained ML model
├── data/                  # Dataset (if included)
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
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

Start the Django development server:

```
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

## 🧠 Model Details

* Pretrained transformer model (e.g., BERT / T5)
* Fine-tuned on hate speech dataset
* Capable of detecting both explicit and implicit hate

---

## 📊 Example

**Input:**

> "I hate how those people behave."

**Output:**

> Conversational Hate

---

## 🔮 Future Improvements

* Improve dataset size and labeling quality
* Add multilingual support
* Deploy using cloud platforms (AWS / Render)
* Improve UI and user experience

---

## 👩‍💻 Author

Kareena Shaik
---
