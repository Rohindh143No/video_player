from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import RegistrationForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Create a new user profile
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            profile = UserProfile(username=user.username, password=user.password, email=form.cleaned_data['email'])
            profile.save()
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})
