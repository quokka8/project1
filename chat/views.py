# chat/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Message
from .forms import MessageForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Room

def index(request):
   return render(request, "chat/index.html")

@login_required
def room(request, room_name):
    # Retrieve the Room object based on room_name
    room = get_object_or_404(Room, book_title=room_name)

    room_messages = Message.objects.filter(room=room_name).order_by('timestamp')

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            Message.objects.create(content=content, room=room_name, user=request.user)

            # Redirect to the same page to avoid form resubmission on refresh
            return redirect('room', room_name=room_name)
    else:
        form = MessageForm()

    # Retrieve the updated room data from the database
    updated_room = Room.objects.get(book_title=room_name)

    context = {
        'room_name': room_name,
        'user': request.user,
        'room_messages': room_messages,
        'form': form,
        'room': updated_room,  # Include the updated room data in the context
    }

    return render(request, 'chat/room.html', context)



