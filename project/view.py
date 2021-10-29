# from django.http import HttpResponse
from django.shortcuts import render

def showhome(request):
    return render(request, 'Home.html')

def about(request):
    return  render(request, 'aboutus.html')

def search(request):
    return  render(request, 'search.html')

def client(request):
    return  render(request, 'client.html')