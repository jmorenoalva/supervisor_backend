from django.urls import path

from .views import TypeDocumentViews, UbigeoViews, TypeInvoiceViews, PeriodViews

urlpatterns = [
    path("api/v1/typedocument/", TypeDocumentViews.as_view()),
    path("api/v1/typedocument/<int:id>", TypeDocumentViews.as_view()),
    path("api/v1/ubigeo/", UbigeoViews.as_view()),
    path("api/v1/ubigeo/<int:id>", UbigeoViews.as_view()),
    path("api/v1/typeinvoice/", TypeInvoiceViews.as_view()),
    path("api/v1/typeinvoice/<int:id>", TypeInvoiceViews.as_view()),
    path("api/v1/period/", PeriodViews.as_view()),
    path("api/v1/period/<int:id>", PeriodViews.as_view()),
]
