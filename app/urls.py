from django.urls import path
from .import views

urlpatterns=[
    path("",views.home,name="home"),
    path('createfutsal/',views.createfutsal,name="createfutsal"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login_user,name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('addfutsal/',views.addfutsal,name="addfutsal"),
    path('bookfutsal/',views.bookfutsal,name="bookfutsal"),



    
]