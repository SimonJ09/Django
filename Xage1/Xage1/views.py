from django.http import HttpResponse
from .form import ContactForm
from .form import ContactForm
from django.contrib import messages
import smtplib
from email.mime.text import MIMEText
from django.shortcuts import render, redirect



def propos_view(request):
    return render(request, 'propos.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            # Récupérez les données du formulaire
            name = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Construisez le contenu de l'e-mail
            subject = 'Nouveau message de {}'.format(name)
            body = 'Nom: {}\nEmail: {}\nMessage:\n{}'.format(name, email, message)

            # Configurer les détails du serveur SMTP
            smtp_server = 'smtp.gmail.com'  # Remplacez par le serveur SMTP de votre fournisseur de messagerie
            smtp_port = 587  # Port SMTP (587 est généralement utilisé pour TLS)
            smtp_username = 'judesimongbeliana@gmail.com'  # Votre adresse e-mail
            smtp_password = 'Simon09@09@09'  # Votre mot de passe

            # Créez un objet MIMEText pour l'e-mail
            msg = MIMEText(body)

            # Configurez les en-têtes de l'e-mail
            msg['Subject'] = subject
            msg['From'] = smtp_username
            msg['To'] = 'judesimongbeliana@gmail.com'  # Adresse e-mail de destination

            try:
                # Établissez une connexion SMTP sécurisée
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()
                server.login(smtp_username, smtp_password)

                # Envoyez l'e-mail
                server.sendmail(smtp_username, 'judesimongbeliana@gmail.com', msg.as_string())

                # Fermez la connexion SMTP
                server.quit()

                # Redirigez l'utilisateur vers une page de remerciement
                return redirect('merci')

            except Exception as e:
                # Gérez les erreurs d'envoi d'e-mail ici
                return render(request, 'erreur.html', {'error_message': str(e)})

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


