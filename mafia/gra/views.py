from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from .models import *
from .forms import *
from .constant import *

@cache_page(60 * 15)
@csrf_protect
# Widok Nowa gra (1)
def home(request):
  template = loader.POST_template('home.html')
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
   #minumu 6 maksimum 16
 # print(request.POST['users'])
 # 
  if request.method == 'GET' and 'users' in request.GET:
    gracze=request.GET['users']
    print("Co za typ")
  else:
    gracze={}
    for i in range(0,min_graczy):
      gracze[i]=''
  
  context = {
    'gracze': gracze
  }
  return render(request, 'gra/dodaj_graczy.html', context)