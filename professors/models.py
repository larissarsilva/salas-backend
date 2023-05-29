from django.db import models
from courses.models import Course
# Create your models here.
class Professor(models.Model):
    first_name = models.CharField(max_length=25, verbose_name='Primeiro nomme')
    last_name = models.CharField(max_length=25, verbose_name='Último nome')
    courseId = models.ForeignKey(Course, on_delete= models.PROTECT ,verbose_name='Curso')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Professor(a)"
        verbose_name_plural = "Professores(as)"