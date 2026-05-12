from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.lista_posteos, name='lista_posteos'),
    path('acerca-de/', views.AcercaDe.as_view(), name='acerca_de'),
    path('login/', LoginView.as_view(template_name='blogweb/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='lista_posteos'), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.EditarPerfil.as_view(), name='perfil'),
    path('crear-post/', views.CrearPost.as_view(), name='crear_post'),
    path('editar-post/<int:pk>/', views.EditarPost.as_view(), name='editar_post'),
    path('borrar-post/<int:pk>/', views.BorrarPost.as_view(), name='borrar_post'),
]