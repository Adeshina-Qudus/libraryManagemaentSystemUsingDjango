"""
URL configuration for libraryManagementSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# admin.site.site_header = 'holy child'
# admin.site.index_title = 'holy'


urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path('demo/', include('demo.urls')),
    path('catalog/', include('catalog.urls')),
    path('auth/', include("djoser.urls")),
    path('auth/', include("djoser.urls.jwt"))
]
