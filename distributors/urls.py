from django.urls import path

from .views import DistributorViews, ProductDistributorViews, SalesViews

urlpatterns = [
    path("distributor/", DistributorViews.as_view()),
    path("distributor/<int:id>", DistributorViews.as_view()),
    path("productdistributor/", ProductDistributorViews.as_view()),
    path("productdistributor/<int:id>", ProductDistributorViews.as_view()),
    path("sales/", SalesViews.as_view()),
    path("sales/<int:id>", SalesViews.as_view()),
]
