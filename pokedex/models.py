from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=30, null=False)
    POKEMON_TYPES = {('A', 'Agua'),
                     ('F', 'Fuego'),
                     ('T', 'Tierra'),
                     ('P', 'Planta'),
                     ('E', 'Electrico'),
                     ('R', 'Roca')}
    type = models.CharField(max_length=30, null=False, choices=POKEMON_TYPES)
    weight = models.DecimalField(max_digits=6, decimal_places=4)
    height = models.DecimalField(max_digits=6, decimal_places=4)
    
    def __str__(self):
        return self.name
    
class Trainer(models.Model):
    name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    level = models.PositiveSmallIntegerField(null=False)
    birth_date = models.DateField(null=False)

    def __str__(self):
        return f"{self.name} {self.last_name}"
    


    