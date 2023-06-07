from django import forms
from .models import *


class LaptopModelForm(forms.ModelForm):
    class Meta:
        model = LaptopModel
        fields = '__all__'
    def clean_modelprice(self):
        price = self.cleaned_data['modelprice']
        if price<=100000:
            return price
        else:
            raise forms.ValidationError('modelprice should be less than 100000')
    def clean_modelname(self):
        name = self.cleaned_data['modelname']
        if name == 'lenovo':
            return name
        else:
            raise forms.ValidationError('model should be of lenovo only')



class MobileModelForm(forms.ModelForm):
    class Meta:
        model = MobileModel
        fields = '__all__'

class TVModelForm(forms.ModelForm):
    class Meta:
        model = TVModel
        fields = '__all__'