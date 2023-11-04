from django.urls import path

from .views import TypeDocumentViews, UbigeoViews, TypeInvoiceViews, PeriodViews

urlpatterns = [
    path("typedocument/", TypeDocumentViews.as_view()),
    path("typedocument/<int:id>", TypeDocumentViews.as_view()),
    path("ubigeo/", UbigeoViews.as_view()),
    path("ubigeo/<int:id>", UbigeoViews.as_view()),
    path("typeinvoice/", TypeInvoiceViews.as_view()),
    path("typeinvoice/<int:id>", TypeInvoiceViews.as_view()),
    path("period/", PeriodViews.as_view()),
    path("period/<int:id>", PeriodViews.as_view()),
]
