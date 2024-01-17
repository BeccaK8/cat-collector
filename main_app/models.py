from django.db import models
from django.urls import reverse
from datetime import date

# A tuple of 2-tuples
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
# The Toy model for our M:M relationship
class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.color} {self.name}'

    def get_absolute_url(self):
        return reverse('toy_detail', kwargs={'pk': self.id})


class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    # Add the M:M relationship for cats and toys
    # Cats >--< Toys
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return self.name
    
    # this is the get_absolute_url method
    # it redirects to the detail page where appropriate
    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})
    
    # this is how we can view related data from the main parent model
    def fed_for_today(self):
        # we can use django's filter, which produces a queryset for all feedings
        # we'll look at the array(QuerySet) and compare it to the length of the MEALS tuple
        # we can return a boolean that will be useful in our detail template
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)


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
    
    # change the default sort
    class Meta:
        ordering = [ '-date' ]
