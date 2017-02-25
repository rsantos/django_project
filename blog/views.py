from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Category, Post

def home(request):
    name = "Rafael"
    #categories = ['PHP', 'Java', 'Ruby']

    #for category in categories:
    #    Category.objects.create(name=category)

    all_categories = Category.objects.all()

    category_python = Category.objects.get(name='PHP')

    '''
    post = Post()
    post.name = 'My first post'
    post.content = 'Content of my first post'
    post.status = 'Published'
    post.category = category_python
    post.save()
    '''

    post = Post.objects.get(pk=1)

    context = {
        'name': name,
        'categories': all_categories,
        'post': post,
    }

    return render(request, 'blog/home.html', context)
