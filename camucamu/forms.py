from django import forms
from apps.books.models import Book
from django.forms import ModelForm


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='E-Mail')
    message = forms.CharField(widget=forms.Textarea, label='We\'re listening!')

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Too few words!")
        return message


class BookForm(ModelForm):
    class Meta:
        model = Book
        exclude = ('user',)
