from django.shortcuts import render, redirect, get_object_or_404
from .models import Evenement
from .forms import EvenementForm

# Lire (Read) - Afficher la liste des événements
def list_evenements(request):
    evenements = Evenement.objects.all()
    return render(request, 'evernements/index.html', {'evenements': evenements})

# Créer (Create) - Ajouter un nouvel événement
def create_evenement(request):
    if request.method == 'POST':
        form = EvenementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_evenements')
    else:
        form = EvenementForm()
    return render(request, 'evenements/create_evenement.html', {'form': form})

# Mettre à jour (Update) - Modifier un événement existant
def update_evenement(request, evenement_id):
    evenement = get_object_or_404(Evenement, pk=evenement_id)
    if request.method == 'POST':
        form = EvenementForm(request.POST, request.FILES, instance=evenement)
        if form.is_valid():
            form.save()
            return redirect('list_evenements')
    else:
        form = EvenementForm(instance=evenement)
    return render(request, 'evenements/update_evenement.html', {'form': form, 'evenement': evenement})

# Supprimer (Delete) - Supprimer un événement existant
def delete_evenement(request, evenement_id):
    evenement = get_object_or_404(Evenement, pk=evenement_id)
    if request.method == 'POST':
        evenement.delete()
        return redirect('list_evenements')
    return render(request, 'evenements/delete_evenement.html', {'evenement': evenement})
