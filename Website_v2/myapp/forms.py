from django import forms
from .models import Input, STATES

options = ['Homocide', 'Caught Selling Drugs', 'Caught Selling Only Marijuana']

class InputForm(forms.ModelForm):

    attrs = {'class ' : 'form−control ',
             'onchange ' : 'this.form.submit() '}

    state = forms.ChoiceField(choices=STATES, required=True,
                              widget=forms.Select(attrs = attrs))
    class Meta:

        model = Input
        fields = ['state']
class inputfromuser(forms.Form):
    '''
    RecommendationForm to capture the user info entered on the Recommendation
    Tool
    '''
    user_input = forms.ChoiceField\
    ( label = 'Choose a graph to display',\
    choices = [ ( x, x ) for x in options ], required = False )
