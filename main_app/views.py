from django.shortcuts import render
from .models import Artist
# This will import the class we are extending 
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView

# Create your views here.
# I created a class named Home that's a child of TemplateView and is inheriting what's built into the parent class
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class SongList(TemplateView):
    template_name = "song_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["songs"] = songs
        return context

class Song:
    def __init__(self, title, album):
        self.title = title
        self.album = album

songs = [
    Song("Lost", "stressed & depressed by The Circle Sessions"),
    Song("Never Ending Song", "Never Ending Song")
]

class ArtistCreate(CreateView):
    model = Artist
    fields = ['name', 'img', 'bio', 'verified_artist']
    template_name = "artist_create.html"
    success_url = '/artists/'

class ArtistList(TemplateView):
    template_name = "artist_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # This is essentially a query built into Django that's saying SELECT * FROM main_app_artist
        # self.request.GET is a dictionary just like in express we have req.query
        # print(self.request.GET)
        name = self.request.GET.get('name')
        if name != None:
            # This is essentially a regex matcher that's built in for us. It's searching for anything where the name of the artist contains (at any point) this name if there is a query
            context["artists"] = Artist.objects.filter(name__icontains=name)
        else:
            context["artists"] = Artist.objects.all()
        return context