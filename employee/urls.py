from django.urls import path

from .views import SupervisorViews, ZoneViews, PromoterViews, QuotaViews, LevelViews, EmployeeViews

urlpatterns = [
    path("supervisor/", SupervisorViews.as_view()),
    path("supervisor/<int:id>", SupervisorViews.as_view()),
    path("zone/", ZoneViews.as_view()),
    path("zone/<int:id>", ZoneViews.as_view()),
    path("promoter/", PromoterViews.as_view()),
    path("promoter/<int:id>", PromoterViews.as_view()),
    path("quota/", QuotaViews.as_view()),
    path("quota/<int:id>", QuotaViews.as_view()),
    path("level/", LevelViews.as_view()),
    path("level/<int:id>", LevelViews.as_view()),
    path("employee/", EmployeeViews.as_view()),
    path("employee/<int:id>", EmployeeViews.as_view()),
]
