from django.http import HttpResponse
from django.template import loader
from .models import Movies

# Create your views here.
def index(request):
    movies = Movies.objects.order_by('type')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'movies': movies}, request))

def movies(request, movies_id):
    movie = Movies.objects.get(pk = movies_id)
    template = loader.get_template('display_movies.html')
    context = {
        'movie': movie
    }
    return HttpResponse(template.render(context, request))