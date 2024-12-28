from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirmer le mot de passe")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
        'username': 'Nom d\'utilisateur',
        'email': 'Adresse email',
        }
        # Suppression ou personnalisation des messages d'aide
        help_texts = {
            'username': None,  # Supprime le texte d'aide pour 'username'
            'email': None,
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")
        return cleaned_data


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nom d\'utilisateur',
            'id': 'username'
        }),
        label="Nom d'utilisateur"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mot de passe',
            'id': 'password'
        }),
        label="Mot de passe"
    )
    error_messages = {
        'invalid_login': (
            "Les informations de connexion ne sont pas valides. "
            "Veuillez vérifier votre nom d'utilisateur et votre mot de passe."
        ),
        'inactive': ("Ce compte est inactif."),
    }