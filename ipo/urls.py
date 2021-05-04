from django.urls import path
from .views import IpoView, IpoRetrieveView

urlpatterns = [
    path("", IpoView.as_view()),
    path("<str:company_code>/", IpoRetrieveView.as_view())
]