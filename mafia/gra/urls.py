from django.urls import path
from . import views

urlpatterns = [
    path('gra/', views.gra_dodaj, name='Dodaj grę'),
    path('gra/dodaj_graczy/', views.gra_dodaj_graczy, name='Dodaj graczy')
]