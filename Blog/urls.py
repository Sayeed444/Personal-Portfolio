from django.urls import path
from . import views
urlpatterns = [
    path('', views.all_blog,name='all_blog'),
    path('details/<int:post_id>/', views.postDetails,name ='postDetails' ),
]
