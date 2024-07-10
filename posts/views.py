from django.shortcuts import render
from .models import Post

# Create your views here.
def post_lists(request):
    posts = Post.objects.all().order_by('-date')
    print(posts)
    return render(request, 'posts/post_lists.html', { 'posts': posts })