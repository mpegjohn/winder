from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import NameForm, TransformerForm
from reactor.models import Wire


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


            import pdb; pdb.set_trace()

            primary_voltage = form.cleaned_data['primary_voltage']
            s1_voltage = form.cleaned_data['s1_voltage']
	    s1_current = form.cleaned_data['s1_current']


            # Current densityu A/(mm^2)
            CURRENT_DENSITY = 3
	    windings = {}
            windings['primary'] = {}

	    windings['primary']['voltage'] = form.cleaned_data['primary_voltage']

            windings['secondary'] = {}
	    windings['secondary'][1] = {}
            windings['secondary'][1]['voltage'] = form.cleaned_data['s1_voltage']
            windings['secondary'][1]['current'] = form.cleaned_data['s1_current']

            calc_area = form.cleaned_data['s1_current']/CURRENT_DENSITY

            # get the first wire that has this area or greater.
            Wire.objects.filter(area__gte = calc_area)[:1]
           

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TransformerForm()

    return render(request, 'transformer/input_data.html', {'form': form})
