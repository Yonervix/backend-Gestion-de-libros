from rest_framework import serializers
from .models import Libro

class LibroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Libro
        fields = ('id', 'titulo', 'autor', 'precio', 'fecha_publicacion')


class LibroSerializerReg(serializers.ModelSerializer):

    class Meta:
        model = Libro
        fields = ('id', 'titulo', 'autor', 'precio', 'fecha_publicacion')


class LibroSerializerUpdate(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Libro
        fields = ('id', 'titulo', 'autor', 'precio', 'fecha_publicacion')


class LibroSerializerDelete(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Libro
        fields = ('id',)