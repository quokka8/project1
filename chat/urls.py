# chat/urls.py
from django.urls import path

from . import views
from allbooks.views import update_room, create_chat_room


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
    path('update_room/<str:room_name>/', update_room, name='update_room'),
]