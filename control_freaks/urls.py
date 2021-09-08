"""control_freaks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView
from . import views
from control_freaks.views import HomePageView, InformView, InformActionView, InformFilmView, InfromFutureView, InformOpinionView, InformSeriousView, ContactView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('inform', InformView.as_view(), name='inform'),
    path('inform/action', InformActionView.as_view(), name='inform_action'),
    path('inform/film', InformFilmView.as_view(), name='inform_film'),
    path('inform/future', InfromFutureView.as_view(), name='inform_future'),
    path('inform/opinion', InformOpinionView.as_view(), name='inform_opinion'),
    path('inform/serious', InformSeriousView.as_view(), name='inform_serious'),
    path('contact', ContactView.as_view(), name='contact'),
    path('', include('stories.urls')),
    path('', include('submit.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
