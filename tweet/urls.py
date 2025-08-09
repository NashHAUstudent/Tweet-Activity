from tweet import views
from django.urls import path

urlpatterns = [
    path('', views.tweet, name='tweet'),

    path('view_tweet', views.view_tweet, name='view_tweet')
]