from django.urls import path
from . import views

#/Users/macbookpro_meksem/Documents/Django-all-projects/www/mysite/myapps/templatetags 
urlpatterns = [
    path('home', views.index, name='home'),
    path('', views.tarifs, name='tarifs'), 
    # path('demandedevis', views.demandedevis, name='demandedevis'), 
   
    
]
