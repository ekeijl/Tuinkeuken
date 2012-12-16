from django.shortcuts import render_to_response

from keuken.models import Recipe

def index(request):
    return render_to_response('index.html', {
        'recipes': Recipe.objects.all().order_by('-pub_date')
    })
