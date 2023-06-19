from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    CHOICES = [
        ('1', 'Ish beruvchi'),
        ('2', 'Xodim'),
    ]
    user_types = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES, 
    )
    
    full_name = forms.CharField(max_length=150, widget= forms.TextInput(attrs={'placeholder':'Ism va familiya'}))
    username = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Parol'}))

    class Meta:
        model = User
        fields = ['username', 'full_name',  'password', 'user_types']
        
class UserLoginForm(forms.ModelForm):
    username = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Parol'}))

    class Meta:
        model = User
        fields = ['username', 'password']
