
from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')


def Count(request):
    a = request.GET['fulltext']
    wordcount = a.split()
    return render(request, 'count.html', {'fulltext': a, 'count': len(wordcount)})


def About(request):
    return render(request, 'About.html')
