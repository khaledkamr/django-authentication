from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, "user/index.html")

def signup(request):
    if request.method == "POST":
        # username = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "User name already exist! please try other user name")
            return redirect("signup")
        
        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect("signup")
        
        if len(username) > 15:
            messages.error(request, "Username must be under 15 characters")
            return redirect("signup")
        
        if pass1 != pass2:
            messages.error(request, "passwords didn't match!")
            return redirect("signup")
        
        if not username.isalnum():
            messages.error(request, "Username must be alpha-numeric!")
            return redirect('signup')

        myUser = User.objects.create_user(username, email, pass1)
        myUser.first_name = fname 
        myUser.last_name = lname 

        myUser.save()

        messages.success(request, "Your account has been successfully created")
        return redirect('signin')

    return render(request, "user/signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        pass1 = request.POST["pass1"]
        
        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "user/index.html", {'fname':fname})
        else:
            messages.error(request, "Bas credentials!")
            return redirect('home')
            
    return render(request, "user/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home') 