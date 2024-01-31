from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus_history.html')

def products(request):
    return render(request, 'productsnservices.html')

def articles(request):
    return render(request, 'articles.html')

def article_ds(request):
    return render(request, 'article-DS.html')

def article_dTrans(request):
    return render(request, 'article-digitalTrans.html')

def article_dHealth(request):
    return render(request, 'article-digitalHealth.html')

def article_iot(request):
    return render(request, 'article-IOT.html')

def contactus(request):
    return render(request, 'contactus.html')

def pdpa_policy(request):
    return render(request, 'pdpa-policy.html')

def cookie_policy(request):
    return render(request, 'cookie-policy.html')

def ourscustomers(request):
    return render(request, 'ourcustomers.html')

def ourcustomers_company(request):
     return render(request, 'ourcustomers-company.html')

def ourcustomers_stateSector(request):
     return render(request, 'ourcustomers-stateSector.html')

def ourcustomers_stateSector(request):
     return render(request, 'ourcustomers-stateSector.html')

def career(request):
     return render(request, 'career.html')
    
def career_programmer(request):
     return render(request, 'career_programmer.html')

def career_programmer2(request):
     return render(request, 'career_programmer2.html')

def career_accountant(request):
     return render(request, 'career_accountant.html')

def career_marketing(request):
    return render(request, 'career_marketing.html')

def h_series(request):
    return render(request, 'H-Series.html')

def queue(request):
    return render(request, 'queue.html')


