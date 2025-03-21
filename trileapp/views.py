from django.shortcuts import render, redirect


from trileapp.models import *


# Create your views here.
def index(request):
    return render(request, 'index.html')
def starter(request):
    return render(request,'starter-page.html')

def portfolio(request):
    return render(request, 'portfolio.html')
def services(request):
    return render(request, 'services.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def contact(request):
    if request.method == "POST":
        mycontact= Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )


        mycontact.save()
        return redirect('/contact')
    else:
        return render(request, 'contact.html')

