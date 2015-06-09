from django.shortcuts import render

# Create your views here.
from articles.models import Article


def index(request):
    articles = Article.objects.all()

    return render(request, 'articles/index.html', context={'articles': articles})
