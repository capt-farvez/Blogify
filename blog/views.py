from django.shortcuts import render, redirect
from .models import Blogger, Blog
from django.contrib import messages


def create_blog(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            title = request.POST['title']
            abstract = request.POST['abstract']
            date = request.POST['date']
            user = request.user
            blogger = Blogger.objects.filter(user=user).first()

            blog =  Blog(title=title, abstract=abstract, date=date)
            blog.save()
            blog.blogger.add(blogger)
            blog.save()
            return (redirect, "/user/profile")
        return render(request, "create_blog.html")

    else:
        print("user not authenticated.")
        return redirect('/user/login')   

def update_blog(request, id):
    blog = Blog.objects.get(id=id)
    if request.user.is_authenticated:
        user = request.user
        blogger = Blogger.objects.filter(user=user).first()
        if blog.blogger == blogger:
            if request.method == 'POST':
                title = request.POST['title']
                abstract = request.POST['abstract']

                blog.title = title
                blog.abstract = abstract
                blog.save()
        
        else:
            print("unathorised Login")
            messages.error(request, "Unathorisez, Access Denied!")
            return redirect('/user/profile')
        
        data = {
            "title": blog.title,
            "abstract": blog.abstract,
        }
        return render(request, "update_blog.html", data)
    else:
        messages.error(request, "Unauthorised, Login First")
        return redirect('/user/login')
    

def delete_blog(request, id):
    blog = Blog.objects.get(id=id)
    if request.user.is_authenticated:
        user = request.user
        blogger = Blogger.objects.filter(user=user).first()
        if blog.blogger == blogger:
            blog.delete()
        else:
            print("unathorised Login")
            messages.error(request, "Unathorisez, Access Denied!")
            return redirect('/user/profile')
        
        data = {
            "id": id,
            "title": blog.title,
            "abstract": blog.abstract,
        }
        return render(request, "delete_blog.html", data)
    else:
        messages.error(request, "Unauthorised, Login First")
        return redirect('/user/login')


    
def blog_list(request):
    if request.user.is_authenticated:
        return render(request, "blog_list.html")
    else:
        return redirect("/user/login")