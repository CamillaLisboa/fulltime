import django.forms as forms
from .models import Person, Bill


class PersonForm(forms.ModelForm):
    
    class Meta:
        model = Person
        fields = ['name', 'doc', 'income']

class BillForm(forms.ModelForm):
    
    class Meta:
        model = Bill
        fields = ['name', 'price', 'due_date']