from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("apply/<int:program_id>/", views.apply, name="apply"),
]
