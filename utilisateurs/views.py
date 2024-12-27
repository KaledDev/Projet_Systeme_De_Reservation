from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Crée un utilisateur à partir du formulaire
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()  # Sauvegarde dans la base de données PostgreSQL
            login(request, user)  # Connecte automatiquement l'utilisateur
            return redirect('connexion')  # Redirige après l'inscription
    else:
        form = UserRegistrationForm()
    return render(request, 'utilisateurs/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Authentification de l'utilisateur
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirige vers la page d'accueil après connexion
            else:
                form.add_error(None, 'Identifiants incorrects')
    else:
        form = LoginForm()

    return render(request, 'utilisateurs/login.html', {'form': form})