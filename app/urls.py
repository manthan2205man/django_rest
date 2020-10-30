from django.urls import path,include
from .views import *
from . import views
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)
router.register("Studentmdodel", views.Studentapi)
router.register("Marksmodel", views.Marksapi)


urlpatterns = [
    path('', include(router.urls)),
    path('home/',views.home ),
    path('login/', views.Login.as_view()),
    path('token/', views.TokenAuthentication),


    # path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('users/', views.UserList.as_view()),

]