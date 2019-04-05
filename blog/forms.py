from django import forms
from . import models


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['content']
        widgets = {
            'content':forms.Textarea(attrs={'rows':4,'resize':'none'})
        }
        labels = {
            'content':'متن'
        }
        help_texts = {
            'content' : 'متن خود را وارد کنید'
        }
