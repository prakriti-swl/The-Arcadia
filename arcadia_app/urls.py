from django.urls import path
from arcadia_app import views

urlpatterns = [
    path("",views.HomeView.as_view(), name= "home"),
    # path('menu/', views.menu, name='menu'),
    # path('review/', views.review, name='review'),
    # path('event/', views.event, name='event'),
    # path('gallery/', views.gallery, name='gallery'),
    # path('booking/', views.booking, name='booking'),
]