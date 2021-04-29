from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("Items.urls")),
    path('auth/', include("Authentications.urls")),
    path('admin/', admin.site.urls),
]
