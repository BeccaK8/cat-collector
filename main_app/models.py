from django.db import models
from django.urls import reverse

# A tuple of 2-tuples
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
    # this is the get_absolute_url method
    # it redirects to the detail page where appropriate
    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})
    
# This is a model for feedings - this is a 1:M relationship with Cats
    # One Cat can have many Feedings
    # A Feeding belongs to one Cat
class Feeding(models.Model):
    # we can add a customer label to show up on our forms
    date = models.DateField('feeding date')

    # B-reakfast
    # L-unch
    # D-inner
    meal = models.CharField(
        max_length=1,
        # add the custom 'choices' field option
        choices=MEALS,
        # set default choice to 'B'
        default=MEALS[0][0]
    )
    # Create a cat_id FK
    # Creates the 1:M relationship - Cat -< Feedings
    # models.ForeignKey needs two args: model and what to do if the parent model is deleted
    # in the database, the column in the feedings table for the FK will be called "cat_id"
    # because Django, by default, appends _id to the name of the model
    # DO NOT CONFUSE THIS WITH MONGODB and THEIR `._id` - NOT THE SAME
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_meal_display()} on {self.date} for {self.cat}"