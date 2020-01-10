from django import forms
# from models import Customer

# class DealerAddCustForm(forms.ModelForm):
#     cust_email = forms.CharField()
#     cust_address = forms.CharField()
#     fname = forms.CharField()
#     lname = forms.CharField()
#     phone = forms.CharField()
#     notes = forms.CharField()
#     vin = forms.CharField()

#     class Meta:
#         model = Customer
#         fields = ('cust_email', 'cust_address', 'fname', 'lname', 'phone', 'notes', 'vin')

class DealerAddCustForm(forms.Form):
    cust_email = forms.CharField()
    cust_address = forms.CharField()
    fname = forms.CharField()
    lname = forms.CharField()
    phone = forms.CharField()
    notes = forms.CharField()
    vin = forms.CharField()