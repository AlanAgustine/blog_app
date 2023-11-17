from django.urls import path,include
from.import views


urlpatterns = [
    path('viewblog/', views.viewBlog, name="viewBlog"),
    path('addblog/', views.addBlog, name="addBlog"),
    path('userblog/',views.userBlog, name="userBlog"),
]