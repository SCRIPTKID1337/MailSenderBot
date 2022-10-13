from django.urls import path 
from home import views


urlpatterns = [
    # path('', views.home, name = 'index'),
    path('', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    
    
]
