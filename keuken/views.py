from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response

from models import Recipe

def index(request):
    return render_to_response('index.html', {
        # return only the 10 most recent recipies
        'recipes': Recipe.objects.all().order_by('-pub_date')[:10]
    })
	
def detail(request, id):
    return render_to_response('recipe-details.html', {
        'recipe': get_object_or_404(Recipe, pk=id)
    })

def list_by_author(request, author):
    return HttpResponse(get_object_or_404(User, username=author))

