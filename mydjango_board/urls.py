from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.conf import settings

urlpatterns = [
                  path("admin/", admin.site.urls),
                  path('board/', include('board.urls')),
                  path('user/', include('user.urls')),
                  path('api/board/', include('board.api_urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
