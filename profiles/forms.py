from django import forms

from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    birthday = forms.DateField(
        widget=forms.DateInput(attrs={
            'placeholder': 'Format: mm/dd/YYYY'
        }),
        input_formats=['%m/%d/%Y'],
        error_messages={'invalid': 'Be sure to use the correct format (mm/dd/YYYY).'}
    )

    class Meta:
        model = UserProfile
        fields = ('profile_picture', 'birthday', 'gender')
