import streamlit as st
import string
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# --- Setup ---
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)
stop_words = set(stopwords.words("english"))

# --- FAQ dataset ---
faqs = {
    "What is your return policy?": "You can return any item within 30 days of purchase for a full refund. Items must be in original condition with tags attached.",
    "How do I track my order?": "Use the tracking link sent to your email after purchase. You can also track your order by logging into your account and visiting 'My Orders' section.",
    "Do you offer international shipping?": "Yes! We ship worldwide. International shipping fees vary by location and are calculated at checkout.",
    "How do I contact support?": "You can reach our support team via:\n• Email: support@example.com\n• Phone: +1-555-555-5555\n• Live chat: Available Mon-Fri 9AM-5PM EST",
    "What payment methods do you accept?": "We accept Visa, MasterCard, American Express, PayPal, and Apple Pay.",
    "How long does shipping take?": "Standard shipping takes 5-7 business days. Express shipping (2-3 days) is available for an additional fee.",
    "Can I cancel my order?": "Orders can be cancelled within 24 hours of placement. After that, you'll need to wait for delivery and initiate a return.",
    "Do you have a loyalty program?": "Yes! Join our rewards program to earn points on every purchase. 100 points = $5 off your next order.",
    "hello": "Hi there! Welcome to our FAQ Assistant. How can I help you today?",
    "hi": "Hello! I'm here to help answer your questions. What would you like to know?",
    "thanks": "You're welcome! Is there anything else I can help you with?",
    "thank you": "My pleasure! Feel free to ask if you have any other questions.",
    "bye": "Goodbye! Have a great day!",
    "help": "I can help you with questions about:\n• Orders and shipping\n• Returns and refunds\n• Payment methods\n• Customer support\n• And more! Just ask your question.",
}

# --- Preprocessing ---
def preprocess(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in string.punctuation]
    tokens = [t for t in tokens if t not in stop_words]
    return " ".join(tokens)

# Prepare data
questions = list(faqs.keys())
processed_questions = [preprocess(q) for q in questions]
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(processed_questions)

# Chatbot logic
def chatbot_response(user_input):
    user_proc = preprocess(user_input)
    user_vec = vectorizer.transform([user_proc])
    similarities = cosine_similarity(user_vec, faq_vectors)
    best_idx = similarities.argmax()
    best_score = similarities[0, best_idx]
    
    if best_score < 0.15:
        return None, "I'm not quite sure about that. Could you rephrase your question? Or type 'help' to see what I can assist with.", best_score
    
    return questions[best_idx], faqs[questions[best_idx]], float(best_score)

# --- Streamlit UI ---
st.set_page_config(
    page_title="FAQ Assistant", 
    page_icon="🤖", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS ---
st.markdown("""
    <style>
    #MainMenu, footer {visibility: hidden;}

    .stApp {
        background: #0E1117;
        color: #E0E0E0;
        font-family: 'Segoe UI', Tahoma, sans-serif;
    }

    h1 {
        color: #FFFFFF;
        text-align: center;
        margin-bottom: 0.5rem;
    }

    .subtitle {
        color: #A0A0A0;
        text-align: center;
        margin-bottom: 2rem;
        font-size: 1.1rem;
    }

    /* Chat bubbles */
    .chat-message {
        display: flex;
        align-items: flex-start;
        margin-bottom: 16px;
    }

    .chat-avatar {
        width: 38px;
        height: 38px;
        border-radius: 50%;
        margin-right: 12px;
    }

    .chat-bubble {
        padding: 12px 16px;
        border-radius: 14px;
        max-width: 75%;
        font-size: 0.95rem;
        line-height: 1.5;
    }

    .user-bubble {
        background: #1E88E5;
        color: white;
        margin-left: auto;
        margin-right: 0;
    }

    .bot-bubble {
        background: #2C2C2C;
        color: #E0E0E0;
        margin-right: auto;
        margin-left: 0;
    }

    /* Buttons */
    .stButton > button {
        background: #1E1E1E;
        color: #FFFFFF;
        border: 1px solid #333;
        border-radius: 8px;
        padding: 8px 16px;
        transition: 0.2s;
    }
    .stButton > button:hover {
        background: #333;
        border-color: #555;
    }
    </style>
""", unsafe_allow_html=True)

# --- Avatar URLs ---
USER_AVATAR = "https://cdn-icons-png.flaticon.com/512/847/847969.png"
BOT_AVATAR = "https://cdn-icons-png.flaticon.com/512/4712/4712109.png"

# --- Chat Layout ---
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.title("FAQ Assistant")
    st.markdown('<p class="subtitle">Dark mode assistant to answer your questions instantly</p>', unsafe_allow_html=True)
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.messages.append({"role": "bot", "content": "Hi! I'm your FAQ Assistant. Ask me about orders, shipping, returns, payments, and more."})
    
    # Render chat history
    for msg in st.session_state.messages:
        avatar = BOT_AVATAR if msg["role"] == "bot" else USER_AVATAR
        bubble_class = "bot-bubble" if msg["role"] == "bot" else "user-bubble"
        st.markdown(
            f"""
            <div class="chat-message">
                <img class="chat-avatar" src="{avatar}" />
                <div class="chat-bubble {bubble_class}">{msg["content"]}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Chat input
    if prompt := st.chat_input("Type your question here..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        matched_question, response, confidence = chatbot_response(prompt)
        st.session_state.messages.append({"role": "bot", "content": response})
        st.rerun()

    # Quick action buttons
    st.markdown("---")
    st.markdown("**Quick Questions:**")
    
    col_btn1, col_btn2, col_btn3 = st.columns(3)
    with col_btn1:
        if st.button("Return Policy"):
            st.session_state.messages.append({"role": "user", "content": "What is your return policy?"})
            st.rerun()
    with col_btn2:
        if st.button("Track Order"):
            st.session_state.messages.append({"role": "user", "content": "How do I track my order?"})
            st.rerun()
    with col_btn3:
        if st.button("Payment Methods"):
            st.session_state.messages.append({"role": "user", "content": "What payment methods do you accept?"})
            st.rerun()

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()
