from django.shortcuts import render
from django.http import HttpResponseRedirect
from clarifact_app.form import author_form
from clarifact_app.form import source_form
from clarifact_app.form import fake_news_form
from django.http import HttpResponse
from django.shortcuts import redirect
from pickle import NONE, load
import datetime
from .models import source
from urllib.parse import urlparse
import re
from django.conf.urls import handler404

def error_404_view(request, exception=None):
    
    return render(request,'page/error_404.html',status=404)

def handler500(request):
    print('handler500')
    return render(request, 'page/500.html', status=500)

def index(request):
    return render(request,'page/index.html')

def spot_fake_news(request):
    return render(request, 'page/about.html')
def ask_expert(request):
    return render(request, 'page/ask_expert.html')
def read_beyond(request):
    return render(request, 'page/read_beyond.html')
def solution(request):
    return render(request, 'page/solution.html')


def source_view(response):
    if response.method == 'POST':
        form = source_form(response.POST)
        is_reliable = None

        if form.is_valid():
            source_name = form.cleaned_data['source']
            # print(source_name)
            domain = urlparse(source_name).netloc
            if(domain):
                # print(domain)
                domain = domain.split('.')
                # print(domain)
                if(domain[0] == 'www'):
                    source_name = domain[1]
                else:
                    source_name = domain[0]
            else:
                domain = source_name.split('.')
                # print(domain)
                if(domain[0] == 'www'):
                    source_name = domain[1]
                else:
                    source_name = domain[0]
            # print(source_name)
            t = source.objects
            filter = source.objects.filter(url__icontains =source_name)
            filtered_source = filter.values_list()[0][1]
            if filter:
                # print('found')
                is_reliable = True
            else:
                is_reliable = False

        return render(response, 'page/source.html', {'form':form, "is_reliable":is_reliable,'filtered_source':filtered_source})
            # if source.objects.get(name='abc new'):
            #     print('exist')
            # else:
            #     print('not exist')
            
    else:
        form = source_form()
        return render(response, 'page/source.html', {'form':form})

def author(response):
    if response.method == 'POST':
        form = author_form(response.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            author_info = author.split(' ')
            if(len(author_info) == 2):
                url = 'https://au.linkedin.com/pub/dir?firstName='+author_info[0]+'&lastName='+author_info[1]+'&trk=people-guest_people-search-bar_search-submit'
            elif(len(author_info) == 1):
                url = 'https://www.linkedin.com/pub/dir?firstName='+author_info[0]+'&lastName=&trk=public_profile_people-search-bar_search-submit'
            return redirect(url)
    else:
        form = author_form()


    return render(response, 'page/author.html', {'form':form})

def author_check(author_name):
    author_info = author_name.split(' ')
    url = None
    if(len(author_info) == 2):
        url = 'https://au.linkedin.com/pub/dir?firstName='+author_info[0]+'&lastName='+author_info[1]+'&trk=people-guest_people-search-bar_search-submit'
    elif(len(author_info) == 1):
        url = 'https://www.linkedin.com/pub/dir?firstName='+author_info[0]+'&lastName=&trk=public_profile_people-search-bar_search-submit'
    return url

def is_url(url):
    
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    return re.match(regex, url) is not None

def check_source(source_name):
    if(not source_name):
        return (None, None)
    if(not is_url(source_name)):
        return (None, None)

    is_reliable = 'no'
    domain = urlparse(source_name).netloc
    
    if(domain):
        domain = domain.split('.')
      
        if(domain[0] == 'www'):
            source_name = domain[1]
        else:
            source_name = domain[0]
        
    else:
        domain = source_name.split('.')
    
        if(domain[0] == 'www'):
            source_name = domain[1]
        else:
            source_name = domain[0]
    
    t = source.objects
    filter = source.objects.filter(url__icontains =source_name)
    
    if filter:
        is_reliable = True
    else:
        is_reliable = False
    
    return (is_reliable, source_name)

def sentiment_analysis(text):
    # sentiment = load(open('/home/rahulagg/clarifact/clarifact/clarifact_app/sentiment_model.pkl', 'rb'))
    sentiment = load(open('sentiment_model.pkl', 'rb'))
    result = sentiment.polarity_scores(text)
    senti = None
    
    percentage = round(result['compound'] * 100, 1)
    if(percentage < 0 ):
        percentage = percentage * -1
    
    percentage = ''.join((str(percentage), '%'))
    print('result of sentiment analyzer = {}'.format(result))
    
    if(result['compound']>0.2):
        senti =  'positive'
        
    elif(result['compound'] <-0.2):
        senti = 'negative'
        
    else:
        senti = 'neutral'
        
    return (senti,percentage)

def fake_news(response):
    model = load(open('model.pkl', 'rb'))
    vec = load(open('transformation.pkl', 'rb'))
    
    if response.method == 'POST':
        newsform = fake_news_form(response.POST)
        
        if newsform.is_valid():
            # Reading the form content
            text = newsform.cleaned_data['news_text']
            title = newsform.cleaned_data['news_title']
            
            author = newsform.cleaned_data['news_author']
            source = newsform.cleaned_data['source']
           
            news_bias = newsform.cleaned_data['news_bias']


          

            #Pac algorithm
            vec_result = vec.transform([text])
            result = model.predict(vec_result)[0]
            result_prob = model._predict_proba_lr(vec_result)[0]
            fake_prob = round(result_prob[0]*100, 1)
            real_prob = round(result_prob[1]*100, 1)
            str_fake_prob = ''.join((str(round(result_prob[0]*100, 1)),'%' ))
            str_real_prob = ''.join((str(round(result_prob[1]*100, 1)), '%'))

            

            # Sentiment
            sentiment,percentage = sentiment_analysis(text)
           
            sentiment_text = None
            
            if(news_bias == 'Positive' and sentiment =='positive'):
                sentiment_text = 'You are reading similar news comparing to your perspective, go find some opposing news!'
                
            if(news_bias == 'Negative' and sentiment =='negative'):
                sentiment_text = 'You are reading similar news comparing to your perspective, go find some opposing news!'
                your_bias = 'Negative'
            if((news_bias == 'Positive' and sentiment =='negative') | (news_bias == 'Negative' and sentiment =='positive')):
                sentiment_text =  'You are reading opposing news comparing to your perspective, Great job!'
               
            if(sentiment=='neutral'):
                sentiment_text = 'You are reading opposing news comparing to your perspective, Great job!'
            
           
            author_url =  author_check(author)

            
            if(source):
                is_reliable, source_name = check_source(source)
            else:
                is_reliable = None
                source_name = None
           

            return render(response, 'page/result.html',{'text':text,
                                                         'ans':result,
                                                         'fake_prob':fake_prob,
                                                         'real_prob':real_prob,
                                                         'str_real_prob':str_real_prob,
                                                         'str_fake_prob':str_fake_prob,
                                                         'author':author,
                                                         'author_check':author_url,
                                                         'your_bias':news_bias,
                                                         'title':title,
                                                         'is_reliable':is_reliable,
                                                         'source':source,
                                                         'source_name':source_name,
                                                         'sentiment':sentiment,
                                                         'sentiment_text':sentiment_text,
                                                         'percentage':percentage})
    else:
        
        newsform = fake_news_form()

    

    return render(response, 'page/fake_news.html', {'form':newsform,})



