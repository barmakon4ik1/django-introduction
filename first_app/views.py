from django.http import HttpResponse


def first_view(request):
    return HttpResponse("<h1>Hello! It's my first view!</h1")


def second_view(request):
    return HttpResponse("<h1>Hello! It's my second view!</h1")
