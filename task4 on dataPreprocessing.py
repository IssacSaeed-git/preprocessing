import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

df = pd.read_csv(r"C:\Users\Royal\OneDrive\Desktop\NLP\database files\archive2\netflix_reviews_CLEANED.csv")
texts = df["cleaned_text"].astype(str).tolist()

# 1) BAG OF WORDS (CountVectorizer)

bow_vectorizer = CountVectorizer(stop_words='english')
bow_matrix = bow_vectorizer.fit_transform(texts)
bow_columns = bow_vectorizer.get_feature_names_out()

bow_df = pd.DataFrame(bow_matrix.todense(), columns=bow_columns, index=texts)
print("Bag of Words DataFrame:")
print(bow_df)

# 2) TF-IDF (TfidfVectorizer)

tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(texts)
tfidf_columns = tfidf_vectorizer.get_feature_names_out()

tfidf_df = pd.DataFrame(tfidf_matrix.todense(), columns=tfidf_columns, index=texts)
print("TF-IDF DataFrame:")
print(tfidf_df)

# 3) N-GRAMS (1–2 grams)

ngram_vectorizer = CountVectorizer(stop_words='english', ngram_range=(1, 2))
ngram_matrix = ngram_vectorizer.fit_transform(texts)
ngram_columns = ngram_vectorizer.get_feature_names_out()

ngram_df = pd.DataFrame(ngram_matrix.todense(), columns=ngram_columns, index=texts)
print("N-grams DataFrame:")
print(ngram_df)
