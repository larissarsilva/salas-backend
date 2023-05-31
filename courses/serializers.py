from rest_framework import serializers
from courses.models import Course, Subject


# Forma como vai representar os dados
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    # Para retornar o objeto de subject no lugar de somente o Id
    # Many = True indica que é um campo many to many
    subjectsIds = SubjectSerializer(many=True)

    class Meta:
        model = Course
        fields = '__all__'
    # Personalizar a saída do serializer
    # def to_representation(self, instance):
    #     response_data = {}
    #     response_data['statusCode'] = 200
    #     return response_data
