from django.urls import path

from .views import TypeClientViews, ClientViews, SitesClientViews, ContactViews, type_client_views

urlpatterns=[
  # path("api/v1/typeclient/", TypeClientViews.as_view()),
  # path("api/v1/typeclient/<int:id>", TypeClientViews.as_view()),
  path('api/v1/typeclient/', TypeClientViews.as_view(), name='type_client_views'),
  path('api/v1/typeclient/<int:id>', TypeClientViews.as_view(), name='type_client_views'),
  path("api/v1/client/", ClientViews.as_view()),
  path("api/v1/client/<int:id>", ClientViews.as_view()),
  path("api/v1/sitesclient/", SitesClientViews.as_view()),
  path("api/v1/sitesclient/<int:id>", SitesClientViews.as_view()),
  path("api/v1/contact/", ContactViews.as_view()),
  path("api/v1/contact/<int:id>",ContactViews.as_view()),
]