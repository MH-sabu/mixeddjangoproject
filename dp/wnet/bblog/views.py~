from django.shortcuts import render

from bblog.models import Post , Comment

def index(request):
    latest_post_list = Post.objects.all()
    context = {'latest_post_list': latest_post_list}
    return render(request, 'bblog/index.html', context)

