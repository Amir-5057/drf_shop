from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/media/', include('media.urls')),
    path('api/products/', include('products.urls')),
]
