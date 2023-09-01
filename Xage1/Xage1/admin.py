from django.contrib import admin
from forms.models import MonModel
from evernements.models import Evenement
from articles.models import Article

admin.site.register(MonModel)
admin.site.register( Evenement)
admin.site.register( Article)
