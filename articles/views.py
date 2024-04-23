from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
def article_search_view(request):

    query_dict = request.GET
    q = None
    try:
        q = int(query_dict.get("q"))
    except:
        q = None
    article_obj = None
    if q is not None:
        article_obj = Article.objects.get(id=q)
    context = {
        "object": article_obj
    }
    return render(request, "articles/search.html", context=context)

# Create your views here.
def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj,
    }
    return render(request, "articles/detail.html", context=context)

# Create your views here.
@login_required        
def article_create_view(request, ):
    form = ArticleForm(request.POST or None)
    context = {
        "form": form,
        "created": False
    }
    if request.method == "POST":
        if form.is_valid():
            article_obj = form.save()
            context["form"] = ArticleForm()
    return render(request, "articles/create.html", context=context)