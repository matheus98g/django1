from django import forms
from .models import Posts
from .models import Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'rounded-lg border border-gray-300 p-2', 'placeholder': 'Título'}),
            'body': forms.Textarea(attrs={'class': 'rounded-lg border border-gray-300 p-2', 'placeholder': 'Conteúdo'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'class': 'w-full p-2 border rounded', 'placeholder': 'Escreva aqui...'}),
        }
