from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.index, name='index'),
    path('register/',views.register, name='register'),
    #path('', include("django.contrib.auth.urls")),         login using django.contrib.auth
    path('test/',views.test, name='test'),
    path('login/',views.login_view, name='login'),
    #path('login-match/',views.login_match, name='login_match'),
    path('logout/',views.logout_view, name='logout'),

]