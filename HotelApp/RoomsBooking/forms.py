from django import forms # type: ignore # type: ignore
from django.forms import ModelForm # type: ignore
from .models import Room , UserRegistration



class UserBookingForm(forms.ModelForm):
    startdate = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    enddate = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = UserRegistration
        fields = ['startdate','enddate']
        widgets = {
            'my_des': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),

        }

    def clean(self ,startdate,enddate):
        cleaned_data = super().clean()
        startdate = cleaned_data.get('start_date')
        enddate = cleaned_data.get('end_date')

        if enddate and startdate and enddate <= startdate:
            self.add_error('end_date', 'End date must be greater than start date.')    
        
    def __init__(self, *args, **kwargs):
        super(UserBookingForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'          


