from django.shortcuts import render


def index(request):
    return render(request, "blog/index.html", context={"site" : "google.com"})

def about(request):
    return render(request, "blog/about.html", context={"site" : "yandex.ru"})
