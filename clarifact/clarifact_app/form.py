from django import forms
import datetime


class source_form(forms.Form):
    source = forms.CharField(label='',
                                max_length=100, 
                                widget=forms.TextInput(attrs={'class' : 'input-form','placeholder': 'Enter the Source full name...'}))

class author_form(forms.Form):
    author = forms.CharField(label='',
                                max_length=100, 
                                widget=forms.TextInput(attrs={'class' : 'input-form','placeholder': 'Search Author...'}))



class fake_news_form(forms.Form):
    
    news_title = forms.CharField(label='',
                                 widget=forms.TextInput(attrs={'placeholder':'Enter the News Title...',
                                                              'class':'input-form required',
                                                              'id':'f_name'}),
                                                              required=True)
    news_text = forms.CharField(label='', 
                                widget=forms.Textarea(attrs={'placeholder': 'Enter the News Body...',
                                                            'class':'input-form required',
                                                            'id':'con_message'}),
                                                            required=True)
    news_author = forms.CharField(label='',
                                 widget=forms.TextInput(attrs={'placeholder':'Enter the Author Name...',
                                                              'class':'input-form',
                                                              'id':'author'}),
                                                              required=False)
    source = forms.CharField(label='',
                                max_length=100, 
                                widget=forms.TextInput(attrs={'class' : 'input-form',
                                'placeholder': 'Source URL(https://www.focusnews.com.ng/)'}),
                                required=False)

    CHOICES = [('Positive','Positive'),('Negative','Negative'),]
    news_bias= forms.CharField(label="What's your view concerning this subject?", widget=forms.RadioSelect(choices=CHOICES, attrs={
        'class':'radio_button'
    }))
    


                               


# <input class="input-form required" type="text" name="f_name" id="f_name" placeholder="News Title" required>

                            