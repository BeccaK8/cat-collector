from django.shortcuts import render
from .models import Cat

# cats = [
#     {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
#     {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
#     {'name': 'Chunky Monkey', 'breed': 'long hair', 'description': 'sweet and cuddly', 'age': 0},
# ]

# Define the home view - '/'
# GET - Home
def home(request):
    # Include a .html file extension, unlike EJS
    return render(request, 'home.html')

# Define the about view - about/
def about(request):
    return render(request, 'about.html')

# Index View - shows all cats at '/cats'
def cats_index(request):
    # collect our objects from the database
    # this uses the object's object on the at model class
    # the objects object has a method called all
    # all grabs all of the entities using the parent model
    cats = Cat.objects.all()
    # print(cats)
    # for cat in cats:
    #     print(cat)
    # just like in EJS we can pass data to views
    return render(request, 'cats/index.html', { 'cats': cats })

# Detail View - shows one cat at '/cats/:id'
def cats_detail(request, cat_id):
    # find one cat with its id
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', { 'cat': cat })