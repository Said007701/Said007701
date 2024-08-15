from django.shortcuts import render

def hello_view(request):
    return render (request,'index.html')

def index(request):
    menu_items = [
        {"name": "Home", "url": "index", "active": True},
        {"name": "About", "url": "about", "active": False},
        {"name": "Classes", "url": "classes", "active": False},
        {"name": "Blog", "url": "blog", "active": False},
    ]
    return render(request, 'index.html', {'menu_items': menu_items})