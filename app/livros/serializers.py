from rest_framework import serializers
from .models import Livro

#The serializer convert django models to JSON format to be sent to the API
class LivroSerializer(serializers.ModelSerializer):
    #class Meta indicates the main config of the class
    class Meta:
        model = Livro
        fields = '__all__'