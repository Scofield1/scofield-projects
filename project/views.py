from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import ContactForm, CreateUserForm
from django.contrib.auth.models import User
from .models import Contact


def index(request):
    return render(request, 'index.html', {})

def list(request):
    contact = Contact.objects.all()
    context = {
        'contacts': contact
    }
    return render(request,'list.html', context)

def create(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        print(form)
        messages.success(request, 'Contact Saved Successfully')
        return redirect('create')
    context = {
        'form': form,
    }
    return render(request, 'create.html', {'form': form})

def delete(request, id):
    contacts = Contact.objects.filter(id=id)
    if request.method == 'POST':
        contacts.delete()
        return redirect('list')
    context = {
        "contacts": contacts
    }
    return render(request, 'delete.html', {'contacts':contacts})

def update(request, id):
    contacts = Contact.objects.filter(id=id)
    form = ContactForm(request.POST or None, instance=contacts)
    if form.is_valid():
        form.save()
        return redirect('list')
    context = {
        'form': form,
        "contacts": contacts
    }
    return render(request, 'update.html', context)

def register(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or Password is Incorrect')
            return redirect('login')
    return render(request, 'login.html', )

def log_out(request):
    logout(request)
    return redirect('login')
