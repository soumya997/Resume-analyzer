[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/soumya997/resume-analyzer/main/Resume_analyzer_app.py)

<p align="center">
<img src="https://i.imgur.com/BcPSOvq.png" width="400">
<br/>
<a href=""><img alt="Contributions Welcome" src="https://img.shields.io/badge/contributions-welcome-brightgreen?style=for-the-badge&labelColor=black&logo=github"></a>
<br/>
<img alt="GitHub" src="https://img.shields.io/github/license/soumya997/Resume-analyzer?style=for-the-badge">
<p align="center">

 <img src="https://forthebadge.com/images/badges/built-with-love.svg"> <img src="https://forthebadge.com/images/badges/made-with-python.svg"> <img src="https://forthebadge.com/images/badges/open-source.svg"> <img src="https://forthebadge.com/images/badges/made-with-reason.svg">

</p>

<i>Resume Analyzer is a tool for recruiters which can help them to select candidates based on their resume and it also helps by providing a overall summary of the resume using which recruiters can know that individual in a more better way in less time.</i>

</p>


# About the Project🌟:
The whole application is having two tools right now,
1. Resume Score Generator
2. Resume Summarizer

**Resume Score Generator**: Its a NLP classification problem usecase, where multiple resumes are taken and a certaing score(between 1 to 10) is assigned. And a classification model is trained to classify any resume between 1 to 10. and this score is the score what they get for their resume.Total data points was 300+.file name is `resume_data2_(used in training).csv` and its under `data` folder.
**Resume Summarizer**: Custom NER is used to summarize any resume. Its done using spacy. Data for this provided in the `data` folder,file name is `train_data.pkl`. Total custom tagged data is 150+.



# User Interface📱:
<pre>
<img src="https://i.imgur.com/V9hXoqu.png" width="900"> <img src="https://i.imgur.com/buS9WTx.png" width="900"> <img src="https://i.imgur.com/a5hXSTc.png" width="900"> <img src="https://i.ibb.co/WWxq1mv/Screenshot-798.png" width="900">

</pre>




# Project workflow🧾: 


### Data Preparation:
1. I scraped app the sample resumes from overlife.com using the `pdf scraper.py` file.And parsed all the text from each resume. The resumes from this source is mostly for Engineering and programming field.And data quality is not so good.
2. I took some data from [here](https://github.com/laxmimerit/Resume-and-CV-Summarization-and-Parsing-with-Spacy-in-Python) also. Most of the resume of this source is for software development and data analyst role.
3. There was almost 300+ resumes(122 by scrapping and ~200 from the above repo), I did not get chance to label all the data to I randomly assigned some score from 1 to 10. 
4. Created a csv file combining all the data source.
5. Data from above repo is already tagged for NER so i did not do that.

### Model Building:
1. For classificating I tried RNNs but as the dataset size was too less deep learning was working poor. I tried different ML models like `random forest` ,`naive bayes classifier`, `random forest with RandomizedSearchCV`. As we were having `accurecy_score` as the evaluation method so i went with random forest as it was giving more accuracy.(The dataset is not so balanced and upsampling, weighted baised approach can be applied and some different method of evaluation could be applied like `recall` or `f1` but because of some time constraints I was unable to do that). Notebook is provided under `Notebooks` folder,file name is `classification model training notebook.ipynb`.

2. For Custom NER I used Spacy to do that. As per the Spacy docs they used Convolutional layers with residual connections, layer normalization and maxout non-linearity are used,which giving much better efficiency than the standard BiLSTM solution.[Source](https://spacy.io/models)

### Model Deployment:
1. For that I went with `flask` 1st, but as the UI was not good so, finally i switched to `streamlit`. The python file for flask and streamlit are present in the repo.
2. As it was a streamlit app, and as I just got the approval to use their deployment plateform from the `streamlit` team itself. So, I decided to use that. You can see the deployed app [here](https://share.streamlit.io/soumya997/resume-analyzer/main/Resume_analyzer_app.py).

<!-- 2. I have also Containerized the whole app using `Docker`. So you can that also to get the app locally. -->

### Documentation:
In the form of readme I am providing the details of the project. Below, I also have provided that ditails explanation for the file structure and how you can run the application locally.

# Future Improvements✊"
1. Making the models more robust.As its not right now, because of some reason

1.1. Data is not labeled correctly.
1.2. Dataset is imbalanced,
```
df5['score'].value_counts()
```
```
1    47
7    39
9    35
3    33
5    32
0    32
4    31
8    28
2    22
6    20
Name: score, dtype: int64
```
1.3. Adding More data in the dataset for both the task.

2. Adding a QnA based model for easy query search option. As it will provide the user to make some query in the form of a question and extract answer in the form of model output. It will help people to search specific things from the resume.

3. Migrate the webapp from sreamlit to flask.Add some good UI.
4. Containerizing the project.
<BR>

**NOTE:** <i>If you can implement any of the above mentioned feature, please feel free to make a PR. Except, that if you have any problem understanding the above mentioned features feel free to creat an issue.</i>

# File Structure📂:
|File/Folder Name| Usage of that file/folder|
|----------------|--------------------------|
|Notebooks|Data collection,Model training every thing is done in the ipynbs,file names are self explanatory so, you will be understand their usage|
|data|All the CSV and the tagged data is provided here|
|data/resume_data2_(used in training).csv|is used for classification|
|data/train_data.pkl|Used for NER|
|rf_score_model.pkl/tfidf_vectorizer.pkl| Used for classification model training|
|Resume_analyzer_app.py|is the streamlit app|
|resume_app_main_flask.py|flask app|
|pdf scraper.py|for scrap pdfs|
|Dockerfile| is the Dockerfile|

**Note**: if you dont get the file structure currect feel free to make an issue.

# Run Locally💻:
<!--1. **Using `Docker`:**

1.1 `git clone <repo link>`

1.2 `cd Resume-analyzer`

1.3 `Docker build -t "<give_some_name>" .`

1.4 `Docker run -ti "<provided_name>"`
-->

 1. **Run Locally:**

1.1 `git clone <repo link>`

1.2 `cd Resume-analyzer`

1.3 `pip install -r requirements.txt `

1.4 `streamlit run <file_name>`

# Connect with me If you need any help🤝:

<br>

<a href="https://twitter.com/Soumya997Sarkar"><img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/Soumya997Sarkar?style=for-the-badge&color=09f&labelColor=black&logo=twitter&label=@Soumya997Sarkar"></a>
<a href="https://www.linkedin.com/in/soumyadip-sarkar-173901183/" target="blank"><img align="left" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/linkedin.svg" alt="xtenzq" width="22px" />
<img alt="GitHub followers" src="https://img.shields.io/github/followers/soumya997?color=green&logo=github&style=for-the-badge">
[![Gmail](https://img.shields.io/badge/-soumyadip-c14438?style=for-the-badge&logo=Gmail&logoColor=white)](mailto:soumya997.sarkar@gmail.com)


<br>







