from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('items.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    #path('<int:items_user_id>', views.seller, name='seller'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
