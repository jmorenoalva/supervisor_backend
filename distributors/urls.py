from django.urls import path

from .views import DistributorViews, ProductDistributorViews, SalesViews

urlpatterns = [
    path("api/v1/distributor/", DistributorViews.as_view()),
    path("api/v1/distributor/<int:id>", DistributorViews.as_view()),
    path("api/v1/productdistributor/", ProductDistributorViews.as_view()),
    path("api/v1/productdistributor/<int:id>", ProductDistributorViews.as_view()),
    path("api/v1/sales/", SalesViews.as_view()),
    path("api/v1/sales/<int:id>", SalesViews.as_view()),
]
