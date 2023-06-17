from django.db import models

class Classes(models.Model):
    startTime = models.TimeField(verbose_name = 'Horário de Início')
    endTime = models.TimeField(verbose_name = 'Horário de Término')
    subjectId = models.ForeignKey('courses.Subject', on_delete = models.CASCADE, verbose_name = 'Disciplina')
    roomId = models.ForeignKey('rooms.Room', on_delete = models.CASCADE, verbose_name = 'Sala')
    professorsId = models.ManyToManyField('professors.Professor', verbose_name = 'Professor(es)')
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    DAY_CHOICES = [
        (MONDAY, "Segunda"),
        (TUESDAY, "Terça"),
        (WEDNESDAY, "Quarta"),
        (THURSDAY, "Quinta"),
        (FRIDAY, "Sexta"),
        (SATURDAY, "Sábado")
    ]
    day = models.IntegerField (
        choices = DAY_CHOICES,
        default = MONDAY,
        verbose_name = 'Dia da Semana'
    )

    def __str__(self):
        return f'{self.subjectId} - {self.startTime} - {self.endTime} - {self.roomId} - {self.day}'
    
    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'