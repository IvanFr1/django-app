from django.urls import path
from .views import (
    get_cookie_view,
    set_cookie,
    set_session_view,
    get_session_view,
    logout_view,
    MyLogoutView,
    AboutMeView,
    RegisterView,
    FooBarView,
    UpdateProfileView,
    UsersListView,
    UserDetailsView,
    HelloView,
)
from django.contrib.auth.views import LoginView

app_name = 'myauth'

urlpatterns = [
    # path('login/', login_view, name='login),
    path(
        'login/',
        LoginView.as_view(
            template_name='myauth/login.html',
            redirect_authenticated_user=True,
        ),
        name='login',
    ),
    path('hello/', HelloView.as_view(), name='hello'),
    # path('logout/', logout_view, name='logout'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('about-me/', AboutMeView.as_view(), name='about-me'),
    path('profile/<int:pk>/update/', UpdateProfileView.as_view(), name='update_profile'),
    path('users_list/', UsersListView.as_view(), name='users-list'),
    path('users/<int:pk>/', UserDetailsView.as_view(), name='user_details'),
    path('register/', RegisterView.as_view(), name='register'),

    path('cookie/get/', get_cookie_view, name='cookie-get'),
    path('cookie/set/', set_cookie, name='cookie-set'),

    path('session/get/', get_session_view, name='session-get'),
    path('session/set/', set_session_view, name='session-set'),

     path('foo-bar/', FooBarView.as_view(), name='foo-bar'),
]

