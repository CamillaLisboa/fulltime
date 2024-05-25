from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Person, Bill
from .forms import PersonForm, BillForm


class Index(ListView):
    model=Person
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['finance_data'] = self.get_finance_data()
        return context

    def get_finance_data(self):
        # Obtém as todas as pessoas
        people = Person.objects.all()
        finance_data = []

        total_income = 0
        total_people = 0
        for person in people:
            total_income+= person.income
            total_people+=1

        total_bills = 0

        bills = Bill.objects.all()
        for bill in bills:
            total_bills+= bill.price
        net_income = total_income - total_bills

        finance_data.append({
            'total_income': round(total_income, 2),
            'total_people': total_people,
            'total_bill': total_bills,
            'net_income': round(net_income, 2),
                             })

        return finance_data
    

class PersonList(ListView):
    model = Person
    template_name = 'person.html'

    
class PersonCreate(CreateView):
    model = Person
    template_name = 'person_create.html'
    success_url = reverse_lazy('finance:person')
    form_class = PersonForm

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super(PersonCreate, self).get_form_kwargs()
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PersonUpdate(UpdateView):
    model = Person
    template_name = 'person_update.html'
    fields = ['name', 'doc', 'income']
    success_url = reverse_lazy('finance:person')


class PersonDelete(DeleteView):
    model = Person
    template_name = 'person_delete.html'
    
    def get_success_url(self):
        return reverse_lazy("finance:person")
    

class BillList(ListView):
    model = Bill
    template_name = 'bill.html'


class BillCreate(CreateView):
    model = Bill
    template_name = 'bill_create.html'
    success_url = reverse_lazy('finance:bill')
    form_class = BillForm

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super(BillCreate, self).get_form_kwargs()
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context  


class BillUpdate(UpdateView):
    model = Bill
    template_name = 'bill_update.html'
    fields = ['name', 'price', 'due_date']
    success_url = reverse_lazy('finance:bill')


class BillDelete(DeleteView):
    model = Bill
    template_name = 'bill_delete.html'
    
    def get_success_url(self):
        return reverse_lazy("finance:bill")

