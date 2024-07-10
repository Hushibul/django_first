from django.shortcuts import render
# from django.http import HttpResponse

def homepage(request):
   # return HttpResponse('Hello World!')
   return render(request, 'home.html')

def aboutpage(request):
    # return HttpResponse('This is the about page')
    return render(request, 'about.html')