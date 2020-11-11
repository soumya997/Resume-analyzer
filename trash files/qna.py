from transformers import pipeline
import fitz
import re


def func(qsn,path,filename):
    
    contxt = red_pdf(path,filename) 
    return qsn,contxt
    
    

def red_pdf(path,filename):
    doc = fitz.open(path)
    text = ""
    
    for pages in doc:
        text = text + str(pages.getText())
    txt = " ".join(text.split("\n"))
    return txt
    



if __name__ == '__main__':
    
    # freeze_support()
    # def qsn_gen(qsn,path,filename):
    qsn, context = func(qsn,path,filename)
    nlp = pipeline('question-answering')
    ans = nlp({
        'question': qsn,
        'context': context
    })
    print(ans)
        
    
    
