from django.contrib import admin
from django.urls import path, include  # Importe 'include' para incluir as URLs do seu aplicativo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('iot.urls')),  # Inclua as URLs do seu aplicativo 'iot' aqui
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
