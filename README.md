# Emotion_Diary

<p align="center">
    I had used the model of Yuedong Chen from his article Official PyTorch Implementation of **Facial Motion Prior Networks for Facial Expression Recognition** by <a href="https://donydchen.github.io">Yuedong Chen</a>, <a href="https://jianfeng1991.github.io/personal">Jianfeng Wang, <a href="https://www.researchgate.net/profile/Shikai_Chen3">Shikai Chen</a>, Zhongchao Shi, and <a href="https://www.ntu.edu.sg/home/asjfcai/">Jianfei Cai</a>. 
<br>VCIP 2019, Oral, \[[arXiv](https://arxiv.org/abs/1902.08788)\]
 
</p>

---

<div align="center">
<a href="https://www.youtube.com/channel/UCzRuHTZpfoag9ky3P0UCFgg" target="_blank"><img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
<a href="https://www.youtube.com/channel/UCzRuHTZpfoag9ky3P0UCFgg" target="_blank"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python"></a>
<a href="https://www.youtube.com/channel/UCzRuHTZpfoag9ky3P0UCFgg" target="_blank"><img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"></a>
<a href="https://www.twitter.com/mercy_thuyle" target="_blank"><img src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"></a>
<a href="https://www.facebook.com/Mercy.ThuyLe" target="_blank"><img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1" alt="JaveScript"></a>
<a href="https://www.facebook.com/Mercy.ThuyLe" target="_blank"><img src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white" alt="CSS"></a>
<a href="https://www.facebook.com/Mercy.ThuyLe" target="_blank"><img src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white" alt="VS Code"></a>
</div>

#### To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

``` sh
pip install virtualenv
```

#### Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

``` sh
virtualenv env
```

#### Check and set ExecutionPolicy on Windows follow this tutorial:

``` sh
1. Open VSCode as Adminstrator
2. Open Terminal
3. Type <powershell>
4. Type <Get-ExecutionPolicy>. If it return Restricted, continue to next step
5. Type <Set-ExecutionPolicy –ExecutionPolicy RemoteSigned>
6. Check again by type <Get-ExecutionPolicy>
7. Close VSCode and open normal again.
```

#### That will create a new folder env in your project directory. Next activate it with this command on Windows:

``` sh
1. env\Scripts\activate
2. or: e:/THESIS/GITHUB/Emotion_Diary/env/Scripts/Activate.ps1
```

or Mac/Linux:

``` sh
source env/bin/active
```

#### Deactivate it with this command on Windows:

``` sh
deactivate
```

#### Then install the project dependencies with

``` sh
pip install -r requirements.txt
```

#### Now you can run the project with this command on Window

### Run in python console

``` sh
python run.py
```

### Run in flask console

```sh
$env:FLASK_APP = ".\run.py"
$env:FLASK_ENV = "development"
flask shell or flask run
from apps import db
db.create_all()
from apps.authentication.models import Users, Emotions, Diaries
emo_an = Emotions(0,'Anger')
emo_co = Emotions(1, 'Contempt')
emo_di = Emotions(2, 'Disgust')
emo_fe = Emotions(3, 'Fear')
emo_ha = Emotions(4, 'Happy')
emo_sa = Emotions(5, 'Sad')
emo_su = Emotions(6, 'Surprise')
emo_ne = Emotions(7, 'Neutral')
dia_1 = Diaries(id=1, uid=3, eid=5, imgname='20211209-132000.png', title='Thesis', contents='I feel so stressfull and confused about machine learning. T_T')
db.session.add(emo_an)
db.session.add(emo_co)
db.session.add(emo_di)
db.session.add(emo_fe)
db.session.add(emo_ha)
db.session.add(emo_sa)
db.session.add(emo_su)
db.session.add(emo_ne)
db.session.add(dia_1)
db.session.commit()
```

**Note** if you want payments to work you will need to enter your own Stripe API keys into the `.env` file in the settings files.

```bash
api-server-flask/
├── api
│   ├── config.py
│   ├── __init__.py
│   ├── models.py
│   └── routes.py
├── Dockerfile
├── README.md
├── requirements.txt
├── run.py
└── tests.py
```

```bash
< PROJECT ROOT >
   |
   |-- apps/
   |    |
   |    |-- home/                          # A simple app that serve HTML files
   |    |    |-- routes.py                 # Define app routes
   |    |
   |    |-- authentication/                # Handles auth routes (login and register)
   |    |    |-- routes.py                 # Define authentication routes  
   |    |    |-- models.py                 # Defines models  
   |    |    |-- forms.py                  # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |    |    |-- includes/                 # HTML chunks and components
   |    |    |    |-- navigation.html      # Top menu component
   |    |    |    |-- sidebar.html         # Sidebar component
   |    |    |    |-- footer.html          # App Footer
   |    |    |    |-- scripts.html         # Scripts common to all pages
   |    |    |
   |    |    |-- layouts/                   # Master pages
   |    |    |    |-- base-fullscreen.html  # Used by Authentication pages
   |    |    |    |-- base.html             # Used by common pages
   |    |    |
   |    |    |-- accounts/                  # Authentication pages
   |    |    |    |-- login.html            # Login page
   |    |    |    |-- register.html         # Register page
   |    |    |
   |    |    |-- home/                      # UI Kit Pages
   |    |         |-- index.html            # Index page
   |    |         |-- 404-page.html         # 404 page
   |    |         |-- *.html                # All other pages
   |    |    
   |  config.py                             # Set up the app
   |    __init__.py                         # Initialize the app
   |
   |-- requirements.txt                     # Development modules - SQLite storage
   |-- requirements-mysql.txt               # Production modules  - Mysql DMBS
   |-- requirements-pqsql.txt               # Production modules  - PostgreSql DMBS
   |
   |-- Procfile                             # Deployment
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- run.py                               # Start the app - WSGI gateway
   |
   |-- ************************************************************************
```

```bash
< PROJECT ROOT >
   |
   |-- apps/
   |    |
   |    |-- authentication/     # Handles auth routes (login and register)
   |         |-- routes.py      # Define authentication routes  
   |         |-- models.py      # Defines models  
   |         |-- forms.py       # Define auth forms (login and register) 
   |
   |-- **************************
```

```bash
< PROJECT ROOT >
   |
   |-- apps/
   |    |
   |    |-- home/                          # A simple app that serve HTML files
   |    |    |-- routes.py                 # Define app routes
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |         |-- includes/                 # HTML chunks and components
   |         |    |-- navigation.html      # Top menu component
   |         |    |-- sidebar.html         # Sidebar component
   |         |    |-- footer.html          # App Footer
   |         |    |-- scripts.html         # Scripts common to all pages
   |         |
   |         |-- layouts/                   # Master pages
   |         |    |-- base-fullscreen.html  # Used by Authentication pages
   |         |    |-- base.html             # Used by common pages
   |         |
   |         |-- accounts/                  # Authentication pages
   |         |    |-- login.html            # Login page
   |         |    |-- register.html         # Register page
   |         |
   |         |-- home/                      # UI Kit Pages
   |              |-- index.html            # Index page
   |              |-- 404-page.html         # 404 page
   |              |-- *.html                # All other pages
   |
   |
   |-- **************************************
```

<div align="center">

<i>Find me here:</i><br>

<a href="https://www.youtube.com/channel/UCzRuHTZpfoag9ky3P0UCFgg" target="_blank"><img src="https://img.shields.io/badge/YouTube-%23E4405F.svg?&style=flat-square&logo=youtube&logoColor=white" alt="YouTube"></a>
<a href="https://www.twitter.com/mercy_thuyle" target="_blank"><img src="https://img.shields.io/badge/Twitter-%231877F2.svg?&style=flat-square&logo=twitter&logoColor=white" alt="Twitter"></a>
<a href="https://www.facebook.com/Mercy.ThuyLe" target="_blank"><img src="https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=Facebook&logoColor=white" alt="Facebook"></a>
<a href="https://www.youtube.com/channel/UCzRuHTZpfoag9ky3P0UCFgg" target="_blank"><img src="https://img.shields.io/badge/%3CServer%3E-%237289DA.svg?style=for-the-badge&logo=discord&logoColor=white" alt="Discord"></a>
<a href="https://www.youtube.com/channel/UCzRuHTZpfoag9ky3P0UCFgg" target="_blank"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail"></a>
<a href="https://www.youtube.com/channel/UCzRuHTZpfoag9ky3P0UCFgg" target="_blank"><img src="https://img.shields.io/badge/Microsoft_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white" alt="OutLook"></a>
<a href="https://www.youtube.com/channel/UCzRuHTZpfoag9ky3P0UCFgg" target="_blank"><img src="hhttps://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="Linkedin"></a>
<a href="https://www.youtube.com/channel/UCzRuHTZpfoag9ky3P0UCFgg" target="_blank"><img src="https://img.shields.io/badge/Reddit-FF4500?style=for-the-badge&logo=reddit&logoColor=white" alt="Reddit"></a>
</div>