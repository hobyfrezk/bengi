from django.shortcuts import render
from .models import News


def index(request):
    return render(request, "bengi_news/index.html")


def fetch_news(request):
    # get query from url
    query = request.GET.get("query", "")

    news_list = News.objects.filter(title__icontains=query)

    context = {"news_list": news_list}
    # render news as cards
    return render(
        request,
        "bengi_news/htmx/news.html",
        context,
    )
