from django.shortcuts import render, redirect

# import class-based-views (CBVs)
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Cat, Toy
from .forms import FeedingForm

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

    # here we'll get a value list of the toy ids associated with the cat
    id_list = cat.toys.all().values_list('id')
    # this is for all toys a cat does not have
    toys_cat_doesnt_have = Toy.objects.exclude(id__in=id_list)

    # instantiate the FeedingForm to be rendered in our template
    feeding_form = FeedingForm()

    return render(request, 'cats/detail.html', { 
        'cat': cat, 
        'feeding_form': feeding_form,
        'toys': toys_cat_doesnt_have
    })



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

# FEEDING AND RELATIONSHIP VIEW FUNCTIONS
# This is to add a feeding to a cat
def add_feeding(request, cat_id):
    # Create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # it's also important to validate forms
    # Django gives us a bit in function for that
    if form.is_valid():
        # don't want to save the feeding to the db 
        # until we have a cat_id
        new_feeding = form.save(commit=False)
        # add the cat_id
        new_feeding.cat_id = cat_id
        new_feeding.save()

    # finally, redirect to cat detail page
    return redirect('detail', cat_id=cat_id)

# TOY views
# Toy List
class ToyList(ListView):
    model = Toy
    template_name = 'toys/index.html'

# Toy Detail
class ToyDetail(DetailView):
    model = Toy
    template_name = 'toys/detail.html'

# Toy Create
class ToyCreate(CreateView):
    model = Toy
    fields = [ 'name', 'color' ]

    def form_valid(self, form):
        return super().form_valid(form)

# Toy Update
class ToyUpdate(UpdateView):
    model = Toy
    fields = [ 'name', 'color' ]
    
# Toy Delete
class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys'

# Add/Associate Toy to Cat
def assoc_toy(request, cat_id, toy_id):
    # we target the cat and pass it the toy id
    Cat.objects.get(id=cat_id).toys.add(toy_id)

    return redirect('detail', cat_id=cat_id)

# Unassociate/Remove Toy from Cat
def unassoc_toy(request, cat_id, toy_id):
    # we target the cat and pass it the toy id
    Cat.objects.get(id=cat_id).toys.remove(toy_id)

    return redirect('detail', cat_id=cat_id)
