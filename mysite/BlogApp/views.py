from django.db.models.base import Model
from django.utils.safestring import SafeText
from django.views.generic import ListView, DetailView
from django.contrib.syndication.views import Feed
from django.urls import reverse, reverse_lazy
from .models import Article

# Create your views here.


class ArticleListView(ListView):

    template_name = 'article_list.html'
    context_object_name = 'articles'
    queryset = (
        Article.objects
        .select_related('author', 'category')
        .prefetch_related('tags')
        .defer('content')
    )


class ArticleDetailView(DetailView):
    model = Article


class LatestArticlesFeed(Feed):
    title = 'Blog articles (latest)'
    description = 'Update on changes and addition blog articles'
    link = reverse_lazy('BlogApp:article_list')

    def items(self):
        return (
            Article.objects
            .filter(pub_date__isnull=False)
            .order_by('-pub_date')[:5]
        )
    
    def item_title(self, item: Article):
        return item.title
    
    def item_description(self, item: Article):
        return item.content[:200]
    