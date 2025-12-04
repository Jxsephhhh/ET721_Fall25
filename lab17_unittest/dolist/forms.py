from django import forms

class Todolistform(forms.Form):
    text = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'todo_text',
                'placeholder': 'Enter to do...',
                'aria-label': 'Todo',
                'aria-describeby': 'add-btn'
            }
        )
    )
