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
            print(source_name)
            domain = urlparse(source_name).netloc
            if(domain):
                print(domain)
                domain = domain.split('.')
                print(domain)
                if(domain[0] == 'www'):
                    source_name = domain[1]
                else:
                    source_name = domain[0]
            else:
                domain = source_name.split('.')
                print(domain)
                if(domain[0] == 'www'):
                    source_name = domain[1]
                else:
                    source_name = domain[0]
            print(source_name)
            t = source.objects
            filter = source.objects.filter(url__icontains =source_name)
            filtered_source = filter.values_list()[0][1]
            if filter:
                print('found')
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

def fake_news(response):
    model = load(open('model.pkl', 'rb'))
    vec = load(open('transformation.pkl', 'rb'))
    
    if response.method == 'POST':
        newsform = fake_news_form(response.POST)
        
        if newsform.is_valid():
            
            text = newsform.cleaned_data['news_text']
            title = newsform.cleaned_data['news_title']
            date = newsform.cleaned_data['news_date']
            author = newsform.cleaned_data['news_author']
            print(type(date))
            if(date == datetime.date(1900, 1, 1)):
                date = None
            print(date)
            vec_result = vec.transform([text])
            result = model.predict(vec_result)[0]
            
            return render(response, 'page/result.html',{'text':text,
                                                         'ans':result,
                                                         'autho':author,
                                                         'date':date,
                                                         'title':title})
    else:
        
        newsform = fake_news_form()

    

    return render(response, 'page/fake_news.html', {'form':newsform,})



