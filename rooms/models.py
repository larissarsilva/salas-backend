from django.db import models
from django.core.validators import MaxValueValidator

class Block(models.Model):
    name = models.CharField(max_length = 1, verbose_name = 'Nome')

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'bloco'
        verbose_name_plural = 'blocos'


class Room(models.Model):
    name = models.CharField(max_length = 6, verbose_name = 'Nome')
    blockId = models.ForeignKey(Block, on_delete = models.PROTECT, verbose_name = 'Bloco')
    isAcessible = models.BooleanField(default=True, verbose_name = 'Acessibilidade')
    hasAirConditioner = models.BooleanField(default=True, verbose_name = 'Ar Condicionado')
    hasFan = models.BooleanField(default=True, verbose_name = 'Ventilador')
    hasProjector = models.BooleanField(default=True, verbose_name = 'Projetor')
    available = models.BooleanField(default=True, verbose_name = 'Disponivel')
    capacity = models.IntegerField(default=True, validators=[MaxValueValidator(100)])
    note = models.CharField(max_length = 100, verbose_name = 'Observações', null = True, blank = True)
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'
