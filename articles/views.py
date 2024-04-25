from django.shortcuts import render,redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from django.http import Http404
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
def article_detail_view(request, slug=None):
    article_obj = None
    if slug is not None:
        try:
            article_obj = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            article_obj = Article.objects.filter(slug=slug).first() 
        except:
            raise Http404

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
            return redirect('article-detail', slug=article_obj.slug)
    return render(request, "articles/create.html", context=context)