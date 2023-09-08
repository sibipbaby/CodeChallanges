from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm


# Create your views here.
def index(request):
    movie = Movie.objects.all()

    return render(request, 'index.html', {'movie_list': movie})


def detail(request, movie_id):
    cini = Movie.objects.get(id=movie_id)
    return render(request, 'detail.html', {'cini': cini})


def add_movie(request):
    if request.method == "POST":
        name = request.POST.get('name1', '')
        desc = request.POST.get('name2', '')
        year = request.POST.get('name3', '')
        img = request.FILES['img']
        movie = Movie(name=name, desc=desc, year=year, img=img)
        movie.save()
    return render(request, "add.html")


def update(request, id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, "edit.html", {'form': form}, {'movie': movie})


def delete(request, id):
    if request.method == "POST":
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')
