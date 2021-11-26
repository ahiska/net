from django import forms
from blog.models import Comment


class CommentForm(forms.ModelForm):
    name = forms.CharField(label='name', widget=forms.TextInput(attrs={'placeholder': 'Ad Soyad'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'placeholder': 'E-Posta'}))
    body = forms.CharField(label='body', widget=forms.TextInput(attrs={'placeholder': 'Yorum'}))

    class Meta:
        model = Comment
        # fields = '__all__'
        fields = ('name', 'email', 'body')
