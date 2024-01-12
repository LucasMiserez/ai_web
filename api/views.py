from django.shortcuts import render
from .form import InputForm
import requests


def index(request):
    no_value = False
    submitted_value = None
    your_input_value = None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid() and form.cleaned_data['formInput'] != "":
            your_input_value = form.cleaned_data['formInput']
            api_url = f'https://lucasmiserez.pythonanywhere.com/?comment={your_input_value}'

            try:
                response = requests.get(api_url)
                response.raise_for_status()
                submitted_value = response.json()[0].get('label', 'API call unsuccessful')
            except requests.exceptions.RequestException as e:
                submitted_value = f'API call failed: {e}'

            print(f'Input Value: {submitted_value}')
        else:
            no_value = True
    else:
        form = InputForm()
    return render(request, "home.html", {'form': form, 'submitted_value': submitted_value, "no_value": no_value, "your_input_value": your_input_value})
