from django import forms

from .models import StatusPost, UserProfile


class StatusPostForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': "Tell us what's happening!",
            'id': 'new_post',
            'rows': 5,
            'style': 'resize:none'
        }),
        error_messages={'required': "Hey there! I don't think you typed anything..."}
    )

    def __init__(self, *args, **kwargs):
        super(StatusPostForm, self).__init__(*args, **kwargs)
        self.fields['text'].label = False

    class Meta:
        model = StatusPost
        fields = ('text',)


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
