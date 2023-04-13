from django.shortcuts import render, redirect
from .models import Article, Comment, Reply

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
    comments = Comment.objects.filter(article=article).order_by('-created_date')
    replies = Reply.objects.filter(comment__article=article)
    if request.method == 'POST':
        
        author = request.POST.get('author', '').strip()
        body = request.POST.get('body', '').strip()
        if author and body:
            comment = Comment(author=author, body=body, article=article)
            comment.save()
            return redirect('detail', article_id=article_id)
        
        # Handle reply form submission
    elif request.POST.get('comment_id'):
        parent_comment = Comment.objects.get(id=request.POST.get('comment_id'))
        author = request.POST.get('reply_author', '').strip()
        body = request.POST.get('reply_body', '').strip()
        if author and body:
                reply = Comment(author=author, body=body, article=article, parent=parent_comment)
                reply.save()
                return redirect('detail', article_id=article_id)
            
    return render(request, 'detail.html', {'article': article, 'comments': comments})


def category(request, category):
    articles = Article.objects.filter(category=category)
    return render(request, 'category.html', {'articles': articles, 'category': category})