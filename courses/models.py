from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length = 40, verbose_name = 'Curso')
    MORNING = 1
    AFTERNOON = 2
    NIGHT = 3
    SHIFT_CHOICES = [
        (MORNING, "Manhã"),
        (AFTERNOON, "Tarde"),
        (NIGHT, "Noite")
    ]
    shift = models.IntegerField (
        choices = SHIFT_CHOICES,
        default = MORNING
    )
    subjectsIds = models.ManyToManyField('Subject', related_name = 'coursesId', blank = True, null = True, verbose_name = 'Disciplinas') # Related name permite que eu acesse cursos a partir de matérias

    def __str__(self):
        return f"{self.name}" #Retorna a instância como uma string
    

class Subject(models.Model):
    name = models.CharField(max_length = 25, verbose_name = 'Nome')
    code = models.CharField(max_length = 25, verbose_name = 'Código')
    workload = models.IntegerField(verbose_name = 'Carga Horária')
    group = models.CharField(max_length = 2, verbose_name = 'Grupo')
    coursesIds = models.ManyToManyField('Course', blank = True, null = True, verbose_name=('Curso(s)'))

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'