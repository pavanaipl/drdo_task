from django import forms

class DashboardForm(forms.Form):
    fdate = forms.DateField(label='fdate')
    tdate = forms.DateField(label='tdate')