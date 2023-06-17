from rest_framework import serializers
from classes.models import Classes
from courses.serializers import SubjectSerializer
from professors.serializers import ProfessorSerializer

class ClassesSerializer(serializers.ModelSerializer):
    subjectId = SubjectSerializer()
    professorsId = ProfessorSerializer(many = True)
    class Meta:
        model = Classes
        fields = '__all__'