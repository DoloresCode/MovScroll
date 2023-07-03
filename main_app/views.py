from django.shortcuts import redirect
from django.views import View
from .models import Actor, Movie, Watchlist
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

    # Here we have added the playlists as context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["watchlists"] = Watchlist.objects.all()
        return context
    
class About(TemplateView):
    template_name = "about.html"

# class Actor:
#     def __init__(self, name, image, bio):
#         self.name = name
#         self.image = image
#         self.bio = bio

class MovieList(TemplateView):
    template_name = "movie_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["movies"] = Movie.objects.all()
        return context

# class Movie:
#     def __init__(self, image, title, release_year, actors, runtime, genre, synopsis):
#         self.image = image
#         self.title = title
#         self.release_year = release_year
#         self.actors = actors
#         self.runtime = runtime
#         self.genre = genre
#         self.synopsis = synopsis

movies = [
    Movie("https://m.media-amazon.com/images/I/91mgQQaBOCL._RI_.jpg", "Unbreakable", 2000, ["Bruce Willis", "Samuel L. Jackson"], 106, "Drama, Mystery, Sci-Fi", "A man learns something extraordinary about himself after a devastating accident."),
    Movie("https://s3.amazonaws.com/nightjarprod/content/uploads/sites/130/2022/01/19173426/dvEggyDTTIBDvrUNjTEa9depT0f-scaled.jpg", "Dirty Dancing", 1987, ["Patrick Swayze", "Jennifer Grey"], 100, "Drama, Music, Romance", "Spending the summer at a Catskills resort with her family, Frances \"Baby\" Houseman falls in love with the camp's dance instructor, Johnny Castle.")
]


class ActorList(TemplateView):
    template_name = "actor_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            context["actors"] = Actor.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["actors"] = Actor.objects.all()
            # default header for not searching 
            context["header"] = "Trending Actors"
        return context

class ActorCreate(CreateView):
    model = Actor
    fields = ['name', 'img', 'bio', 'verified_actor']
    template_name = "actor_create.html"
    success_url = "/actors/"

class ActorDetail(DetailView):
    model = Actor
    template_name = "actor_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["watchlists"] = Watchlist.objects.all()
        return context

class ActorUpdate(UpdateView):
    model = Actor
    fields = ['name', 'img', 'bio', 'verified_actor']
    template_name = "actor_update.html"
    success_url = "/actors/"

class ActorDelete(DeleteView):
    model = Actor
    template_name = "actor_delete_confirmation.html"
    success_url = "/actors/"

class MovieCreate(View):

    def post(self, request, pk):
        image = request.POST.get("img")
        title = request.POST.get("title")
        release_year = request.POST.get("release_year")
        runtime = request.POST.get("runtime")
        genre = request.POST.get("genre")
        synopsis = request.POST.get("synopsis")
        actor = Actor.objects.get(pk=pk)
        Movie.objects.create(image=image, title=title, release_year=release_year, runtime=runtime, genre=genre, synopsis=synopsis, actor=actor)
        return redirect('actor_detail', pk=pk)
    
class MovieCreateGeneral(CreateView):
    model = Movie
    fields = ['img', 'title', 'release_year', 'runtime', 'genre', 'synopsis', 'actors']
    template_name = 'movie_create_general.html'
    success_url = '/movies/'   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['actors'] = Actor.objects.all()
        return context
    
class WatchlistMovieAssoc(View):

    def get(self, request, pk, movie_pk):
        # get the query param from the url
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            # get the watchlist by the id and
            # remove from the join table the given song_id
            Watchlist.objects.get(pk=pk).movies.remove(movie_pk)
        if assoc == "add":
            # get the watchlist by the id and
            # add to the join table the given song_id
            Watchlist.objects.get(pk=pk).movies.add(movie_pk)
        return redirect('watchlist_list')
    

class WatchlistList(ListView):
    model = Watchlist
    template_name = "watchlist_list.html"

class WatchlistDetail(DetailView):
    model = Watchlist
    template_name = "watchlist_detail.html"

