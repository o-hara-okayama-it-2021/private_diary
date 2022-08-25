from django.urls import path 
from . import views

app_name = 'testapp' 

urlpatterns = [ 
    path('test/', views.TestappView.as_view(), name="test"), 
] 