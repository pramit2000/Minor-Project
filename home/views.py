from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')

def contacts(request):
    return render(request, 'contacts.html')