# 📰 News Category Classification App

A Machine Learning project that classifies news articles into four categories using **TF-IDF feature extraction** and **Logistic Regression / Support Vector Machine (SVM)** models.

The project also includes a simple **Streamlit web application** for real-time inference.

---

## 📌 Categories

- 🌍 World  
- ⚽ Sports  
- 💼 Business  
- 💻 Sci/Tech  

---

## 🚀 Project Pipeline

1. Data Loading (Predefined Train & Test files)
2. Text Preprocessing  
   - Lowercasing  
   - Removing punctuation  
   - Removing stopwords
   - Lemmatization  
3. Feature Extraction using **TF-IDF**
4. Model Training:
   - Logistic Regression
   - Linear SVM
5. Model Evaluation:
   - Accuracy comparison
   - Classification report
   - Confusion matrices
6. Inference function for unseen text
7. Deployment using Streamlit

---

## 📊 Model Comparison

| Model | Description |
|--------|------------|
| Logistic Regression | Strong baseline model for text classification |
| Linear SVM | High-performance classifier for high-dimensional TF-IDF features |

> In experiments, SVM achieved slightly higher accuracy.

---

## 🖥️ Streamlit App

The project includes an interactive web app where users can:

- Enter a news article  
- Click **Predict**  
- Instantly see the predicted category  

### ▶ Run the App Locally

```bash
pip install streamlit
python -m streamlit run app.py
