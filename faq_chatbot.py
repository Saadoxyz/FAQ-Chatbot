# faq_chatbot.py
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- 1) FAQ dataset (questions -> answers)
faqs = {
    "What is your return policy?": "You can return any item within 30 days of purchase.",
    "How do I track my order?": "Use the tracking link sent via email to track your order.",
    "Do you offer international shipping?": "Yes — we ship worldwide with additional fees.",
    "How do I contact support?": "Email support@example.com or call +1-555-555-5555."
}

# --- 2) Preprocessing setup ---
nltk.download("punkt", quiet=True)       # ensures tokenizer is available
nltk.download("stopwords", quiet=True)   # ensures stopwords are available
stop_words = set(stopwords.words("english"))

def preprocess(text):
    """Lowercase, tokenize, remove punctuation and stopwords, then join back."""
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in string.punctuation]
    tokens = [t for t in tokens if t not in stop_words]
    return " ".join(tokens)

# Preprocess FAQ questions and build TF-IDF matrix
questions = list(faqs.keys())
processed_questions = [preprocess(q) for q in questions]
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(processed_questions)

# --- 3) Chatbot: compute similarity and return best answer ---
def chatbot_response(user_input):
    user_proc = preprocess(user_input)
    user_vec = vectorizer.transform([user_proc])
    similarities = cosine_similarity(user_vec, faq_vectors)  # shape (1, n_faqs)
    best_idx = similarities.argmax()
    best_score = similarities[0, best_idx]
    # you can set a threshold if best_score is too low (no good match)
    return questions[best_idx], faqs[questions[best_idx]], float(best_score)

# --- 4) CLI loop ---
if __name__ == "__main__":
    print("🤖 FAQ Chatbot — type 'quit' to exit")
    while True:
        query = input("You: ").strip()
        if query.lower() in ("quit", "exit"):
            print("Chatbot: Goodbye!")
            break
        q_match, answer, score = chatbot_response(query)
        print(f"Chatbot (match score {score:.2f}): {answer}\n  — matched FAQ: \"{q_match}\"\n")
