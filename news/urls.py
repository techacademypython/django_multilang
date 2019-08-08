from django.urls import path
from news import views

urlpatterns = [
    path('', views.index_view, name="home"),
    path('upload/image', views.picture_add, name="picture-add"),
    path('delete/image', views.picture_delete, name="picture-delete"),
]
