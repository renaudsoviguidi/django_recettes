from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Recette
from .forms import RecetteForm
import sweetify
from django.urls import reverse
import json


# Create your views here.

# Fonction menant vers la liste des recettes
def index(request):
    recettes = Recette.objects.order_by("-id").all()
    template = loader.get_template("recettes/liste_recette.html")
    context = {
        "recettes": recettes,
    }
    return HttpResponse(template.render(context, request))


# Fonction permettant d'afficher le formulaire de création des recettes
def create(request):
    recettes = Recette.objects.all()
    template = loader.get_template('recettes/ajouter_recette.html')
    context = {
        'form': RecetteForm,
        'recettes': recettes,
    }
    return HttpResponse(template.render(context, request))


# Fonction permettant de créer une recette
def store(request):
    recettes = Recette.objects.all()
    if request.method == "POST":
        form = RecetteForm(request.POST)
        if form.is_valid():
            nom_agent = form.cleaned_data.get("nom_agent")
            nom_plat = form.cleaned_data.get("nom_plat")
            url_video = form.cleaned_data.get("url_video")
            ingredients = form.cleaned_data.get("ingredients")
            etapes_preparation = form.cleaned_data.get("etapes_preparation")
            time = form.cleaned_data.get("time")

            recettes = Recette.objects.create(
                nom_agent=nom_agent,
                nom_plat=nom_plat,
                url_video=url_video,
                ingredients=ingredients,
                etapes_preparation=etapes_preparation,
                time=time
            )
            recettes.save()
            sweetify.success(request, 'Recette créée avec succès', button="Ok", timer=5000, timerProgressBar=True)
        else:
            # sweetify.error(request, form.errors, button="Ok", timer=5000)
            # return HttpResponseRedirect(reverse('recettes.create'))
            return HttpResponse(form.errors)
    return HttpResponseRedirect(reverse('recettes.index'))


# Fonction permettant d'afficher le formulaire de modification d'une recette
def edit(request, id):
    recette = Recette.objects.select_related().get(id=id)
    template = loader.get_template('recettes/modifier_recette.html')
    context = {
        'recette': recette,
    }
    return HttpResponse(template.render(context, request))


# Fonction permettant de modifier une recette
def update(request, id):
    recette = Recette.objects.select_related().get(id=id)
    if request.method == "POST":
        nom_agent = request.POST['nom_agent']
        nom_plat = request.POST['nom_plat']
        url_video = request.POST['url_video']
        ingredients = request.POST['ingredients']
        etapes_preparation = request.POST['etapes_preparation']
        time = request.POST['time']
        form = RecetteForm(request.POST, instance=recette)
        if form.is_valid():
            nom_agent = nom_agent,
            nom_plat = nom_plat,
            url_video = url_video,
            ingredients = ingredients,
            etapes_preparation = etapes_preparation,
            time = time

            recette.save()
            sweetify.success(request, 'Recette modifiée avec succès', button="Ok", timer=5000, timerProgressBar=True)
        else:
            # sweetify.error(request, "Veuillez remplir les champs", button="Ok", timer=5000)
            # return HttpResponseRedirect(reverse('recettes.edit'))
            return HttpResponse(form.errors)
    return HttpResponseRedirect(reverse('recettes.index'))


# Fonction permettant de supprimer une recette
def delete(request, id):
    recette = Recette.objects.select_related().get(id=id)
    recette.delete()
    sweetify.success(request, 'Supression avec succès', button="Ok", timer=5000)
    return HttpResponseRedirect(reverse('recettes.index'))


from django.shortcuts import render

# Create your views here.
