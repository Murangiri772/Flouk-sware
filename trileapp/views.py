from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def starter(request):
    return render(request,'starter-page.html')
def service(request):
    return render(request, 'service-details.html')
def portfolio(request):
    return render(request, 'portfolio-details.html')
def portfolio(request):
    return render(request, 'portfolio.html')
def services(request):
    return render(request, 'services.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')

