# Exercise 1: Clean a text corpus and visualize word frequencies

import nltk
import matplotlib.pyplot as plt
from collections import Counter
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

# Sample text
text_corpus = """
Natural language processing is a fascinating field of artificial intelligence.
It helps computers understand, interpret, and manipulate human language.
Python provides excellent libraries for text processing and analysis.
Machine learning models can be trained to perform various NLP tasks.
Sentiment analysis is one popular application of natural language processing.
Text cleaning is an important first step in any NLP pipeline.
We need to remove punctuation, stopwords, and normalize the text.
Word frequency analysis helps us understand the most important terms.
"""

# Clean & Convert to lowercase
text_lower = text_corpus.lower()

# Remove punctuation & special characters
text_clean = re.sub(r'[^\w\s]', '', text_lower)

# Tokenize
tokens = word_tokenize(text_clean)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word not in stop_words and len(word) > 2]

# word frequencies
word_freq = Counter(filtered_tokens)

# the top 20 words
top_words = word_freq.most_common(20)

if top_words:
    words, frequencies = zip(*top_words)

    plt.figure(figsize=(12, 8))
    plt.bar(words, frequencies, color='skyblue')
    plt.title('Top 20 Word Frequencies in the Corpus')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()
else:
    print("No words available for visualization.")

# results
print("Exercise 1: Clean a text corpus and visualize word frequencies")
print("=" * 60)
print(f"Original tokens: {len(tokens)}")
print(f"Filtered tokens (after cleaning): {len(filtered_tokens)}")
print("\nTop 10 most frequent words:")
for word, freq in word_freq.most_common(10):
    print(f"  {word}: {freq}")
    
# --------------------------------------------------------------------------------------
# Exercise 2: write a python program to perform a Basic Sentiment Analysis on a list of text sentences

import matplotlib.pyplot as plt
import re

# Define positive & negative word
positive_words = {
    'good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic',
    'awesome', 'brilliant', 'love', 'like', 'happy', 'joy', 'pleased',
    'perfect', 'beautiful', 'nice', 'positive', 'success', 'win'
}

negative_words = {
    'bad', 'terrible', 'awful', 'horrible', 'hate', 'dislike',
    'angry', 'sad', 'unhappy', 'poor', 'worst', 'negative',
    'failure', 'lose', 'problem', 'issue', 'wrong', 'broken'
}

custom_sentences = [
    "I really enjoy learning Python programming",
    "This weather makes me feel miserable",
    "The results were acceptable but not great",
    "I absolutely adore this new restaurant",
    "The traffic today was horrible and frustrating"
]

print("Custom Sentiment Analysis with Your Sentences:")
print("=" * 50)

# Reset counters for custom analysis
custom_sentiment_counts = {'Positive': 0, 'Negative': 0, 'Neutral': 0}

for i, sentence in enumerate(custom_sentences, 1):
    # Clean text
    clean_sentence = re.sub(r'[^\w\s]', '', sentence.lower())
    words = clean_sentence.split()

    # Count positive & negative words
    positive_count = sum(1 for word in words if word in positive_words)
    negative_count = sum(1 for word in words if word in negative_words)

    # Classify sentiment
    if positive_count > negative_count:
        sentiment = 'Positive'
        custom_sentiment_counts['Positive'] += 1
    elif negative_count > positive_count:
        sentiment = 'Negative'
        custom_sentiment_counts['Negative'] += 1
    else:
        sentiment = 'Neutral'
        custom_sentiment_counts['Neutral'] += 1

    print(f"{i}. \"{sentence}\"")
    print(f"   → {sentiment} (Positive: {positive_count}, Negative: {negative_count})")

# Visualize custom results
custom_sentiments = list(custom_sentiment_counts.keys())
custom_counts = list(custom_sentiment_counts.values())

plt.figure(figsize=(8, 5))
bars = plt.bar(custom_sentiments, custom_counts, color=['green', 'red', 'blue'])

for bar, count in zip(bars, custom_counts):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
            str(count), ha='center', va='bottom', fontweight='bold')

plt.title('Custom Sentences Sentiment Distribution', fontweight='bold')
plt.xlabel('Sentiment', fontweight='bold')
plt.ylabel('Count', fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# results
print("\nresults:")
print(f"Positive: {custom_sentiment_counts['Positive']} sentences")
print(f"Negative: {custom_sentiment_counts['Negative']} sentences")
print(f"Neutral: {custom_sentiment_counts['Neutral']} sentences")
