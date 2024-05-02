from django.urls import path
from . import views


app_name = 'chat'

urlpatterns = [
    #calls
    path('chat', views.lobby, name='chat'),
    path('room/', views.room),
    path('get_token/', views.getToken),
    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),
    #messages
    path('message/', views.CreateRoom, name='create-room'),
    path('private-chat/<int:assignmemt_id>/', views.MessageView, name='private-room'),
]