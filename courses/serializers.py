from rest_framework import serializers
from courses.models import Course


# Forma como vai representar os dados
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('__all__')