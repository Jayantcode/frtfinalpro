
from django.urls import path
from blogapp import views 

urlpatterns = [
    path('register/' , views.user_register),
    path('blogs-list/', views.blog_list_view),
    path('get/blog/<int:id>/', views.get_blogs_by_id),
    path('create/new/blog/', views.create_blog_post),
    path('update/<int:id>/', views.update_blog_post),
    path('delete/<int:id>/', views.delete_blog_post)
]