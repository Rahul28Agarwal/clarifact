# Clarifact
> Over the last few years, fake news has become an everyday expression. since 2019, we are not only dealing with a pandemic, we are also facing an infodemic era. At Clarifact, we developed an educational platform specifically for the aged group of 60+. It is a web-based educational platform that provides an easy 7-steps strategy to shield you from fake News. If you are unsure, use our platform to get a more accurate understanding of whether your reading real news or is it fake. 



## Requirements  (Prerequisites)
Tools and packages required to successfully install this project.
For example:
* Django [Install](https://docs.djangoproject.com/en/3.2/topics/install/)
* Python 3.8 and up [Install](https://link-for-setup-guide)

## Installation
A step by step list of commands / guide that informs how to install an instance of this project. 

1. Verify Python Installation

`$ python -V `

2. Upgrade Pip

`$ python -m pip install --upgrade pip`

3. Create Virtual Environment

`$ python -m venv env`

4. Activate Virtual EnvironmentPermalink

`source env/bin/activate`

5. Install Django

`pip install django`

6. Install the dependencies
`(env)$ pip install -r requirements.txt`

7. Once pip has finished downloading the dependencies
`(env)$ cd clarifact`
`(env)$ python manage.py runserver`


 
## After installation
After setup we will see on the web-browser

![Screenshots of projects](https://raw.githubusercontent.com/rahul28aggarwal/clarifact/master/clarifact/clarifact_app/static/images/slider/news_analyzer.png)

![Screenshots of the project](https://raw.githubusercontent.com/rahul28aggarwal/clarifact/master/clarifact/clarifact_app/static/images/slider/Screenshot%202021-05-22%20100114.png)

## Features
The website has to hero features
* Educate yourself:- At Clarifact, we aspire our readers to be well aware and make educated choices after reading each article. We provide a brief study on how to differentiate real and fake news
* News Analyzer:- The Fake News detector allows the user to distinguish whether the news article is genuine or not. Users can provide information such as news title, news description, author name, source URL, and their bias to recognize the authenticity of the article.


## Tech Stack / Built With
List down the technology / frameworks / tools / technology you have used in this project.
1. [Django]- The Python framework
2. [Passive Aggressive Classifiers]- Machine learning algorithm to detect the analomly in the news content
3. [SENTIMENTAL ANALYSIS USING VADER] - Machine learning algorithm to detect the sentiment of the news.
