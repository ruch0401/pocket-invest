from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name="home"),
    path('sign-in/', views.SignIn, name="sign-in"),
    path('sign-up/', views.SignUp, name="sign-up"),
    path('child-dashboard/', views.ChildDashboard, name='ChildDashboard'),
    path('market-place/', views.ChildMarketPlace, name='ChildMarketPlace'),
    path('courses/', views.ChildCourses, name='ChildCourses'),
    path('parent-dashboard/', views.ParentDashboard, name='ParentDashboard'),
]