from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from .models import *
from .forms import *
# Widok Nowa gra (1)
def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def gra_dodaj(request):
  form = GraTworzForm()
  if request.method == "POST":
    form = GraTworzForm(request.POST)
    if form.is_valid():
      form.save(commit= True)
      return redirect('/gra/dodaj_graczy/')

  context = {
    'form': form
  }
  return render(request, 'home.html', context)

def gra_dodaj_graczy(request):
  form = GraTworzGraczyForm()
  if request.method == "POST":
    form = GraTworzGraczyForm(request.POST)
    if form.is_valid():
      print(form.cleaned_data)
    else:
      print(form.errors)
 
  context = {
    'form': form
  }
  return render(request, 'gra/dodaj_graczy.html', context)