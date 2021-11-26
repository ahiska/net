from django import forms
from contact.models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(label = 'name', widget=forms.TextInput(attrs={'placeholder': 'Ad Soyad'}))
    email = forms.EmailField(label = 'email', widget=forms.EmailInput(attrs={'placeholder': 'E-Posta'}))
    phone = forms.IntegerField(label = 'phone', widget=forms.NumberInput(attrs={'placeholder': 'Telefon'}))
    subject = forms.CharField(label = 'subject', widget=forms.TextInput(attrs={'placeholder': 'Konu'}))
    message = forms.CharField(label = 'message', widget=forms.TextInput(attrs={'placeholder': 'Mesaj'}))

    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'subject', 'message')