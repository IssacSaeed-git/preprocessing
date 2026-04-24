import pandas as pd
import numpy as np
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

df=pd.read_csv(r'C:\nlp files\archive2\netflix_titles_CLEANED.csv')
df.head()

# 1. Read dataset
df = pd.read_csv(r'C:\nlp files\archive2\netflix_titles_CLEANED.csv')

# "description" column as review_text
df = df[['description']].copy()
df.rename(columns={'description': 'review_text'}, inplace=True)

# review_id and a random rating (1–5)
df['review_id'] = range(1, len(df) + 1)
np.random.seed(42)
df['rating'] = np.random.randint(1, 6, size=len(df))

# Reorder columns
df = df[['review_id', 'rating', 'review_text']]

# 2. Remove missing values
df.dropna(subset=['review_text'], inplace=True)

# 3. Text Cleaning Functions
def clean_text(text):
    # Lowercase
    text = text.lower()
    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

stop_words = set(stopwords.words('english'))
ps = PorterStemmer()
lemm = WordNetLemmatizer()

def preprocess(text):
    # 1. Clean
    text = clean_text(text)
    # 2. Tokenize
    tokens = text.split()
    # 3. Remove stopwords
    tokens = [w for w in tokens if w not in stop_words]
    # 4. Stemming
    stemmed = [ps.stem(w) for w in tokens]
    # 5. Lemmatization
    lemmatized = [lemm.lemmatize(w) for w in stemmed]
    return " ".join(lemmatized)

# 4. Apply preprocessing to the dataset

df['cleaned_text'] = df['review_text'].apply(preprocess)

# 5. Save new cleaned CSV
output_path = r'C:\nlp files\archive2\netflix_reviews_CLEANED.csv'
df.to_csv(output_path, index=False)
df.head()


