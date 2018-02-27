# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseForbidden
from app.models import Article

# Create your views here.


def index(request):
    articles = Article.objects.all()
    if not request.user.is_authenticated():
        articles = articles.exclude(internal=True)
    articles = articles.order_by('-created')[:20]
    return render(request, "bs4_index.html", locals())


def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Exception as E:
        return HttpResponseNotFound()
    if article.internal and not request.user.is_authenticated():
        return HttpResponseForbidden()
    return render(request, "bs4_article.html", locals())
