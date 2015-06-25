from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from articles.models import Article


class ArticlesView(APIView):
    """
    A view that returns a templated HTML representation of a given user.
    """
    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        return Response({'articles': articles}, template_name='articles/index.html')


class UserCountView(APIView):
    """
    A view that returns the count of active users in JSON.
    """
    renderer_classes = (TemplateHTMLRenderer, )

    def get(self, request, format=None):
        user_count = User.objects.filter(active=True).count()
        content = {'user_count': user_count}
        return Response(content, template_name='articles/index.html')


def index(request):
    articles = Article.objects.all()

    return render(request, 'articles/index.html', context={'articles': articles})
