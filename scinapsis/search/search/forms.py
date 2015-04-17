from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def login_action(self):
        login = self.cleaned_data['username']
        passw = self.cleaned_data['password']

