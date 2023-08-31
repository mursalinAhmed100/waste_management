# from django import forms
# from django.contrib.auth.forms import UserCreationForm


# class CustomerRegistrationForm(UserCreationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'autofocus' : 'True', 'class' : 'form-control'}))
#     email = forms.CharField(widget=forms.EmailInput(attrs={'class' : 'form-control'}))
#     password1 = forms.CharField(lebel='Password', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
#     password2 = forms.CharField(lebel='Confirm Password', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user