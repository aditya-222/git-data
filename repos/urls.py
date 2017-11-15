from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'allrepos/',views.allrepos , name = 'allrepos' ),
]