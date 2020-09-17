from django import forms


class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=100)
    user_mail = forms.CharField(max_length=100)
