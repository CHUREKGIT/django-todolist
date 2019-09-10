from django.shortcuts import render, get_object_or_404, redirect
from .models import List
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):
   return render(request, 'home.html')

@login_required(login_url="/account/signup")
def create(request):
   if request.method == "POST":
        if request.POST['name'] and request.POST['body']:
            list = List()
            list.name = request.POST['name']
            list.body = request.POST['body']
            list.user = request.user
            list.save()
            return redirect('../lists')
        else:
            return render(request, 'create.html', {'error': 'All fields are required!'})
   else:
      return render(request, 'create.html')


def lists(request):
   lists = List.objects
   return render(request, 'lists.html', {'lists':lists})
         

def delete(request, id):
   list = get_object_or_404(List, pk=id)
   if request.method == "POST":
      list.delete()
      return redirect('../../lists')

def editing(request, id):
   list = get_object_or_404(List, pk=id)
   return render(request, 'editing.html', {'list':list})

def edit_save(request, id):
   list = get_object_or_404(List, pk=id)
   if request.method == "POST":
      list.name = request.POST['name']
      list.body = request.POST['body']
      list.save()
      return redirect('../../lists')

