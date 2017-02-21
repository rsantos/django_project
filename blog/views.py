from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    name = "Rafael"
    languages = ['Python', 'PHP', 'Java', 'Ruby']

    context = {
        'name': name,
        'languages': languages
    }

    return render(request, 'blog/home.html', context)
