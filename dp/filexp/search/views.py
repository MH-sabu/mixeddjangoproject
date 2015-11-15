from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from search.models import Page,Expression 
def index(request):
    sr=Page.objects.get(pk=10)
    return render(request,'search/index.html', {'sr':sr})
def misearch(request):
    if request.method == 'POST':
        search = request.POST['search']
    sr=Page.objects.filter(expression__exp_text__icontains=search)
    
    return render(request,'search/misearch.html', {'sr':sr})

def exd(request , pk):
    detail=Expression.objects.get(id=pk)
    detail.rating +=1
    detail.save()
    return HttpResponseRedirect('/search/')

