import streamlit as st
import joblib
import re

# ------------------------
# Load Model & Vectorizer
# ------------------------
model = joblib.load("svm_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# ------------------------
# Class Mapping
# ------------------------
class_mapping = {
    1: "World",
    2: "Sports",
    3: "Business",
    4: "Sci/Tech"
}

# ------------------------
# Text Cleaning Function
# ------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text

# ------------------------
# Prediction Function
# ------------------------
def predict_news(text):
    cleaned = clean_text(text)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)[0]
    return class_mapping.get(prediction, "Unknown")

# ------------------------
# Streamlit UI
# ------------------------
st.title("📰 News Category Classifier")
st.write("Enter a news article and the model will classify it.")

user_input = st.text_area("Enter News Text")

if st.button("Predict"):
    if user_input.strip() != "":
        category = predict_news(user_input)
        st.success(f"Predicted Category: {category}")
    else:
        st.warning("Please enter some text.")