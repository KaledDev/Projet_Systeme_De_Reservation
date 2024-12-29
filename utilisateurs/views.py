from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomAuthenticationForm, UserRegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Crée un utilisateur à partir du formulaire
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()  # Sauvegarde dans la base de données PostgreSQL
            login(request, user)  # Connecte automatiquement l'utilisateur
            return redirect('login')  # Redirige après l'inscription
    else:
        form = UserRegistrationForm()
    return render(request, 'utilisateurs/register.html', {'form': form})


def login_view(request):
    form = CustomAuthenticationForm()
    error_message = None  # Initialisation du message d'erreur
    
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Vérifier si l'utilisateur est un super utilisateur
            if user.is_superuser:
                return redirect('admin_dashboard')  # Rediriger vers le tableau de bord admin
            else:
                return redirect('home')  # Rediriger vers la page d'accueil

        else:
            # Personnalisation du message d'erreur
            error_message = (
                "Adresse email ou mot de passe incorrect. "
                "Veuillez vérifier vos identifiants et réessayer."
            )
    
    return render(request, 'utilisateurs/login.html', {'form': form, 'error_message': error_message})

def logout_view(request):
    logout(request)  # Déconnecte l'utilisateur
    return redirect('login') 

@login_required  # Assure que seul un utilisateur connecté peut accéder à la page
def home(request):
    return render(request, 'utilisateurs/home.html')