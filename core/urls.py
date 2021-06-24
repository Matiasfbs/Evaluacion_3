from django.urls import path
from .views import home, logout, noticias, quienessomos, registro, api, rtx2080, rx5700, hyperxexo, proce, grafica, ram, listado_hardware, nuevo_hardware, modificar_hardware, eliminar_hardware
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home, name="home"),
    path('noticias/', noticias, name="noticias"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('login/',LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('registro/', registro, name="registro"),
    path('api/', api, name="api"),
    path('rtx2080/', rtx2080, name="rtx2080"),
    path('rx5700/', rx5700, name="rx5700"),
    path('hyperxexo/', hyperxexo, name="hyperxexo"),
    path('proce/', proce, name="proce"),
    path('grafica/', grafica, name="grafica"),
    path('ram/', ram, name='ram'),
    path('listado-hardwares/', listado_hardware, name="listado_hardwares"),
    path('nuevo_hardware/', nuevo_hardware, name="nuevo_hardware"),
    path('modificar-hardware/<id>/', modificar_hardware, name="modificar_hardware"),
    path('eliminar-hardware/<id>/', eliminar_hardware, name="eliminar_hardware"),
    path('logout/',LogoutView.as_view(template_name='registration/logout.html') , name="logout"),
    

    
]