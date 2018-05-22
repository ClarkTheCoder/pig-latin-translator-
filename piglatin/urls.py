from django.conf.urls import url
from django.contrib import admin
from . import views  # import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),  #  homepage
    url(r'^translate/', views.translate, name='translate'),
    url(r'^about/', views.about, name='about'),
]
