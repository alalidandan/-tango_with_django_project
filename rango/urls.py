from django.urls import path
from rango import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'rango'

urlpatterns = [
    #maps `/rango/` to the `index` view
    path('', views.index, name='index'),
    #maps '/rango/about/' to 'about'
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
]
