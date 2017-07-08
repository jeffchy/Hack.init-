class Food(models.Model):
	name = models.CharField(max_length=50)
	energy = models.FloatField() #in mg/100g
	protein = models.FloatField() #in mg/100g
	fat = models.FloatField() #in mg/100g
	carbohydrate = models.FloatField() #in mg/100g


class Eat(models.Model):
	name = models.CharField(max_length=50)
	weight = models.FloatField()
	time = models.DateTimeField()


class User(models.Model):
	Datetime = models.DateTimeField()
	energy = models.FloatField() #in /mg
	protein = models.FloatField() #in /mg
	fat = models.FloatField() #in /mg
	carbohydrate = models.FloatField()