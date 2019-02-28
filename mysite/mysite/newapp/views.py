from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


posts=[
    {
        'author':'new author',
        'Name':'Mike author',

        'Date':'27-210-29',

    },
    {
        'author':'new author',
        'Name':'Mike author',

        'Date':'27-210-29',

    },
    {
        'author':'new author',
        'Name':'Mike author',

        'Date':'27-210-29',

    }
]
def home(request):
    context={
        "posts": posts
    }
    return render(request,'newapp/home.html',context)

def about(request):
    return render(request,'newapp/about.html')

def contact(request):
    return render(request,'newapp/contact.html')