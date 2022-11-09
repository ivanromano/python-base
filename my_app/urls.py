from django.urls import path

# dentro del archivo esta la carpeta views que contiene la funcion
from my_app.views import hello, mabe

urlpatterns = [
    # path('admin/', admin.site.urls),
    #en la ruta principal, ejecuta la funcion
    path('', hello),
    path('mabe/', mabe)
]
