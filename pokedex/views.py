from django.http import HttpResponse
from django.template import loader
from .models import Pokemon,Trainer
from pokedex.forms import PokemonForm, TrainerForm
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

def index(request):
    pokemons = Pokemon.objects.order_by('name')
    template = loader.get_template('index.html')
    return HttpResponse(template.render(
        {'pokemons': pokemons,                        
        },
        request))

def pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(pk = pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))


def trainer(request, trainer_id):
    trainer = Trainer.objects.get(pk = trainer_id)
    template = loader.get_template('display_trainer.html')
    context = {
        'trainer': trainer
    }
    return HttpResponse(template.render(context, request))

def trainers(request):
    trainers = Trainer.objects.all()
    template = loader.get_template('trainers.html')
    return HttpResponse(template.render(
    {'trainers': trainers,                       
    },
        request))
    
@login_required #Pokemon
def add_pokemon (request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')    
    else:
        form = PokemonForm()
    
    return render(request, 'pokemon_form.html', {'form': form})

@login_required
def edit_pokemon (request, pokemon_id):
    pokemon = Pokemon.objects.get(pk = pokemon_id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon) 
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')    
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'pokemon_form.html', {'form': form})

@login_required
def delete_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(pk = pokemon_id)
    pokemon.delete()
    return redirect('pokedex:index')


@login_required #Trainer
def add_trainer (request):
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('pokedex:trainers')    
    else:
        form = TrainerForm()
    
    return render(request, 'trainer_form.html', {'form': form})

@login_required
def edit_trainer (request, trainer_id):
    trainer = Trainer.objects.get(pk = trainer_id)
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES, instance=trainer) 
        if form.is_valid():
            form.save()
            return redirect('pokedex:trainers')    
    else:
        form = TrainerForm(instance=trainer)
    return render(request, 'trainer_form.html', {'form': form})

@login_required
def delete_trainer(request, trainer_id):
    trainer = Trainer.objects.get(pk = trainer_id)
    trainer.delete()
    return redirect('pokedex:trainers')



class CustomLoginView(LoginView):
    template_name = 'login_form.html'
    