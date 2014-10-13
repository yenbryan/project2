from django import forms
from discussion.models import Category


class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                        'placeholder': 'type message here'}))


class DiscussionForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'type title here'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder': 'type discussion here'}))
    category = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[], required=False)
    category_input = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'type category here'}), required=False)

    def __init__(self, *args, **kwargs):
        super(DiscussionForm, self).__init__(*args, **kwargs)
        self.fields['category'].choices = [(x.pk, x.get_full_name()) for x in Category.objects.all()]

