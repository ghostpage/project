from django.forms import ModelForm, widgets
from django import forms
from secureweb.models import Web

class FormWeb(ModelForm):
    class Meta:
        model = Web
        fields = '__all__'

        widgets = {
            'nama' : forms.TextInput({'class':'form-control'}),
            'ling' : forms.TextInput({'class':'form-control'}),
            'tipe' : forms.TextInput({'class':'form-control'}),
            'pembuat' : forms.TextInput({'class':'form-control'}),
            'pemilik' : forms.TextInput({'class':'form-control'}),
            'kolom' : forms.NumberInput({'class':'form-control'}),
            'kelompok_id' : forms.Select({'class':'form-control'}),
        }