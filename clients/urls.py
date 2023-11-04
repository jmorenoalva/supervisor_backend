from django.urls import path

from .views import TypeClientViews, ClientViews, SitesClientViews, ContactViews

urlpatterns=[
  path("typeclient/", TypeClientViews.as_view()),
  path("typeclient/<int:id>", TypeClientViews.as_view()),
  path("client/", ClientViews.as_view()),
  path("client/<int:id>", ClientViews.as_view()),
  path("sitesclient/", SitesClientViews.as_view()),
  path("sitesclient/<int:id>", SitesClientViews.as_view()),
  path("contact/", ContactViews.as_view()),
  path("contact/<int:id>",ContactViews.as_view()),
]