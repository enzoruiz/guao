from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import AnuncioForm
from .models import Anuncio
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Create your views here.

class PublishView(TemplateView):
	def get(self, request, *args, **kwargs):
		anuncio = None
		if len(args) > 0:
			id_anuncio = int(args[0])
			anuncio = get_object_or_404(Anuncio, pk=id_anuncio)
		return render(request, "publish.html", { 'anuncio' : anuncio })

	def post(self, request, *args, **kwargs):
		if request.POST.get('anuncio_id') == '':
			# CREACION
			form = AnuncioForm(request.POST, request.FILES)
			if form.is_valid():
				anuncio = form.save(commit=False)

				anuncio.creador = request.user
				anuncio.save()
				return redirect('publish')
			else:
				print(form.errors)
				return redirect('publish')
		else:
			# EDICION
			pass
			# pro = get_object_or_404(Producto, pk=request.POST.get('product_id'))
			# try:
			# 	pro.imagen = request.FILES['imagen']
			# except Exception:
			# 	pass
			# form = ProductForm(request.POST or None, request.FILES, instance=pro)
			
			# if form.is_valid():
			# 	form.save()
			# 	return redirect('publish')
			# else:
			# 	print(form.errors)
			# 	return redirect('publish')