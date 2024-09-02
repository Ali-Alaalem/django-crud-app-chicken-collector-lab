
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Chicken
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import EggsForm




def home(request):
 return render(request, 'home.html' )

def chicken_index(request):
        chickens = Chicken.objects.all() 
        return render(request, 'chickens/index.html', {'chickens': chickens})


def chicken_detail(request, chicken_id):
    chicken = Chicken.objects.get(id=chicken_id)
    eggs_form = EggsForm()
    return render(request, 'chickens/detail.html', {'chicken': chicken , 'eggs_form': eggs_form})



class ChickenCreate(CreateView):
    model = Chicken
    fields = ['name', 'breed', 'description', 'age']
    success_url = '/chickens/'
    

class ChickenUpdate(UpdateView):
    model = Chicken
  
    fields = ['breed', 'description', 'age']

class ChickenDelete(DeleteView):
    model = Chicken
    success_url = '/chickens/'


def add_eggs(request, chicken_id):
 
    form = EggsForm(request.POST)
   
    if form.is_valid():
    
        new_eggs = form.save(commit=False)
        new_eggs.chicken_id = chicken_id
        new_eggs.save()
    return redirect('chicken-detail', chicken_id=chicken_id)