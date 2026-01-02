from sklearn.feature_extraction.text import TfidfVectorizer

def build_tfidf(max_features=5000, ngram_range=(1, 2)):
    return TfidfVectorizer(
        stop_words="english",
        max_features=max_features,
        ngram_range=ngram_range,
        min_df=5
    )
