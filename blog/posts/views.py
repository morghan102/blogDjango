from django.shortcuts import render
from .models import Post

# Create your views here.
def index(req):
    posts = Post.objects.all()
    return render(req, 'index.html', {'posts': posts})