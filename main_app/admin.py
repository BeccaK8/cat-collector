from django.contrib import admin

# Import cat model
from .models import Cat

# Register your models here.
admin.site.register(Cat)