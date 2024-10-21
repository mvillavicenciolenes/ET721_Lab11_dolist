from django.shortcuts import render

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "dolist/index.html", context)
