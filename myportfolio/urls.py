from django.urls import path

from myportfolio import views

urlpatterns = [
    path('',views.home),
    path('about',views.about),
    path('project',views.project),
    path('main',views.main,name="Home")
]