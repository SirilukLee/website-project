"""telecorpWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from Website import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('aboutus/', views.aboutus),
    path('productsnservices/', views.products),
    path('articles/', views.articles),
    path('article_ds/', views.article_ds),
    path('article_digitalTrans/', views.article_dTrans),
    path('article_digitalHealth/', views.article_dHealth),
    path('article_iot/', views.article_iot),
    path('contactus/', views.contactus),
    path('pdpa_policy/', views.pdpa_policy),
    path('cookie_policy/', views.cookie_policy),
    path('ourcustomers/', views.ourscustomers),
    path('ourcustomers_company/', views.ourcustomers_company),
    path('ourcustomers_stateSector/', views.ourcustomers_stateSector),
    path('career/', views.career), 
    path('career_programmer/', views.career_programmer),
    path('career_programmer2/', views.career_programmer2),
    path('career_accountant/', views.career_programmer),
    path('career_marketing/', views.career_marketing),
    path('h_series/', views.h_series),
    path('queue/', views.queue),  
     
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
