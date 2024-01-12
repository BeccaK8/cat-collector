from django.shortcuts import render

# Create your views here.

# Define the home view - '/'
# GET - Home
def home(request):
    # Include a .html file extension, unlike EJS
    return render(request, 'home.html')
