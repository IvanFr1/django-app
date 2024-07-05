from django.urls import path
from .views import ArticleListView


app_name = 'BlogApp'


urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article_list'),
]
