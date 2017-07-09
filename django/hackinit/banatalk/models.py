from django.db import models
import datetime
# the food objects
class Food(models.Model):

    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)
	# name = models.CharField(max_length=50)
    energy = models.FloatField() #in kj/100g
    protein = models.FloatField() #in g/100g
    fat = models.FloatField() #in g/100g
    carbohydrate = models.FloatField() #in g/100g

# each scanning
class Eat(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    weight = models.FloatField() # g
    time = models.CharField(max_length=50) # 1 - 24

# the user data for 1 day
class User(models.Model):
	Datetime = models.CharField(max_length=50) # 1 - 24
	energy = models.FloatField() #in /mg
	protein = models.FloatField() #in /mg
	fat = models.FloatField() #in /mg
	carbohydrate = models.FloatField()
