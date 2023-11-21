from django.shortcuts import render, get_object_or_404, redirect
from .models import Collection, Book, Chapter
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from allbooks.models import UserProfile
from django.http import JsonResponse
from .models import Book, UserProfile
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from chat.models import Room
from chat.forms import RoomUpdateForm

def book_catalog(request):
    collections = Collection.objects.all()
    return render(request, 'main/book_catalog.html', {'collections': collections})


def collection_detail(request, collection_id):
    collection = get_object_or_404(Collection, id=collection_id)
    books = collection.book_set.all()  # Assuming your Book model has a related_name='book_set'
    return render(request, 'allbooks/collection_detail.html', {'collection': collection, 'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    chapters = Chapter.objects.filter(book=book)
    return render(request, 'allbooks/book_detail.html', {'book': book, 'chapters': chapters})

def chapter_detail(request, chapter_id):
    chapter = get_object_or_404(Chapter, pk=chapter_id)
    return render(request, 'allbooks/chapter_detail.html', {'chapter': chapter})

def books_in_collection(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)
    books = Book.objects.filter(collection=collection)
    return render(request, 'allbooks/books_in_collection.html', {'collection': collection, 'books': books})
@login_required
def fag(request):
  
    return render(request, 'allbooks/fag.html')

@login_required
def reading_list(request):
    user_profile = request.user.userprofile
    reading_list = user_profile.reading_list.all()
    return render(request, 'main/reading_list.html', {'reading_list': reading_list})

@login_required
def group_readings(request):
    user_profile = request.user.userprofile
    group_readings = user_profile.group_readings.all()
    return render(request, 'main/group_readings.html', {'group_readings': group_readings})

@login_required
def reading_list_partial(request):
    user_profile = request.user.userprofile
    reading_list = user_profile.reading_list.all()
    return render(request, 'main/reading_list_partial.html', {'reading_list': reading_list})

@login_required
def group_readings_partial(request):
    user_profile = request.user.userprofile
    group_readings = user_profile.group_readings.all()
    return render(request, 'main/group_readings_partial.html', {'group_readings': group_readings})


@login_required
def add_to_reading_list(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        # Create a new UserProfile for the user
        user_profile = UserProfile.objects.create(user=request.user)
    
    # Add book to reading list logic here
    user_profile.add_book_to_reading_list(book)

    # Return a JSON response
    return JsonResponse({'message': 'Book added to group readings successfully.'})

    # Redirect the user to a different page (adjust the URL as needed)
    
@login_required
def add_to_group_readings(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        # Create a new UserProfile for the user
        user_profile = UserProfile.objects.create(user=request.user)
    
    # Add book to reading list logic here
    user_profile.add_book_to_group_readings(book)

    # Return a JSON response
    return JsonResponse({'message': 'Book added to reading list successfully.'})

    # Redirect the user to a different page (adjust the URL as needed)    
    
@login_required
@require_POST
def remove_from_reading_list(request, book_id):
    user_profile = request.user.userprofile
    book = get_object_or_404(Book, pk=book_id)

    # Check if the user has the book in their reading list before removing
    if book in user_profile.reading_list.all():
        # Remove book from reading list logic here
        user_profile.remove_book_from_reading_list(book)
        return JsonResponse({'message': 'Book removed from reading list successfully.', 'success': True})
    else:
        return JsonResponse({'message': 'Book not found in reading list.'}, status=404)    
    
@login_required
@require_POST
def remove_from_group_readings(request, book_id):
    user_profile = request.user.userprofile
    book = get_object_or_404(Book, pk=book_id)

    # Check if the user has the book in their reading list before removing
    if book in user_profile.group_readings.all():
        # Remove book from reading list logic here
        user_profile.remove_book_from_group_readings(book)
        return JsonResponse({'message': 'Book removed from group readigns successfully.', 'success': True})
    else:
        return JsonResponse({'message': 'Book not found in group readings.'}, status=404) 


@csrf_exempt 
def create_chat_room(request, book_title):
    # Check if the room already exists
    room, created = Room.objects.get_or_create(book_title=book_title)

    print(f"Room created: {created}")
    print(f"Current Goal: {room.current_goal}")
    print(f"Next Discussion: {room.next_discussion}")
    print(f"Host: {room.host}")
    if created:
        # Set initial values for current_goal and next_discussion
        room.current_goal = '50-90 pages'
        room.next_discussion = timezone.now() + timezone.timedelta(days=7)
        room.host = request.user
        room.save()
    
               
    return JsonResponse({'room_name': room.book_title})
@login_required
def update_room(request, room_name):
    print(f"Room name: {room_name}")
    print(f"User: {request.user}")
    room = get_object_or_404(Room, book_title=room_name)

    if request.method == 'POST':
        form = RoomUpdateForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room', room_name=room.book_title)
    else:
        form = RoomUpdateForm(instance=room)

    return render(request, 'chat/update_room.html', {'form': form, 'room': room})

