from django.db import models

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

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'
