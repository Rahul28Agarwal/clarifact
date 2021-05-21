from django.shortcuts import render


from django.http import HttpResponse


def index(request):
    return render(request,'page/index.html')

def spot_fake_news(request):
    return render(request, 'page/index.html')
def ask_expert(request):
    return render(request, 'page/ask_expert.html')
def read_beyond(request):
    return render(request, 'page/read_beyond.html')
