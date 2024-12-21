from django.contrib import admin
from .models import Pokemon, Trainer

@admin.register(Pokemon)
@admin.register(Trainer)

class PokemonAdmin(admin.ModelAdmin):
    pass

class TrainerAdmin(admin.ModelAdmin):
    pass
