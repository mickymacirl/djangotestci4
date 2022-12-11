from . import views
from django.urls import path

# This is a list of URL patterns for the blog app.
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
