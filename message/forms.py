from django import forms
from registration.models import Profile


class SendMessageForm(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                        'placeholder': 'message title here'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                                        'placeholder': 'type message here'}))
    recipient = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[])

    def __init__(self, *args, **kwargs):
        super(SendMessageForm, self).__init__(*args, **kwargs)
        self.fields['recipient'].choices = [(x.pk, x.get_full_name()) for x in Profile.objects.all()]

