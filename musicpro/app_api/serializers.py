from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Producto, Cliente

class UserSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Group
        fields = ['url', 'name']

class ProductoSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Producto
        fields = ['url', 'id', 'categoria', 'nombre', 'marca', 'codigo', 'valor', 'fecha', 'img']

class ClienteSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Cliente
        fields = ['url', 'nombre', 'rut', 'email', 'password', 'direccion']