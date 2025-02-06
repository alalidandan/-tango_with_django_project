from django.urls import path
from rango import views  # Import views from the Rango app

urlpatterns = [
    path('', views.index, name='index'),  # Maps `/rango/` to the `index` view
]
