from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    name 		= models.CharField(max_length = 256, blank = False)
    author 		= models.ForeignKey(User)
    pub_date 	= models.DateField(auto_now_add = True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
	name = models.CharField(max_length=256, blank = False)
	
	def __str__(self):
		return self.name
		
class RecipeIngredient(models.Model):
	recipe 		= models.ForeignKey(Recipe)
	ingredient 	= models.ForeignKey(Ingredient)
	quantity 	= models.IntegerField()
	unit		= models.CharField(max_length=32, blank = True)
	
	def __str__(self):
		return str(self.quantity) + ' ' + self.unit + ' ' + self.ingredient.name
	
class Direction(models.Model):
	recipe = models.ForeignKey(Recipe)
	step = models.IntegerField()
	description = models.TextField(blank = False)
	
	def __str__(self):
		return self.description