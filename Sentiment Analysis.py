#import libraries
import nltk
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy as nltk_accuracy
from nltk.corpus import stopwords
import random

# Download necessary NLTK data files
nltk.download('movie_reviews')
nltk.download('punkt')
nltk.download('stopwords')
import nltk
nltk.download('punkt_tab')

# preprocess the datasets and extract features

def extract_features(words):
    return {word: True for word in words}

    # Load movie reviews from NLTK corpus

documents = [(list(movie_reviews.words(fileid)), category)
                for category in movie_reviews.categories()
                for fileid in movie_reviews.fileids(category)]

# Shuffle the datasets to ensure randomness

random.shuffle(documents)

# prepare the dataset for training and testing

featuresets = [(extract_features(doc), category) for (doc, category) in documents]
train_set, test_set = featuresets[:1600], featuresets[1600:]

# Train the Naive Bayes classifier
classifier = NaiveBayesClassifier.train(train_set)

# Evaluate the classifier
accuracy = nltk_accuracy(classifier, test_set)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Show the most informative features    
classifier.show_most_informative_features(10)

# Function to predict sentiment of a given text
def analyze_sentiment(text):
    words = nltk.word_tokenize(text)
    words = [word for word in words if word.isalnum() and word.lower() not in stopwords.words('english')]
   
   #predict sentiment
    features = extract_features(words)
    return classifier.classify(features)

# test the classifier with custom input
text_sentences = [
    "I absolutely loved this movie! The plot was thrilling and the characters were well-developed.",
    "This was a terrible film. I wasted two hours of my life.",
    "An average movie with some good moments but overall forgettable.",
    "The cinematography was stunning, but the story was lacking depth.",
    "A heartwarming tale that left me in tears. Highly recommend!"
]     

for sentence in text_sentences:
    print(f'Sentence: "{sentence}" => Sentiment: {analyze_sentiment(sentence)}')
    print()