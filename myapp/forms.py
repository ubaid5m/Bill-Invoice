# from django import forms
# from .models import Invoice

# class InvoiceForm(forms.ModelForm):
#     class Meta:
#         model = Invoice
#         fields = ["customer_name","invoice_number","amount","is_paid"]
        
    
    
    
    
    
    
    
from django import forms
from .models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ["customer_name","invoice_number","amount","is_paid","notes",]

    widgets = {
        "customer_name": forms.TextInput(attrs={
            "placeholder": "Enter customer name"
        }),
        "invoice_number": forms.TextInput(attrs={
            "placeholder": "e.g. INV-001"
        }),
        "amount": forms.NumberInput(attrs={
            "placeholder": "Enter amount",
            "min": "0",
            "step": "0.01"
        }),
        "is_paid": forms.CheckboxInput(),
        "notes": forms.Textarea(attrs={
            "placeholder": "Additional invoice notes",
            "rows": 4
        }),
    }
    def clean_amount(self):
        amount = self.cleaned_data.get("amount")
        if amount <= 0:
            raise forms.ValidationError("Amount must be greater than zero.")
        return amount
    
