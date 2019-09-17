from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'accounts'

urlpatterns = [
    # LoginView and LogoutView are pre-constructed in Django
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    # I am using the default template for LogoutView
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', views.SignUp.as_view(), name="signup"),
]
