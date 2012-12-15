from django.db import models
from django.contrib.auth.models import User

class Recipe(models.model):
    author = models.ForeignKey(User)
    # a free form text field containing the ingredient list
    ingredients = models.TextField(blank = False)
    # a free form text field containing the cooking directions
    directions = models.TextField(blank = False)
