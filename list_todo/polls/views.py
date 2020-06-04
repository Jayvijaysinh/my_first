from django.shortcuts import render,redirect
from polls.models import todo
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.utils import timezone
from django.http import HttpResponseRedirect


def home(request):
    todo_item = todo.objects.all().order_by("-added_date")
    return render(request, 'main/index.html',{
        "todo_items" : todo_item
    })


def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    curent_object = todo.objects.create(added_date = current_date, text = content)
    print(curent_object)
    return HttpResponseRedirect("../")

def delete_todo(request,todo_id):
    todo.objects.get(id=todo_id).delete()
    return redirect(home)
