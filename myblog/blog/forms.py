# blog/forms.py
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Напишите ваш комментарий здесь...',
                'style': 'resize: vertical; min-height: 100px;'
            })
        }
        labels = {
            'text': 'Комментарий'
        }
        help_texts = {
            'text': 'Максимум 1000 символов'
        }
    
    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) > 1000:
            raise forms.ValidationError('Комментарий не должен превышать 1000 символов.')
        return text