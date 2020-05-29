from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'diary/home.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('First Name')
            messages.success(request, f'The account is created for { first_name }')
            return redirect('home')

    else:
        form = RegisterForm()
    return render(request, 'diary/register.html', {'form': form})


def introduction(request):
    return render(request, 'diary/introduction.html')

def login(request):
    return render(request, 'diary/login.html')

def editor(request):
    return render(request, 'diary/editor.html')
