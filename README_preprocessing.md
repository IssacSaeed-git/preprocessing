# 🧹 Text & Data Preprocessing Exercises

A set of small Python exercises on **text preprocessing for NLP** and a first **regression** model, written during my NLP course at the Faculty of Computers and Artificial Intelligence, Minia National University.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-text%20processing-green)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikitlearn&logoColor=white)

---

## 📂 What's inside

| File | Topic | What it does |
|------|-------|--------------|
| `task1 on dataPreprocessing_ex1,2.py` | 🔤 Text cleaning and sentiment | **Ex. 1:** lowercases a corpus, strips punctuation, tokenizes with NLTK, removes stopwords, counts word frequencies and plots the top 20 words. **Ex. 2:** rule-based sentiment analysis (positive / negative / neutral) on custom sentences, using word lists, with a bar chart of the results. |
| `task2 on dataPreprocessing_ex1,2.py` | 🔍 Regular expressions | Extracts **emails**, **dates** (`dd-mm-yyyy` / `dd/mm/yyyy`) and **numbers ≥ 100** from a text. Finds punctuation, **hashtags** and **@mentions** in a social-media style text. |
| `task3 on dataPreprocessing.py` | 🧼 Full text-cleaning pipeline | Builds a review-style table from the Netflix `description` column, then cleans it: lowercase → remove URLs, numbers, punctuation and extra spaces → tokenize → remove stopwords → **Porter stemming** → **WordNet lemmatization**. Saves the cleaned CSV. |
| `task4 on dataPreprocessing.py` | 🔢 Text vectorization | Turns the cleaned text into numeric features: **Bag of Words**, **TF-IDF** and **n-grams (1–2)**, each shown as a pandas DataFrame. |
| `task5 on dataPreprocessing.py` | 📈 Linear regression | Fits a `LinearRegression` model of **Canada's per-capita income vs. year**, plots the fit, predicts **2020** and **2025**, and saves the model with `joblib`. |

---

## 🛠️ Tech stack

- **Python**, **pandas**, **NumPy**
- **NLTK** (tokenization, stopwords, stemming, lemmatization)
- **scikit-learn** (`CountVectorizer`, `TfidfVectorizer`, `LinearRegression`)
- **Matplotlib**, **joblib**, `re` (regular expressions)

---

## ▶️ How to run

```bash
pip install pandas numpy nltk scikit-learn matplotlib joblib
python "task1 on dataPreprocessing_ex1,2.py"
```

For the NLTK scripts, download the resources once:

```python
import nltk
nltk.download("punkt"); nltk.download("punkt_tab")
nltk.download("stopwords"); nltk.download("wordnet")
```

> ⚠️ **Note on data paths:** tasks 3–5 read CSV files from local Windows folders (for example `C:\nlp files\archive2\netflix_titles_CLEANED.csv`). Update the path at the top of each script to where your copy of the data is.
> - `netflix_titles_CLEANED.csv` is available in my [Netflix-Content-Type-Classifier](https://github.com/IssacSaeed-git/Netflix-Content-Type-Classifier) repository.
> - Task 5 needs `canada_per_capita_income.csv`, which is not included here.
> - Task 4 reads the output of task 3, so run task 3 first.

---

## 📝 Notes

- In task 3, the `rating` column is **randomly generated** (seed 42) just to mimic a reviews table for the exercise. It is not real user data.
- These are learning exercises, so the sample texts are short on purpose.

---

## 👤 Author

**Issac Saeed Issac Ayad** · AI & Computer Science student, Minia National University
[GitHub](https://github.com/IssacSaeed-git) · [LinkedIn](https://www.linkedin.com/in/issac-saeed-63b0613b8)
