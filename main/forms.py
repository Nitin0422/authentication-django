from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    # Defining a new field for the form that extends the UserCreationForm
    email_address = forms.CharField(max_length=200, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    #Overriding the default save method of the UserCreationForm 
    def save(self, commit = True):
        #Creates a proxy object of the super class representing the instance of child class and calls the save method of the parent class.
        user = super(RegistrationForm, self).save(commit=False)
        #Sets the attrubute of email of the user class to email_addrress. 
        user.email = self.cleaned_data['email_address']
        if commit:
            user.save()
        return user


