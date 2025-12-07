from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment, Post,Tag


class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text='Enter tags separated by commas (e.g., python, django, web)',
        widget=forms.TextInput(attrs={'placeholder': 'python, django, web'})
    )
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Populate tags field with existing tags
            self.fields['tags'].initial = ', '.join([tag.name for tag in self.instance.tags.all()])
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        
        # Handle tags
        if 'tags' in self.cleaned_data:
            instance.tags.clear()
            tag_names = [name.strip() for name in self.cleaned_data['tags'].split(',') if name.strip()]
            for tag_name in tag_names:
                tag, created = Tag.objects.get_or_create(name=tag_name.lower())
                instance.tags.add(tag)
        
        return instance

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment here...'})
        }
        labels = {
            'content': 'Comment'
        }
