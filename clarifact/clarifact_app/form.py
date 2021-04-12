from django import forms

class author_form(forms.Form):
    author = forms.CharField(label='',
                                max_length=100, 
                                widget=forms.TextInput(attrs={'class' : 'searchTerm','placeholder': 'Search Author...'}))