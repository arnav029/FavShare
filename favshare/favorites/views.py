# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import FavoriteItem
from .forms import FavoriteItemForm


# views.py
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save user first
            login(request, user)  # Directly login after save
            user = form.save()
            print(f"User created: {user.username}")  # Debug output
            print(f"Password valid: {user.check_password(form.cleaned_data['password1'])}")
            return redirect('favorites_list')
        else:
            # Add error logging
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('favorites_list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def favorites_list(request):
    items = FavoriteItem.objects.filter(user=request.user)
    return render(request, 'favorites/list.html', {'items': items})

@login_required
def add_favorite(request):
    if request.method == 'POST':
        form = FavoriteItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('favorites_list')
    else:
        form = FavoriteItemForm()
    return render(request, 'favorites/add.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')
