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
    path('parent-add-money/', views.ParentAddMoney, name='ParentAddMoney'),
    path('profile/', views.Profile, name='Profile'),
    path('parent-update-money/', views.ParentUpdateMoney, name='ParentUpdateMoney'),
    path('quiz/', views.Quiz, name='Quiz'),
    path('quiz2/', views.Quiz2, name='Quiz2'),
    path('module/', views.module, name='module'),
    path('buy-item/', views.BuyItem, name='BuyItem'),
    path('portfolio/', views.Portfolio, name='Portfolio'),
    
]

