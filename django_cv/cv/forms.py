from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    person = forms.CharField(max_length=250)
    email = forms.EmailField(max_length=250)
    message = forms.CharField()

    class Meta:
        model = Feedback()
        fields = ('person', 'email', 'message')
