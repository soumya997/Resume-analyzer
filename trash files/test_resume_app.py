import re
import spacy
import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
import fitz
from werkzeug.utils import secure_filename
import pickle
import nltk 
import numpy as np                                  
import pandas as pd
from nltk.corpus import stopwords
from sklearn.ensemble import RandomForestClassifier
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer     
import pdb
import logging
from werkzeug.debug import DebuggedApplication  
from transformers import pipeline


path=""
filename=""
qsn=""

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

application = DebuggedApplication(app, True)

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def welcome():
    return render_template('index_resume.html')
    
    
@app.route('/form',methods=['POST'])
def resume_main():
    if request.method=='POST':
        if request.method=='POST':
            file = request.files['file']
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            result = int(prediction(path,filename))+1
            print(request.form)
    return render_template('index_resume.html',filename_fe=filename,path_fe=path,result_fe="Your score is {}".format(result))
    
    
@app.route('/summ',methods=['POST'])
def resume_main2():
    if request.method=='POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        cus_ents = custom_NER(path,filename)
        print(cus_ents)

        
    return render_template('index_resume.html',ents_fe=cus_ents)


@app.route('/qna',methods=['POST'])
def resume_main3():
    if request.method=='POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        qsn = request.form['queation']
        
        print(qsn)
        
        

        
    return render_template('index_resume.html')



 

def red_pdf(path,filename):
    doc = fitz.open(path)
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
    model = spacy.load('resume_sum1')
    txt=red_pdf(path,filename)
    doc = model(txt)
    abc = doc.ents
    return abc
    
    
    
    
    
    


if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port='8080', debug=True)
    contxt = red_pdf(path,filename)
    nlp = pipeline('question-answering')
    ans = nlp({
        'question': qsn,
        'context': contxt
    })
    print(ans['answer'])
