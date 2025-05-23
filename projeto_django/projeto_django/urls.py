from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from aplicativo_django.views import home, post_detail, post_new, settings, post_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/new/', post_new, name='post_new'),
    path('post/<int:post_id>/delete/', post_delete, name='post_delete'),

    path('settings/', settings, name='settings'),

    # URLs para login e logout
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]