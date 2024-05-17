from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from info.views import logout_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', include('info.urls')),
    path('api/', include('apis.urls')),
    path('accounts/login/',
         auth_views.LoginView.as_view(template_name='info/login.html'), name='login'),
    path('accounts/logout/',
         logout_view, name='logout'),
    path('', include('info.urls')),
]

urlpatterns += staticfiles_urlpatterns()