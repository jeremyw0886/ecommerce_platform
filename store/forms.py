from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserProfile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        help_text='Required. Enter your first name.',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        help_text='Required. Enter your last name.',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        help_text='Required. Provide a valid email address.',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    street_address = forms.CharField(
        max_length=255,
        required=True,
        help_text='Required. Enter your street address.',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    state = forms.CharField(
        max_length=50,
        required=True,
        help_text='Required. Enter your state.',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    zip_code = forms.CharField(
        max_length=10,
        required=True,
        help_text='Required. Enter your zip code.',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email',
            'street_address', 'state', 'zip_code', 'password1', 'password2'
        )
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Update widget attributes for fields inherited from the parent form
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        # Optionally, update username as well
        self.fields['username'].widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name  = self.cleaned_data['last_name']
        user.email      = self.cleaned_data['email']
        if commit:
            user.save()
            # Ensure that a UserProfile exists for this user
            profile, created = UserProfile.objects.get_or_create(user=user)
            profile.street_address = self.cleaned_data['street_address']
            profile.state = self.cleaned_data['state']
            profile.zip_code = self.cleaned_data['zip_code']
            profile.save()
        return user


class UserProfileForm(forms.ModelForm):
    """
    Form for logged-in users to update their profile information.
    """
    class Meta:
        model = UserProfile
        fields = ['street_address', 'state', 'zip_code']
        widgets = {
            'street_address': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
        }


class BillingAddressForm(forms.Form):
    street_address = forms.CharField(
        max_length=255, 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    state = forms.CharField(
        max_length=50, 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    zip_code = forms.CharField(
        max_length=10, 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    same_as_mailing = forms.BooleanField(
        required=False, 
        label="Same as mailing address"
    )
