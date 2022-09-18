from django.urls import path
from webapp import views

urlpatterns = [
    path('', views.Image_view, name='image_upload'),
    
]
