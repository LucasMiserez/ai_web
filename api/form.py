from django import forms


class InputForm(forms.Form):
    formInput = forms.CharField(label='Your input text')
