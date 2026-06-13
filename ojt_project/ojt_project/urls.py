from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # legacy auth path redirect to the app's login view
    path('accounts/login/', RedirectView.as_view(url='/login/', permanent=False)),
    # Redirect any /login/<anything> to the actual login page to avoid ugly 404 debug pages
    path('login/<path:any>/', RedirectView.as_view(url='/login/', permanent=False)),
    path('', include('attendance.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
