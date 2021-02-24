from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
import datetime
from django.contrib import messages
from  .models import Task

import todoapp.models




def signin (request):
    if request.method == "POST":
        uname = request.POST["username"]
        pwd1 = request.POST['pwd']
        
        user = authenticate(request,username=uname,password=pwd1)
        if user is not None:
            login(request,user)
            return redirect('http://localhost:8000/todoapp/user/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('http://localhost:8000/todoapp/')
    else:
        return render(request, 'todoapp/login.html')
    


def logout(request):
    auth.logout(request)
    return redirect("todoapp.html")



def signup_view(request):

    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if User.objects.filter(username=name).exists():
                messages.info(request,"Username Aready in Use")
                return redirect('http://localhost:8000/todoapp/signup/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email ID Aready in Use")
                return redirect('http://localhost:8000/todoapp/signup/')
            else:
                user = User.objects.create_user(username=name,password=pass1,email=email)
                user.save()
                messages.info(request,"User Registered")
                return redirect("http://localhost:8000/todoapp/")
        else:
            messages.info(request,"Both Password and Confirm password are not matching")
            return render(request, 'todoapp/signup.html')
    else:
        return render(request,'todoapp/signup.html')



def user(request):
    alltasks = Task.objects.filter(user=request.user)
    context = {'alltasks':alltasks}
    return render(request,'todoapp/user.html',context)

    


def insert(request):
    if request.method == 'POST':
       
        Title = request.POST['Title']
        Time = request.POST['Time']
        # status = request.POST['status']
        type2 = request.POST['Task_type']
        tasks =Task.objects.create( user=request.user,Title=Title, Time=Time ,type=type2)
        tasks.save()
        return redirect('todoapp:user')
    else:
        return render(request,'todoapp/insert.html')

    return render(request,'todoapp/insert.html')
    




def delete(request, id):
    task = todoapp.models.Task.objects.get(id=id)
    task.delete()
    return redirect('todoapp:user')









