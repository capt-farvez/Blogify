from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Blogger
from blog.models import Blog

def home_page(request):
    blogs = Blog.objects.all()
    data ={
        'blogs' : blogs
    }
    return render(request, 'home.html', data)

def blogger_signup(request):
    if not request.user.is_authenticated:    
        if request.method == "POST":
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            # Use the email's username
            username = email.split('@')[0]
            password1 = request.POST['psw']
            password2 = request.POST['psw-repeat']
            
            if User.objects.filter(email=email):
                messages.error(request, "Emali already registered!")
                return redirect('/user/signup')
                        
            if password1 != password2:
                messages.error(request, "Password didn't match!")
                return redirect('/user/signup')

            newuser = User.objects.create_user(username, email, password1, first_name=fname, last_name=lname)
            newuser.save()
            blogger = Blogger(user=newuser, bio = " " )
            blogger.save()
            messages.success(request, f"Account has been successfully created. Username: {username}, Email: {email}")

            return redirect('/user/login')
    return render(request,"signup.html")

def blogger_login(request):
    if not request.user.is_authenticated:      
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['psw']

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(request, "Unknown email. Please provide correct email.")
                return redirect('/user/login')
               
            if user.check_password(password):
                login(request, user)
                user = request.user
                return redirect('/user/profile')

            else:
                messages.error(request, "Incorrect password!")
                return redirect('/user/login')

    return render(request, 'login.html')


def blogger_profile(request):
    if request.user.is_authenticated:
        user = request.user
        blogger = Blogger.objects.filter(user=user).first()
        data = {
            'user': user,
            'blogger': blogger
        }
        return render(request, 'blogger_profile.html', data)
    else:
        print("user not authenticated.")
        return redirect('/user/login')
    
def profile_update(request):
    data = {}
    if request.user.is_authenticated:      
        if request.method == 'POST':
            fname = request.POST['fname']
            lname = request.POST['lname']
            bio = request.POST['bio']

            if Blogger.objects.filter(user_id= request.user.id):
                blogger = Blogger.objects.get(user_id= request.user.id)
            else:
                blogger = Blogger(user_id = request.user.id)

            user = request.user
            user.first_name = fname
            user.last_name = lname
            blogger.bio = bio
            blogger.save()
            user.save()
            print("Saved!")
            return redirect('/user/profile')
        else:
            blogger = None
            user = User.objects.get(id=request.user.id)
            print(user)

            if Blogger.objects.filter(user= request.user.pk):
                blogger = Blogger.objects.get(user= request.user)
            else:
                blogger = Blogger()
                print("not found")

            data = {
                'name': user.first_name + ' ' + user.last_name,
                'fname': user.first_name,
                'lname': user.last_name,
                'bio' : blogger.bio,
            }
    
    return render(request, "blogger_profile_update.html", data)

def blogger_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "You have been logged out successfully.")
    return render(request, 'logout.html')

    
def update_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            current_password = request.POST['current_psw']
            password1 = request.POST['psw']
            password2 = request.POST['psw-repeat']
            
            # Check if the current password is correct
            user = authenticate(username=request.user.username, password=current_password)
            if user is None:
                messages.error(request, "Current password is incorrect")
                return render(request, 'update_password.html')

            try:
                resetuser = request.user
                print(resetuser)
       
            except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                resetuser = None
            if resetuser is not None:
                if password1 != password2:
                    messages.error(request,"Password didn't match!")
                    return  render(request, 'update_password.html')
                resetuser.set_password(password1)
                resetuser.save()
                login(request, resetuser)
                messages.success(request,'Your password has been successfully updated')
                return redirect('/user/profile')
            else:
                messages.error(request,"User not authenticated!")
                print("User not authenticated!")
        return render(request,'update_password.html')
