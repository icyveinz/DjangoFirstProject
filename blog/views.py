from django.shortcuts import render


def index(request):
    data = {
        "age" : 66,
        "languages" : ["python", "java"]
    }
    return render(request, "blog/index.html", context=data)
