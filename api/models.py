from django.db import models
from email.policy import default
from django.utils import timezone
# Create your models here.

class Producto(models.Model) :
    CATEGORIAS = (
        ('Instrumento de cuerda', (
            ('Guitarras', 'Guitarras'),
            ('Bajos', 'Bajos'),
            ('Pianos', 'Pianos')
        )),
        ('Percusion', (
            ('Baterias Acusticas', 'Baterias Acusticas'),
            ('Bateria Electronica', 'Bateria Electronica')
        )),
        ('Amplificadores', (
            ('Cabezales', 'Cabezales'),
            ('Cajas', 'Cajas')
        )),
        ('Accesorios varios', 'Accesorios varios')
    )

    categoria = models.CharField(max_length=25, choices=CATEGORIAS, null=True)
    marca = models.CharField(max_length=30)
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=35)
    valor = models.IntegerField()
    fecha = models.DateTimeField(default=timezone.now)
    img = models.ImageField(upload_to='img', null=True)

    def __str__(self) :
        return self.nombre

class Cliente(models.Model) :
    nombre =  models.CharField(max_length=30)
    rut = models.CharField(max_length=9)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=12)
    direccion = models.CharField(max_length=30)
    
    def __str__(self) :
        return self.nombre

