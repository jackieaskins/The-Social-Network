from django import forms

from .models import StatusPost


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
