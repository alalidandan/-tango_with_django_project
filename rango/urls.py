from django.urls import path
from rango import views

urlpatterns = [
    #maps `/rango/` to the `index` view
    path('', views.index, name='index'),
    #maps '/rango/about/' to 'about'
    path('about/', views.about, name='about'),
]
