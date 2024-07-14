from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import buscar_cep
from .views import on_change_pais
from .views import on_change_estado
from .views import signup
from .views import resetar_senha
from .views import ChangePasswordView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="login/index.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('buscar_cep/', buscar_cep, name="buscar_cep"),
    path('on_change_pais/', on_change_pais, name="on_change_pais"),
    path('on_change_estado/', on_change_estado, name="on_change_estado"),
    path('signup/', signup, name='signup'),
    path('', include('django.contrib.auth.urls')),
    path('resetar_senha/', resetar_senha, name='resetar_senha'),
    path('change_password/', ChangePasswordView.as_view()),
]