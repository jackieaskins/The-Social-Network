from django import forms

from .models import StatusPost, StatusComment


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


class StatusCommentForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': "Did you want to add something?",
            'rows': 2,
            'style': 'resize:none'
        }),
        error_messages={'required': "Did you change your mind? You didn't type anything..."}
    )

    def __init__(self, *args, **kwargs):
        super(StatusCommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].label = False

    class Meta:
        model = StatusComment
        fields = ('text',)
