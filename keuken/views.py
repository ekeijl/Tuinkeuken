from django.shortcuts import get_object_or_404, render_to_response

from .models import Recipe

def details(request, id):
    return render_to_response('recipe-details.html', {
        'recipe': get_object_or_404(Recipe, pk = id)
    })
