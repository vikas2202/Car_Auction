from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include your app URLs
    path('', include('auction.urls')),  # Replace 'auction' with your app name if different

    # Optional override of login view
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
]

# Media file handling
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
