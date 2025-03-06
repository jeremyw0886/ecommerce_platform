from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your first name.')
    last_name  = forms.CharField(max_length=30, required=True, help_text='Required. Enter your last name.')
    email      = forms.EmailField(max_length=254, required=True, help_text='Required. Provide a valid email address.')
    street_address = forms.CharField(max_length=255, required=True, help_text='Required. Enter your street address.')
    state          = forms.CharField(max_length=50, required=True, help_text='Required. Enter your state.')
    zip_code       = forms.CharField(max_length=10, required=True, help_text='Required. Enter your zip code.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 
                  'street_address', 'state', 'zip_code', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name  = self.cleaned_data['last_name']
        user.email      = self.cleaned_data['email']
        if commit:
            user.save()
            # Save address data to the UserProfile
            user.userprofile.street_address = self.cleaned_data['street_address']
            user.userprofile.state = self.cleaned_data['state']
            user.userprofile.zip_code = self.cleaned_data['zip_code']
            user.userprofile.save()
        return user

class BillingAddressForm(forms.Form):
    street_address = forms.CharField(max_length=255, required=True)
    state = forms.CharField(max_length=50, required=True)
    zip_code = forms.CharField(max_length=10, required=True)
    same_as_mailing = forms.BooleanField(required=False, label="Same as mailing address")
