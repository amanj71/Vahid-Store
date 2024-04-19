from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login_view(request):
    context = {'message': ''}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        print(username, password)   
        if user is not None:
            message = "Welcome back Sir"
            login(request, user)
            return redirect('/admin')
        else:
            context['message'] = "Username or Password is Wrong!"     
    print(context)  
    return render(request, "account/login_page.html", context)

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect("/accounts/")
    context = {"form": form}
    return render(request, "account/register_page.html", context)