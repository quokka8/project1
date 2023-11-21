from django.urls import path
from .views import book_catalog
from . import views
from .views import chapter_detail 
from .views import add_to_reading_list, remove_from_reading_list, add_to_group_readings

from .views import reading_list_partial, fag

app_name = 'allbooks'



urlpatterns = [
    path('book-catalog/', book_catalog, name='book-catalog'),
    path('fag/', fag, name='fag'),
    path('collection/<int:collection_id>/', views.collection_detail, name='collection_detail'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('chapter/<int:chapter_id>/', chapter_detail, name='chapter_detail'),
    path('collection/<int:collection_id>/books/', views.books_in_collection, name='books_in_collection'),
    
    
    path('add_to_reading_list/<int:book_id>/', add_to_reading_list, name='add_to_reading_list'),
    path('reading_list/', views.reading_list, name='reading_list'),
    path('remove_from_reading_list/<int:book_id>/', remove_from_reading_list, name='remove_from_reading_list'),
    path('reading_list_partial/', reading_list_partial, name='reading_list_partial'),
    path('create_chat_room/<str:book_title>/', views.create_chat_room, name='create_chat_room'),
    path('add_to_group_readings/<int:book_id>/', add_to_group_readings, name='add_to_group_readings'),

    path('group_readings/', views.group_readings, name='group_readings'),
    path('group_readings_partial/', views.group_readings_partial, name='group_readings_partial'),
    path('remove_from_group_readings/<int:book_id>/', views.remove_from_group_readings, name='remove_from_group_readings'),
    
]
