# from django.urls import path
# from .views import welcome, about, login, user_actions, past_events

# urlpatterns = [
#     path('', welcome, name='welcome'),
#     path('about/', about, name='about'),
#     path('login/', login, name='login'),
#     path('user-actions/', user_actions, name='user_actions'),
#     path('past-events/', past_events, name='past_events'),
    
# ]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('user_actions/', views.user_actions, name='user_actions'),
    path('past_events/', views.past_events, name='past_events'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('runner_dashboard/', views.runner_dashboard, name='runner_dashboard'),
    path('create_runner/', views.create_runner, name='create_runner'),
    path('view_runner/<int:runner_id>/', views.view_runner, name='view_runner'),
    path('delete_runner/<int:runner_id>/', views.delete_runner, name='delete_runner'),
]
