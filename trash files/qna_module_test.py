import qna
from transformers import pipeline
import fitz
import re


path = r'D:\Documents\My_projects\uploads\bkrdzqcqbmqd.pdf'
filename = 'bkrdzqcqbmqd.pdf'
qsn='what is your name ?'

print(qna.func(qsn,path,filename))