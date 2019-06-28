from django import forms
from . import models

class CustomerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = models.Customer
        #fields = ('name', 'email', 'password', 'instrument_purchase', 'house_no', 'address_line1', 'address_line2', 'telephone', 'zip_code', 'state', 'country')
        fields = ('telephone', 'password')
'''
from django import forms
from . import models

class ProfileForm(forms.ModelForm):
	class Meta():
		model = models.Profile
		exclude = ['avatar', 'surname', 'displayedName', 'email']
'''