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
import logging

logging.basicConfig(filename='test_resume.log',level=logging.DEBUG,
                    format='%(levelname)s:%(filename)s:%(funcName)s:%(message)s')

# result=None
# filename=None


UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
# DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'
ALLOWED_EXTENSIONS = {'pdf', 'txt'}

app = Flask(__name__, static_url_path="/static")
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 8*1024*1024

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    result=None
    # cus_ents = ()
    filename= None
    path=None
    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file attached in request')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print('No file selected')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            
            filename = secure_filename(file.filename)
            print(filename)
            print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            result = prediction(os.path.join(app.config['UPLOAD_FOLDER'],filename),filename)
            # return redirect(url_for('uploaded_file', filename=filename))
            
            result = int(result)+1
            logging.debug('result:{},filename: {}'.format(result,filename))
            if request.form['Summarization'] == 'Summarize':
                cus_ents = custom_NER(os.path.join(app.config['UPLOAD_FOLDER'], filename),filename)
                # logging.debug('result:{},filename: {},cus_ents: {}'.format(result,filename,cus_ents))
            
            
            

        return render_template('index_resume.html',pred_result='Your score is {}'.format(result),doc_ents=cus_ents)
    # else:
        # return render_template('index_resume.html')




def custom_NER(path,filename):
    model = spacy.load('resume_sum')
    txt=red_pdf(path,filename)
    
    
    doc = model(txt)
    
    ents = doc.ents
    # print(ents)
    lists = []
    ents=list(ents)
    for i in range(len(ents)):
        lists.append(str(ents[i]))
    print(tuple(lists))
    
    return lists
    
    

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
    
    


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port,debug=config.DEBUG_MODE)

    
    
    
    
    
    

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

