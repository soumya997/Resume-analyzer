from bs4 import BeautifulSoup
import requests
import urllib.request
import csv
main_url = 'https://www.overleaf.com/'
url = 'https://www.overleaf.com/latex/templates/tagged/cv/page/1'
page_url = 'https://www.overleaf.com/latex/templates/tagged/cv/page/'
file_type = '.pdf'

count=0

resume_csv = open('resume1.csv','w')
csv_writer = csv.writer(resume_csv)
csv_writer.writerow(['resume_text'])

for i in range(1,15):
    
    source = requests.get(page_url+str(i)).text

    page = BeautifulSoup(source,'lxml')


    for pages in page.find_all('div',class_="gallery-thumbnail"):
        for a_tags in pages.find_all('a'):
            try:
                num_url = a_tags.get('href')
                print(f'https://www.overleaf.com{num_url+file_type}')
                urllib.request.urlretrieve(f'https://www.overleaf.com{num_url+file_type}',num_url.split('/')[4]+file_type)
                test_pdf = pp.PdfFileReader(num_url.split('/')[4]+file_type)
                num_page = test_pdf.getNumPages()-1
                pdf_text = test_pdf.getPage(num_page).extractText()
                csv_writer.writerow([pdf_text])
                count=count+1
            except Exception as e:
                pass
resume_csv.close()
print(count)