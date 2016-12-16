
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class TransformerForm(forms.Form):
	primary_voltage = forms.FloatField(label='primary voltage', required=True)
	s1_voltage = forms.FloatField(label='S1 voltage', required=True)
	s1_current = forms.FloatField(label='S1 current', required=False)
	s2_enabled = forms.BooleanField(label='S2 enabled', initial=False, required=False)
	s2_voltage = forms.FloatField(label='S2 voltage', required=False, disabled=True)
	s2_current = forms.FloatField(label='S2 current', required=False)
	s3_enabled = forms.BooleanField(label='S3 enabled', initial=False, required=False)
	s3_voltage = forms.FloatField(label='S3 voltage', required=False)
	s3_current = forms.FloatField(label='S3 current', required=False)
	s4_enabled = forms.BooleanField(label='S4 enabled', initial=False, required=False)
	s4_voltage = forms.FloatField(label='S4 voltage', required=False)
	s4_current = forms.FloatField(label='S4 current', required=False)
	





