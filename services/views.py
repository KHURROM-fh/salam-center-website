from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def marriage(request):
    return render(request, 'marriage.html')

def funeral_burial(request):
    return render(request, 'funeral-burial.html')

def convert_group(request):
    return render(request, 'Convert Group.html')

def interfaith(request):
    return render(request, 'Interfaith.html')

def financial_assistance(request):
    return render(request, 'Financial Assistance.html')

def community_relief(request):
    return render(request, 'Community Relief.html')

def zakat(request):
    return render(request, 'Zakat.html')