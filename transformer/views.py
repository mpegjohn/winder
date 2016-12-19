from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import NameForm, TransformerForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'transformer/name.html', {'form': form})


def transformer_data(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TransformerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            primary_voltage = form.cleaned_data['primary_voltage']
            s1_voltage = form.cleaned_data['s1_voltage']
	    s1_current = form.cleaned_data['s1_current']


            # Current densityu A/(mm^2)
            CURRENT_DENSITY = 3

	    windings{'primary':'voltage'} = form.cleaned_data['primary_voltage']

	     






            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TransformerForm()

    return render(request, 'transformer/input_data.html', {'form': form})
