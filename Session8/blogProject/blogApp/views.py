from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def new(request):
    if request.method == 'POST':
        
        print(request.POST)
        
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
        )
        return redirect('list')
    
    return render(request, 'new.html')


def list(request):
    articles = Article.objects.all()
    startups = Article.objects.filter(category='startup')
    startups_len = len(startups)

    hobbies = Article.objects.filter(category='hobby')
    hobbies_len = len(hobbies)

    programmings = Article.objects.filter(category='programming')
    programmings_len = len(programmings)

    return render(request, 'list.html', {'startups_len': startups_len, 'hobbies_len': hobbies_len, 'programmings_len': programmings_len})
    
def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'detail.html', {'article':article})

def category(request, category):
    articles = Article.objects.filter(category=category)
    return render(request, 'category.html', {'articles': articles, 'category': category})