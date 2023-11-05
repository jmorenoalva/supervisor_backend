from django.urls import path

from .views import SupervisorViews, ZoneViews, PromoterViews, QuotaViews, LevelViews, EmployeeViews

urlpatterns = [
    path("api/v1/supervisor/", SupervisorViews.as_view()),
    path("api/v1/supervisor/<int:id>", SupervisorViews.as_view()),
    path("api/v1/zone/", ZoneViews.as_view()),
    path("api/v1/zone/<int:id>", ZoneViews.as_view()),
    path("api/v1/promoter/", PromoterViews.as_view()),
    path("api/v1/promoter/<int:id>", PromoterViews.as_view()),
    path("api/v1/quota/", QuotaViews.as_view()),
    path("api/v1/quota/<int:id>", QuotaViews.as_view()),
    path("api/v1/level/", LevelViews.as_view()),
    path("api/v1/level/<int:id>", LevelViews.as_view()),
    path("api/v1/employee/", EmployeeViews.as_view()),
    path("api/v1/employee/<int:id>", EmployeeViews.as_view()),
]
