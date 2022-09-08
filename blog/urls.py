from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogIndexView.as_view(), name="index"),
    path('list/', views.BlogListView.as_view(), name="blog_list"),
    path('detail/<int:pk>/', views.BlogDetailView.as_view(), name="blog_detail"),
    path('create/', views.BlogCreateView.as_view(), name="blog_create"),
    path('update/<int:pk>/', views.BlogUpdateView.as_view(), name="blog_update"),
    path('delete/<int:pk>/', views.BlogDeleteView.as_view(), name="blog_delete"),
]