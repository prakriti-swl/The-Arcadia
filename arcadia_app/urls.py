from django.urls import path
from arcadia_app import views

urlpatterns = [
    path("",views.HomeView.as_view(), name= "home"),
    path('events/', views.EventSliderView.as_view(), name='events'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('detailed_menu/', views.DetailedMenuView.as_view(), name='detailed_menu'),
    # path('review/', views.review, name='review'),
    # path('event/', views.event, name='event'),
    # path('gallery/', views.gallery, name='gallery'),
    path('booking/', views.IntroSectionView.as_view(), name='booking'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
