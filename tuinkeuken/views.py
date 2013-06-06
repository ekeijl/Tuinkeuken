from django.shortcuts import HttpResponse

from keuken.models import Recipe

def index(request):
    return HttpResponse("I'm in your keuken, crafting Tuin.")
