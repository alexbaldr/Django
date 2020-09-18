from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Sections, Relationship


def articles_list(request):
    template = 'articles/news.html'
    get_articles = Article.objects.prefetch_related('relationship_set')
    ordering = '-published_at'
    context = {
            'object_list': get_articles,
            }

    return render(request, template, context)
