from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('spot_fake_news/', views.spot_fake_news, name='spot_fake_news'),
    path('ask_expert/', views.ask_expert, name='ask_expert'),
    path('read_beyond/', views.read_beyond, name='read_beyond'),
    path('solution/', views.solution, name='solution'),
    path('author/', views.author, name='author'),
    path('fake_news_detector/', views.fake_news, name='fake_news'),
    path('source/', views.source_view, name = 'source')
]
