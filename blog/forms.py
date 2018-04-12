from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    class Meta:
        model=User
        help_texts = {
            'username': None,
        }
        fields=('username','email','password')

class PostForm(forms.ModelForm):
    # author=forms.ModelChoiceField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    # 'title'=forms.TextInput(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    class Meta:
        model = Post
        fields = ('author','title', 'text',)

        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'textinputclass form-control','placeholder':'Add Title'}),
        #     'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent form-control','placeholder':'Add Post'}),
        # }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author','text',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
