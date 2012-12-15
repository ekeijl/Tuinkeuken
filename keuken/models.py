from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    author = models.ForeignKey(User)
    pub_date = models.DateField(auto_now_add = True)
    # a free form text field containing the ingredient list
    ingredients = models.TextField(blank = False)
    # a free form text field containing the cooking directions
    directions = models.TextField(blank = False)
