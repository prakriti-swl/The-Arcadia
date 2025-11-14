from django.urls import path

from dashboard import views
urlpatterns = [
    path("dash/", views.DashboardView.as_view(), name="dash"),
    path("published-post/", views.PublishedPost.as_view(), name="published-post"),
    path("category/", views.CategoryView.as_view(), name="category"),
    path("tag/", views.TagView.as_view(), name="tag"),


    path("post-create/", views.PostCreateView.as_view(), name="post-create"),
    path("post-delete/<int:pk>/", views.PostDeleteView.as_view(), name= 'post-delete'),
    path("post-update/<int:pk>/", views.PostUpdateView.as_view(), name= 'post-update'),
    path("dashpost-detail/<int:pk>/", views.DashPostDetailView.as_view(), name= 'dashpost-detail'),

    path("tag-create/", views.TagCreateView.as_view(), name="tag-create"),
    path("tag-delete/<int:pk>/", views.TagDeleteView.as_view(), name= 'tag-delete'),
    path("tag-update/<int:pk>/", views.TagUpdateView.as_view(), name="tag-update"),

    path("category-create/", views.CategoryCreateView.as_view(), name="category-create"),
    path("category-delete/<int:pk>/", views.CategoryDeleteView.as_view(), name="category-delete"),
    path("category-update/<int:pk>/", views.CategoryUpdateView.as_view(), name="category-update"),

]
