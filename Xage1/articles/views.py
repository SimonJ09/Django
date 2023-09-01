from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

# Lire (Read) - Afficher la liste des articles
def list_articles(request):
    articles = Article.objects.all()
    return render(request, 'articles/article.html', {'articles': articles})

# Créer (Create) - Ajouter un nouvel article
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_articles')
    else:
        form = ArticleForm()
    return render(request, 'articles/create_article.html', {'form': form})

# Mettre à jour (Update) - Modifier un article existant
def update_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('list_articles')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'articles/update_article.html', {'form': form, 'article': article})

# Supprimer (Delete) - Supprimer un article existant
def delete_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('list_articles')
    return render(request, 'articles/delete_article.html', {'article': article})
