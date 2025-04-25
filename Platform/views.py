from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Home Page View
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

# Learn Page View
class LearnView(View):
    def get(self, request):
        return render(request, 'learn.html')

# Register View
class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})  # Ensure the correct template path

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user but don't log them in
            return redirect('login')  # Redirect to login page after registration
        return render(request, 'register.html', {'form': form})

# Login View using Django's built-in LoginView
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Ensure the correct template path
    def get_success_url(self):
        return reverse_lazy('learn')  # Redirect to learn page after successful login

# Logout View
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('index')  # Redirect to the index page
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)