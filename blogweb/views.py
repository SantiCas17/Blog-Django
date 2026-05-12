from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post


def lista_posteos(request):
    posteos = Post.objects.all().order_by('-fecha_creacion')
    return render(request, 'blogweb/lista_posteos.html', {'posteos': posteos})

class AcercaDe(TemplateView):
    template_name = 'blogweb/acerca_de.html'


def registro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    else:
        formulario = UserCreationForm()
    return render(request, 'blogweb/registro.html', {'formulario': formulario})

class EditarPerfil(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = 'blogweb/perfil.html'
    success_url = reverse_lazy('lista_posteos')

    def get_object(self):
        return self.request.user

class CrearPost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['titulo', 'cuerpo', 'imagen']
    template_name = 'blogweb/crear_post.html'
    success_url = reverse_lazy('lista_posteos')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class EditarPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['titulo', 'cuerpo', 'imagen']
    template_name = 'blogweb/editar_post.html'
    success_url = reverse_lazy('lista_posteos')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.autor

class BorrarPost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blogweb/borrar_post.html'
    success_url = reverse_lazy('lista_posteos')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.autor