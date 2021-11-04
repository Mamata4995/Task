from django import forms
from user.models import Post, User


class UserForm(forms.ModelForm):

    class Meta():
        model = User
        fields = ('first_name', 'last_name','email','password', 'username')

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'textinputclass'}),
            'last_name': forms.TextInput(attrs={'class':'textinputclass'}),
        }

class  PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('user', 'text')

        widgets = {
            'user': forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})

        }
