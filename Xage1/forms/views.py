from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import InfoForm

def forms_view(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            # Vous pouvez accéder aux données du formulaire via form.cleaned_data
            # Cependant, dans ce cas, vous pouvez également utiliser form.save() directement.
            form.save()
            return render(request, 'sucess.html')
        else:
            messages.error(request, 'Le formulaire contient des erreurs. Veuillez corriger les erreurs ci-dessous.')
    else:
        form = InfoForm()

    return render(request, 'forms/formulaire.html', {'form': form})
