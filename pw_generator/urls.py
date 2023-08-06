from django.urls import path
from pw_generator.views import Index

urlpatterns = [
    path('', Index.as_view(), name="index"),
]