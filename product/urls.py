from django.urls import path

from .views import UnitViews, ActiveIngredientViews, PresentationViews, ProductViews

urlpatterns = [
    path("api/v1/unit/", UnitViews.as_view()),
    path("api/v1/unit/<int:id>", UnitViews.as_view()),
    path("api/v1/activeingredient/", ActiveIngredientViews.as_view()),
    path("api/v1/activeingredient/<int:id>", ActiveIngredientViews.as_view()),
    path("api/v1/presentation/", PresentationViews.as_view()),
    path("api/v1/presentation/<int:id>", PresentationViews.as_view()),
    path("api/v1/product/", ProductViews.as_view()),
    path("api/v1/product/<int:id>", ProductViews.as_view()),
]
