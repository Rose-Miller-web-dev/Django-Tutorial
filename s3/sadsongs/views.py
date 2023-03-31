from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Song, Singer
from .forms import SingerForm
# Create your views here.

def player(request):
    singers = Singer.objects.all()
    return render(request, 'sadsongs/sound.html', {'singers' : singers})

def singer(request, pk):
    # for s in singers:
    #     if int(pk) == s['id']:
    #         singer = s

    song = Song.objects.get(id=pk)
    return render(request, 'sadsongs/singer.html', {'songs': song})


def song(request):
    form = SingerForm()
    context = {'form': form}
    if request.method == 'POST':
        form = SingerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(player)
    return render(request, 'sadsongs/song.html', context)