from django.shortcuts import render_to_response

from keuken.models import Recipe

def index(request):
    return render_to_response('index.html', {
        # return only the 10 most recent recipies
        'recipes': Recipe.objects.all().order_by('-pub_date')[:10]
    })
