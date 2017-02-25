from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Category, Post

def home(request):
    name = "Rafael"
    #categories = ['PHP', 'Java', 'Ruby']

    #for category in categories:
    #    Category.objects.create(name=category)

    all_categories = Category.objects.all()

    category_post = Category.objects.get(name='Ruby')
    posts = Post.objects.filter(status='Published')

    '''
    post = Post()
    post.name = 'Show post 2'
    post.content = 'Content'
    post.status = 'Published'
    post.category = category_post
    post.save()
    '''

    #post = Post.objects.get(pk=1)

    context = {
        'name': name,
        'categories': all_categories,
        'posts': posts,
    }

    return render(request, 'blog/home.html', context)
