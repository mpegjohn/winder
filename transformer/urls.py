from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'get-name/', views.get_name),
    url(r'input_data/', views.transformer_data),
]

