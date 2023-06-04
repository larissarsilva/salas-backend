from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20, verbose_name = 'Nome')
    surname = models.CharField(max_length=20, verbose_name = 'Sobrenome')
    email = models.EmailField()
    hasValidEmail = models.BooleanField(default = False )
    FIRST_ACCESS = 0
    ADMINISTRADOR = 1
    EMPLOYEE = 2
    SUSPEND = 3
    ROLE_CHOICES = [
        (FIRST_ACCESS, 'Primeiro Acesso'),
        (ADMINISTRADOR, 'Administrador'),
        (EMPLOYEE, 'Funcionário'),
        (SUSPEND, 'Suspenso')
    ]
    role = models.IntegerField (
        choices = ROLE_CHOICES,
        default = FIRST_ACCESS,
        verbose_name = 'Permissões'
    )

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'