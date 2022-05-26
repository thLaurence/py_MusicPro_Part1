from django.urls import path, include, re_path
from .views import api_dolar, index, productos, agregar_producto, eliminar_producto, restar_producto, limpiar_carro 
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', index, name='index'),
    path('productos/', productos, name='productos'),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carro, name="CLS"),
    path('carro/', api_dolar, name='carro')
]

if settings.DEBUG:urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)