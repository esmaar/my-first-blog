from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts_before = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts_after = Post.objects.filter(published_date__gt=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts_before': posts_before, 'posts_after': posts_after})
