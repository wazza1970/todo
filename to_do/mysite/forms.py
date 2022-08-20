from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ToDo

class RegistionForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = {
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'
        }

    def save(self, commit=True):
        user = super(RegistionForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class ToDoForm(forms.ModelForm):
    
    class Meta:
        model = ToDo
        fields = {
            
            'todo'
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = {
            'todo',
            'created',
        }
completed = (
    (True, True),
    (False, False)
   
)
class completedForm(forms.ModelForm):
    completed = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=completed)
    class Meta:
        model = ToDo
        fields = {
            
            'todo',
            'completed'
        }