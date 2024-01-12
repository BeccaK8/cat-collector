from django.shortcuts import render

cats = [
    {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
    {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
    {'name': 'Chunky Monkey', 'breed': 'long hair', 'description': 'sweet and cuddly', 'age': 0},
]

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
    # just like in EJS we can pass data to views
    return render(request, 'cats/index.html', { 'cats': cats })