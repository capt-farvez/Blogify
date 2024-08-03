from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from blogger.models import Blogger
from blog.models import Blog
from .models import Qna

def welcome_page(request):
    blogs = Blog.objects.all()
    data ={
        'blogs' : blogs
    }
    return render(request, 'welcome.html', data)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def privacy(request):
    return render(request, 'privacyPolicy.html')

def qna(request):
    qnas = Qna.objects.all()
    data ={
        'qnas' : qnas
    }
    return render(request, 'qna.html', data)

def addqna(request):
    if request.method == "POST":
        question = request.POST['question']
        answer = request.POST['answer']
        
        newqna = Qna(question=question, answer=answer)
        newqna.save()
        messages.success(request, f"QnA has been successfully Added. Question: {question}, Email: {answer}")

        return redirect('/QnA')
    return render(request, 'addQnA.html')

def terms(request):
    return render(request, 'termsAndConditions.html')
