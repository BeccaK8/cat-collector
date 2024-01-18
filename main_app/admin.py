from django.contrib import admin

# Import cat model
from .models import Cat, Feeding, Photo, Toy

# Register your models here.
admin.site.register(Cat)
admin.site.register(Feeding)
admin.site.register(Photo)
admin.site.register(Toy)
