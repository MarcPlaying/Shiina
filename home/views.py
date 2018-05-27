from django.shortcuts import render
from django.http import HttpResponse
import MySQLdb

def index(request):
        return render(request, 'home/home.html')

def new(request):
        return render(request, 'home/new.html')

def beatmaps(request):



        return render(request, 'home/beatmaps.html')

def search(request):
        query = request.GET.get('q')
        context= {
            'query': query,
        }
        return render(request, 'home/search.html', context)
