

# FAQ Chatbot Assistant

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python\&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-ff4b4b?logo=streamlit\&logoColor=white)](https://streamlit.io/)
[![NLTK](https://img.shields.io/badge/NLTK-NLP-brightgreen?logo=academia\&logoColor=white)](https://www.nltk.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Open Issues](https://img.shields.io/github/issues/saadoxyz/faq-chatbot)](https://github.com/saadoxyz/faq-chatbot/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/saadoxyz/faq-chatbot)](https://github.com/saadoxyz/faq-chatbot/pulls)
[![Last Commit](https://img.shields.io/github/last-commit/saadoxyz/faq-chatbot)](https://github.com/saadoxyz/faq-chatbot/commits/main)
[![Contributors](https://img.shields.io/github/contributors/saadoxyz/faq-chatbot)](https://github.com/saadoxyz/faq-chatbot/graphs/contributors)
[![Stars](https://img.shields.io/github/stars/saadoxyz/faq-chatbot?style=social)](https://github.com/saadoxyz/faq-chatbot/stargazers)

---

## Overview

**FAQ Chatbot Assistant** is an interactive chatbot built with **Python**, **NLTK**, **Scikit-learn**, and **Streamlit**.
It leverages **TF-IDF vectorization** and **cosine similarity** to match user queries with the most relevant **Frequently Asked Questions (FAQs)**, delivering instant answers in a sleek, **dark-mode UI**.

### What is an FAQ Chatbot?

An **FAQ (Frequently Asked Questions) Chatbot** is a type of chatbot designed to **automatically answer common questions** for users.
Instead of manually searching through help articles, users can simply ask questions in natural language, and the chatbot retrieves the **most relevant answer** from a predefined FAQ database.

Typical use cases include:

* Customer support on e-commerce or service websites.
* Internal IT or HR support for employees.
* Educational platforms providing instant guidance to students.

**Benefits of an FAQ Chatbot:**

*  Instant response for common queries
*  Reduces human support workload
*  Improves user experience
*  Scales effortlessly for large FAQ datasets

This project is designed to demonstrate:

*  **Natural Language Processing (NLP)** basics (tokenization, stopwords removal)
*  **Information Retrieval** using TF-IDF + cosine similarity
*  **Modern UI/UX** with avatars, chat bubbles, and dark theme
*  How to build a **deployable, production-ready chatbot** for real-world FAQs

---

##  Features

 **Dark-themed UI** – professional, clean, and user-friendly
 **Chat-like experience** – avatars for both user and bot
 **Instant FAQ matching** – powered by TF-IDF & cosine similarity
 **Quick action buttons** – pre-defined common questions
 **Expandable FAQ dataset** – just add more Q&A pairs
 **Lightweight & fast** – no heavy ML model required

---

## Tech Stack

* **Frontend / UI**: [Streamlit](https://streamlit.io/)
* **NLP**: [NLTK](https://www.nltk.org/)
* **Vectorization**: [Scikit-learn (TF-IDF)](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
* **Backend**: Python 3.9+
* **Deployment**: Streamlit Cloud / Docker / Heroku (optional)

---

## Project Structure

```
faq-chatbot/
│── faq_chatbot_ui.py   # Streamlit UI with chatbot logic
│── faq_chatbot.py      # CLI version (terminal chatbot)
```

---

##  Installation & Usage

###  Clone the Repository

```bash
git clone https://github.com/your-username/faq-chatbot.git
cd faq-chatbot
```

###  Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

###  Install Dependencies

```bash
pip install -r requirements.txt
```

###  Run the Chatbot (UI mode)

```bash
streamlit run faq_chatbot_ui.py
```

###  Run the CLI version (optional)

```bash
python faq_chatbot.py
```

---

##  Example Interaction

**User**: `How do I track my order?`
**Bot**: `Use the tracking link sent to your email after purchase. You can also track your order by logging into your account.`

**User**: `thanks`
**Bot**: `You're welcome! Is there anything else I can help you with?`


##  Support

If you like this project, consider giving it a ⭐ on GitHub!
It helps more developers discover it.

---
