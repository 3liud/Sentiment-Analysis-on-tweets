import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

#data processing 
from textblob import TextBlob 
import re 
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer 
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

#model selection adn Validation
from sklearn.naive_bayes import MultinomialNB 
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline 
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

# Reading the data into pandas

training_set = pd.read_csv('train_tweets.csv')
testing_set = pd.read_csv('test_tweets.csv')

# EDA
sns.barplot('label','length', data = training_set, palette='PRGn')

