from django.shortcuts import render, HttpResponse

# Create your views here.

def movie_list(request):
    return HttpResponse("Movie List")

def movie_detail(request, pk):
    return HttpResponse(f"Movie Detail for movie with id {pk}")