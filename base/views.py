from django.shortcuts import render

# Create your views here.
def index(r):
    return render(r,'base.html')

def flipkart(r):
    return render(r,'index.html')

def signup(r):
    return render(r,'registration/signup.html')


#This change was brought by developer B
#welcome to the django project by sanket more
