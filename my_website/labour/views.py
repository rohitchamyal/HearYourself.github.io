from django.shortcuts import render

# Create your views here.


def starting_page(request):
    return render(request , "labour/index.html")


def posts(request):
     return render(request,"labour/all-posts.html")


def post_detail(request):
    pass
