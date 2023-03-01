from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm

# checks whether the incoming HTTP request contains form POST data. If
# so, it validates the data and stores it in the database, otherwise it just displays an empty form.


def board(request):
    messages = Message.objects.order_by('-date')
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('board')
    else:
        form = MessageForm()
    return render(request, 'msgboard/board.html', {
        'messages': messages,
        'form': form,
    })
