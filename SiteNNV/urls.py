from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainNNV import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.register),
    path('login/', views.loginf),
    path('profile/', views.profile),

    path('download/attestation-educational/', views.download_attestation_educational),
    path('download/attestation-industrial/', views.download_attestation_industrial),
    path('download/characteristic/', views.download_characteristic),
    path('download/all/', views.download_all_documents_zip),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)