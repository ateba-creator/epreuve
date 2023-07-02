from django.urls import path 
from . import views 

urlpatterns = [
    path("",views.index,name='index'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('epreuve',views.addEpreuve,name='addEpreuve'),
    path('upload/', views.file_upload),
    path('form',views.home),
    path('epreuve/delete/<int:id>',views.deletePaper,name='deletePaper'),
]
