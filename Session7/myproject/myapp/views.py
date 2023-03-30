from django.shortcuts import render

def hello(request):
    CountApp/templates/count.html
    return render(request, 'hello.html')
