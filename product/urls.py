from django.urls import path

from .views import UnitViews, ActiveIngredientViews, PresentationViews, ProductViews

urlpatterns = [
    path("unit/", UnitViews.as_view()),
    path("unit/<int:id>", UnitViews.as_view()),
    path("activeingredient/", ActiveIngredientViews.as_view()),
    path("activeingredient/<int:id>", ActiveIngredientViews.as_view()),
    path("presentation/", PresentationViews.as_view()),
    path("presentation/<int:id>", PresentationViews.as_view()),
    path("product/", ProductViews.as_view()),
    path("product/<int:id>", ProductViews.as_view()),
]
