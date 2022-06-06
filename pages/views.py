from django.shortcuts import render
from App1.models import ToDoApp
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def home_view(requests, *args, **kwargs):

    data = ToDoApp.objects.all()

    data = ToDoApp.objects.all()

    my_context = {
        'items': data,
    }

    return render(requests, 'home.html', my_context)



@ csrf_exempt
def add_todo(requests, *args, **kwargs):

    content = (requests.POST['content'])
    content = content.capitalize()
    ToDoApp.objects.create(items=content)

    data = ToDoApp.objects.all()

    my_context = {
        'items': data,
    }

    return render(requests, 'home.html', my_context)



