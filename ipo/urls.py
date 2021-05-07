from django.urls import path
from .views import IpoView, IpoRetrieveView, IpoExceptionView

urlpatterns = [
    path("", IpoView.as_view()),
    path("exceptions/", IpoExceptionView.as_view()),
    path("<str:company_code>/", IpoRetrieveView.as_view())
]