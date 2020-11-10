import re
import spacy
import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
import fitz
from werkzeug.utils import secure_filename
import pickle
import nltk 
import numpy as np                                  #for large and multi-dimensional arrays
import pandas as pd
from nltk.corpus import stopwords
from sklearn.ensemble import RandomForestClassifier
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer     
import pdb


path = r'D:\Documents\NLP project\uploads'
filename = 'dhmkrwtksdgy.pdf'



def red_pdf(path,filename):
    doc = fitz.open((os.path.join(path,filename)))
    text = ""
    
    for pages in doc:
        text = text + str(pages.getText())
    txt = " ".join(text.split("\n"))
    return txt
    


def gen_test_data_for_pred(path,filename):
    test = red_pdf(path,filename)
    snow = nltk.stem.SnowballStemmer('english')
    corpus_test = []
    # for i in range(0, len(df)):
    review = re.sub('[^a-zA-Z]', ' ', test)
    review = review.lower()
    review = review.split()
        
    review = [snow.stem(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    corpus_test.append(review)

    final_tf_test = corpus_test
    # tf_idf = TfidfVectorizer(ngram_range=(1,2),max_features=5000)
    tf_idf = pickle.load(open('tfidf_vectorizer.pkl','rb'))
    test_data = tf_idf.transform(final_tf_test)
    # tf_data_test.get_shape()
    return test_data

    
def prediction(path,filename):
    clf_model = pickle.load(open('rf_score_model.pkl','rb'))
    result = clf_model.predict(gen_test_data_for_pred(path,filename))
    return result
    
    
def custom_NER(path,filename):
    model = spacy.load('resume_sum')
    txt=red_pdf(path,filename)
    
    # snow = nltk.stem.SnowballStemmer('english')
    # corpus_test_ner = []
    # review = re.sub('[^a-zA-Z]', ' ', txt)
    # review = review.lower()
    # review = review.split()
        
    # review = [snow.stem(word) for word in review if not word in stopwords.words('english')]
    # review = ' '.join(review)
    # corpus_test_ner.append(review)
    # corpus_test_ner = str(corpus_test_ner)
    doc = model(txt)
    abc = doc.ents
    return abc
    
    
    
    
    
    
    
    
if __name__=='__main__':
    s = custom_NER(path,filename)
    # print(int(s))
    print(s)

