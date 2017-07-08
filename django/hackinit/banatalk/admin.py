from django.contrib import admin

# Register your models here.
from .models import Food, Eat, User

admin.site.register(Food)
admin.site.register(Eat)
admin.site.register(User)
