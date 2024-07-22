from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    LatestArticlesFeed,
)

app_name = 'BlogApp'


urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('articles/latest/feed/', LatestArticlesFeed(), name='articles-feed'),
]
