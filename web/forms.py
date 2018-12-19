from django import forms
from datetimepicker.widgets import DateTimePicker


class DateForm(forms.Form):
    start = forms.DateField(label="From ",widget=forms.TextInput(attrs=
                                {
                                    'class':'datepicker',
                                    'style': 'width:200px; height:30px;'
                                }))
                               
    end = forms.DateField(label="To ",widget=forms.TextInput(attrs=
                                {
                                    'class':'datepicker',
                                    'style': 'width:200px; height:30px;'
                                }))