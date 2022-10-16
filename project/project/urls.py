from django.urls import path
from contact_form import views

urlpatterns = [
    path("", views.contactform, name="contact"),
]