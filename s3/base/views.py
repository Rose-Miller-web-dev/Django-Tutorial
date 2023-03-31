from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm, MessageForm
# Create your views here.

# rooms = [
#     {'id': 1, 'name':'fool'},
#     {'id': 2, 'name':'dumb'},
#     {'id': 3, 'name':'stupid'},
# ]

houses = [
    {'id': 1, 'name':'villa'},
    {'id': 2, 'name':'apartment'},
    {'id': 3, 'name':'home'},
]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    # for r in rooms :
    #     if r['id'] == int(pk):
    #         this_room = r
    # context = {'room': this_room}
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def nav(request):
    return render(request, 'base/navbar.html')

def createRoom(request):
    form = RoomForm()
    context = {'form': form}
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    return render(request, 'base/room_form.html', context)

def createMessage(request):
    form = MessageForm()
    context = {'form': form}
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect(home)

    context ={'form': form}
    return render(request, 'base/room_form.html', context)

def delete(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect(home)
    context = {'obj': room.name}
    return render(request, 'base/delete.html', context)