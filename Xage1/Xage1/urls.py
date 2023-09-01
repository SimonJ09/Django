from django.contrib import admin
from django.urls import path
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('evernements.urls')),
    path('propos/', views.propos_view, name='propos'),
    path("contact/", views.contact_view, name='contact'),
    path('',include('articles.urls')),
    path('',include('forms.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
