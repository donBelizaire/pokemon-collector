# Add the following import
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pokemon
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm



# class Pokemon:
#     def __init__(self, name, description, attack, weakness, age):
#         self.name = name
#         self.description = description
#         self.attack = attack
#         self.weakness = weakness
#         self.age = age

# pokemon = [
#     Pokemon('Charmander', 'Fire-lizard', 'ember', 'rain', 3),
#     Pokemon('Bulbasour', 'Plant-dinarour thing', 'razor leaf','spicy food', 65000000000),
#     Pokemon('Squertal', 'Water-turtle', 'water gun', 'the quilted quicker picker upper', 4)
# ]


# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def pokemon_index(request):
    pokemon = Pokemon.objects.all()
    return render(request, 'pokemon/index.html', { 'pokemon': pokemon })

def pokemon_detail(request, pokemon_id):
  pokemon = Pokemon.objects.get(id=pokemon_id)
  feeding_form = FeedingForm()
  return render(request, 'pokemon/detail.html', { 
    'pokemon': pokemon, 
    'feeding_form': feeding_form, 
    'toys': toys_cat_doesnt_have
 })

def add_feeding(request, cat_id):
  # create the ModelForm using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.cat_id = cat_id
    new_feeding.save()
  return redirect('detail', pokemon_id=pokemon_id)

class PokemonCreate(CreateView):
  model = Pokemon
  fields = '__all__'
  success_url = '/pokemon/'

class PokemonUpdate(UpdateView):
  model = Pokemon
  # Let's make it impossible to rename a cat :)
  fields = ['name', 'description', 'age']

class PokemonDelete(DeleteView):
  model = Pokemon
  success_url = '/pokemon/'

