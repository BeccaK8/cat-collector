from django.shortcuts import render
# import class-based-views (CBVs)
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

# Create View
# inherit from CBV - CreateView - to make our cats create view
class CatCreate(CreateView):
    model = Cat
    
    # this view creates a form so we need to identify which fields to use:
    # fields attribute is required and can be used to 
    # limit or change the ordering of the attributes from the Cat model
    # that are generatd in the  ModelForm passed to the template
    fields = '__all__'

    # we can add other options inside this view
    # we don't need success_url since we added get_absolute_url to Cat Model
    # success_url = '/cats/{cat_id}'

# Update View - extends UpdateView class
class CatUpdate(UpdateView):
    model = Cat
    # let's make it so you can't rename a cat
    # so we need to customize fields
    fields = [ 'breed', 'description', 'age' ]

# Delete View - extends DeleteView class
class CatDelete(DeleteView):
    model = Cat

    success_url = '/cats'