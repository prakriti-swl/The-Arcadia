from django.urls import path
from arcadia_app import views

urlpatterns = [
    path("",views.HomeView.as_view(), name= "home"),
    path('events/<slug:slug>/', views.EventDetailView.as_view(), name='event_detail'),
    path('detailed_menu/', views.DetailedMenuView.as_view(), name='detailed_menu'),
    path("post-list", views.PostListView.as_view(), name = "post-list"),
    # path("post-detail/<int:pk>/", views.PostDetailView.as_view(), name= "post-detail"),
    path("post-detail/<int:pk>/", views.PostDetailView.as_view(), name= "post-detail"),
    path("post-comment/", views.CommentView.as_view(), name= "post-comment"),
    path("video/", views.VideoView.as_view(), name= "video"),
    path("post-by-category/<int:category_id>/", views.PostByCategoryView.as_view(), name= "post-by-category"),
    path("post-search/", views.PostSearchView.as_view(), name= "post-search"),
    path('reservation/', views.ReservationView.as_view(), name='reservation'),
    path('gallery/', views.GalleryView.as_view(), name='gallery'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path("newsletter/", views.NewsletterView.as_view(), name= "newsletter"),
]
