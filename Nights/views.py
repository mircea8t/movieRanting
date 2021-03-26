from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Movie

from itertools import chain

def home(request):
    return render(request, 'Nights/home.html')

class MovieListView(ListView):
    model = Movie
    template_name = 'Nights/home.html'
    context_object_name = 'movies'
    ordering = ['title']
    paginate_by = 3

class MovieDetailView(DetailView):
    model = Movie

class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ['title', 'image', 'description', 'genre', 'director', 'writer', 'actors']

    def test_func(self):
        movie = self.get_object()
        if self.request.user.is_staff:
            return True
        else:
            return False

class MovieUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Movie
    fields = ['title', 'image', 'description', 'genre', 'director', 'writer', 'actors']

    def test_func(self):
        movie = self.get_object()
        if self.request.user.is_staff:
            return True
        else:
            return False

class MovieDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Movie
    success_url = '/'
    def test_func(self):
        movie = self.get_object()
        if self.request.user.is_staff:
            return True
        else:
            return False

def searchMovie(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        movie = Movie.objects.all().filter(title=search)
        genre = Movie.objects.all().filter(genre=search)
        movie_list = list(chain(movie, genre))
        return render(request, 'Nights/home.html', {'movies': movie_list})

def about(request):
    return render(request, 'Nights/about.html', {'title': 'About'})
