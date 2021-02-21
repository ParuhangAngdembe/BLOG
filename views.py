from django.shortcuts import render
from .models import *

# Create your views here.
#function based view vs class based view

def index(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

def services(request):
    return render(request, 'blog/services.html')

def portfolio(request):
    return render(request,'blog/portfolio.html')

def price(request):
    return render(request,'blog/price.html')

def contact(request):
    if request.method == "POST":
        # yo request vaneko chai Form ma vako input tag ko name
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        data =Contact.objects.create(
# models' field name = vairable
            name = name,
            email = email,
            subject = subject,
            message = message
        )
        data.save()

    return render(request,'blog/contact.html')

def blogHome(request):
     return render(request,'blog/blog-home.html')

def blogSingle(request):
    return render(request, 'blog/blog-single.html')

def elements(request):
    return render(request, "blog/elements.html")