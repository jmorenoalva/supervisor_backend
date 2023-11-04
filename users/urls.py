from django.urls import path

from . import views

urlpatterns = [
  path('register/', views.register),
  #path('user/',UserViews.as_view())
]