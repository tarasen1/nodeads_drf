from django.urls import path, include
from . import views
from rest_framework import routers


urlpatterns = [
    path('', views.index, name='index'),
    path('groups/', views.GroupView.as_view()),
    path('groups/<int:id>/', views.GroupView.as_view()),
    path('post_element/', views.ElementView.as_view()),
]
