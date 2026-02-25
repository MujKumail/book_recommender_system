# 📚 Book Recommender System

A Machine Learning based Book Recommendation Web Application built using Flask and deployed on Render.

This project recommends similar books based on collaborative filtering and cosine similarity.

---

## 🚀 Live Demo

🔗 https://your-render-link.onrender.com  

---

## 🧠 Project Overview

This system recommends books based on user selection using:

- Collaborative Filtering
- Cosine Similarity
- Precomputed similarity matrix
- Flask backend
- Bootstrap-based responsive UI

The model suggests top 4 similar books based on user input.

---

## 🛠️ Tech Stack

**Backend**
- Python
- Flask
- NumPy
- Pandas
- Pickle

**Frontend**
- HTML
- CSS
- Bootstrap
- Select2 (searchable dropdown)

**Deployment**
- GitHub
- Render
- Gunicorn

---

## 📊 How It Works

1. Dataset is preprocessed and pivot table is created.
2. Cosine similarity is computed between books.
3. Similarity matrix is stored using pickle.
4. When user selects a book:
   - Its index is retrieved.
   - Top 4 similar books are fetched.
   - Results are displayed dynamically.

---

## ✨ Features

- 🔎 Searchable book dropdown (Select2)
- 📈 Top popular books homepage
- 🎯 ML-based recommendations
- 📬 Contact form (CSV-based storage)

---


## 📁 Project Structure
