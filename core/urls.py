"""core URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from core import settings

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('store/', include('store.urls', namespace='store')),

    path('apropos', TemplateView.as_view(template_name='apropos.html'), name='apropos'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('faq', TemplateView.as_view(template_name='faq.html'), name='faq'),

    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Administration MyPet"
admin.site.index_title = "Administration"
