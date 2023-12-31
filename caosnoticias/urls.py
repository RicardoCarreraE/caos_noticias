"""
URL configuration for caosnoticias project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('registro/', views.registro, name="registro"),
    path('Formulario/', views.Formulario, name="Formulario"),
    path('tasks/', views.tasks, name="tasks"),
    path('tasks_completed/', views.tasks_completed, name="tasks_completed"),
    path('tasks/create/', views.create_task, name="create_task"),
    path('tasks/<int:task_id>/', views.task_detail, name="task_detail"),
    path('tasks/<int:task_id>/complete', views.complete_task, name="complete_task"),
    path('tasks/<int:task_id>/delete', views.delete_task, name="delete_task"),
    path('logout/', views.cerrar_sesion, name="logout"),
    path('iniSesion/', views.iniSesion, name="iniSesion"),
    path('DEPORTE/', views.DEPORTE, name="DEPORTE"),
    path('POPULAR/', views.POPULAR, name="POPULAR"),
    path('POLITICA/', views.POLITICA, name="POLITICA"),
    path('base2/', views.base2, name="base2"),
    path('resultados-busqueda/', views.buscar, name='resultados_busqueda'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





