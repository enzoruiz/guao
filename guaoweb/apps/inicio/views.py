from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import UsuarioForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from .models import Perfil
from apps.sistema.models import Anuncio

# Create your views here.

class HomeView(TemplateView):
	def get(self, request, *args, **kwargs):
		anuncios = Anuncio.objects.all()
		return render(request, "home.html", { "anuncios" : anuncios })

	def post(self, request, *args, **kwargs):
		pass

class ProfileView(TemplateView):
	def get(self, request, *args, **kwargs):
		try:
			telefono = Perfil.objects.get(usuario=request.user).telefono
		except Exception:
			telefono = ""
		return render(request, "profile.html", { 'telefono' : telefono })

	def post(self, request, *args, **kwargs):
		try:
			perfil = Perfil.objects.get(usuario=request.user)
			perfil.telefono = request.POST.get('telefono')
			perfil.save()
		except Exception:
			perfil = Perfil()
			perfil.usuario = request.user
			perfil.telefono = request.POST.get('telefono')
			perfil.save()
		
		return redirect('profile')

class LoginView(TemplateView):
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			return redirect('home')
		else:
			return render(request, "login.html")

	def post(self, request, *args, **kwargs):
		user = authenticate(username=request.POST.get('email'), password=request.POST.get('password'))
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('home')
		else:
			return render(request, 'login.html', {'mensaje' : 'Usuario y/o password invalido.'})

class RegisterView(TemplateView):
	def get(self, request, *args, **kwargs):
		
		return render(request, "register.html")

	def post(self, request, *args, **kwargs):
		form = UsuarioForm(request.POST)
		if form.is_valid():

			user = form.save(commit=False)
			user.username = request.POST.get("email")
			user.password = make_password(request.POST.get("password"))
			user.save()

			user = authenticate(username=request.POST.get('email'), password=request.POST.get('password'))
			login(request, user)
			return redirect("home")
		else:
			print(form.errors)
			return redirect("register")

def LogOut(request):
	logout(request)
	return redirect('login')