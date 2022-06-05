from django.shortcuts import render
from App1.models import ToDoApp
# Create your views here.

def home_view(requests, *args, **kwargs):
    data = ToDoApp.objects.all()

    for i in data: # loops all items in the given database
        item = i.items # here you use dot notation to select actual field you want

    my_context = {
        'items': item,
    }

    return render(requests, 'home.html', my_context)
