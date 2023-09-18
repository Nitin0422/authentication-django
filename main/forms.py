from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    # Defining a new field for the form that extends the UserCreationForm
    phone_number = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ("username", "phone_number", "password1", "password2")

    #Overriding the default save method of the UserCreationForm 
    def save(self, commit = True):
        #Creates a proxy object of the super class representing the instance of child class and calls the save method of the parent class.
        user = super(RegistrationForm, self).save(commit=False)
        #Sets the attrubute of email of the user class to email_addrress. 
        user.phone_number = self.cleaned_data['phone_number']
        if commit:
            user.save()
        return user


