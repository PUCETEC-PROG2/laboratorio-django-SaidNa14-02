from django.db import models

# Create your models here.
class Trainer(models.Model):
    name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    level = models.PositiveSmallIntegerField(default=1)
    birth_date = models.DateField(null=False)
    picture = models.ImageField(upload_to='trainer_images', null=True)

    def __str__(self):
        return f"{self.name} {self.last_name}"

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
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)
    picture = models.ImageField(upload_to='pokemon_images', null=True)
    
    def __str__(self):
        return self.name
    



    