# from django.shortcuts import render
# from django.http import HttpResponse
# from datetime import datetime
# from .models import Invoice



# # Create your views here.

# def home(request):
#     return HttpResponse("Hello, Ubaid!")

# #it is the point where i use create 
# def create_invoice(request):
#     Invoice.objects.create(
#         customer_name = "Malik ubaid",
#         invoice_number = "INV001",
#         amount = 1500000.00,
#         date_created = datetime.now(),
#         is_paid = False,
#         notes = "Good person",
#     )
#     return render(request, "D:/django/invoices/templates/invoices/invoice.html", {})

# #their i am making function for invoice
# #Fetching
# def show_one_invoice(request):
#     invoice = Invoice.objects.get(invoice_number ="INV001" )
#     data = {
#         "invoice":invoice
#     }
#     return render(request, "D:/django/invoices/templates/invoices/invoice.html",{})


# #filter
# def show_unpaid(request):
#     unpaid_invoice = Invoice.objects.filter(is_paid = False)
#     data = {
#         "unpaid_invoice" : unpaid_invoice 
#     }
#     return render(request,"D:/django/invoices/templates/invoices/invoice.html",data)


# #update
# def  mark_as_paid(request):
#     Invoice.objects.filter(invoice_number = "INV001").update(is_paid = True)
#     all_invoices = invoice.objects.filter(is_paid = False)
#     data = {
#         "all_invoices":all_invoices
#     }
#     return render(request,"D:/django/invoices/templates/invoices/invoice.html",data)


# def show_invoices(request):
#     data = {
#         "all_invoices" : [
#             {"number":1,"customer":"ubaid","amount":10000000,"today": datetime.now()},
#             {"number":2,"customer":"uzair","amount":100000,"today": datetime.now()},
#             {"number":3,"customer":"usman","amount":1000000,"today": datetime.now()},
#         ]
#     }
#     return render(request,"D:/django/invoices/templates/invoices/home1.html",data)

# def invoice(request):
#     marks = {
#         "all_marks":[
#             {"student":1,"grade":"A","Name":"Malik Ubaid","Marks":1100,"today":datetime.now()},
#             {"student":2,"grade":"A","Name":"Malik Abdullah","Marks":1050,"today":datetime.now()},
#             {"student":3,"grade":"A","Name":"Malik Imran","Marks":1000,"today":datetime.now()},
#         ]
#     }
#     return render(request, "D:/django/invoices/templates/invoices/invoice.html",marks)









# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.shortcuts import get_object_or_404
# from datetime import datetime
# from .models import Invoice
# from .forms import InvoiceForm
# from django.views.generic import CreateView 



# def add_invoice(request):
#     if request.method == "POST":
#         form = InvoiceForm(request.POST)
#         if form.is_valid():
#             return redirect("all_invoices")
#     else:
#         form = InvoiceForm()
#     data = {
#         "form":form
#     }
#     return render(request,"D:/django/invoices/templates/invoices/add_invoice.html",data)



# # Home page
# def home(request):
#     return HttpResponse("Hello, Ubaid!")

# # Create invoice
# def create_invoice(request):
#     Invoice.objects.get_or_create(
#         invoice_number="INV001",
#         defaults={
#             "customer_name": "Malik ubaid",
#             "amount": 1500000.00,
#             "date_created": datetime.now(),
#             "is_paid": False,
#             "notes": "Good person",
#         }
#     )

#     return render(
#         request,
#         "invoices/invoice.html",
#         {}
#     )

# # Fetch one invoice
# def show_one_invoice(request):
#     invoice = get_object_or_404(
#         Invoice,
#         invoice_number="INV001"
#     )

#     data = {
#         "invoice": invoice
#     }

#     return render(
#         request,
#         "invoices/invoice.html",
#         data
#     )

# # Filter unpaid invoices
# def show_unpaid(request):
#     unpaid_invoice = Invoice.objects.filter(
#         is_paid=False
#     )

#     data = {
#         "unpaid_invoice": unpaid_invoice
#     }

#     return render(
#         request,
#         "invoices/invoice.html",
#         data
#     )

# # Update invoice as paid
# def mark_as_paid(request):
#     Invoice.objects.filter(
#         invoice_number="INV001"
#     ).update(is_paid=True)

#     all_invoices = Invoice.objects.filter(
#         is_paid=False
#     )

#     data = {
#         "all_invoices": all_invoices
#     }

#     return render(
#         request,
#         "invoices/invoice.html",
#         data
#     )

# # Show sample invoices
# def show_invoices(request):
#     data = {
#         "all_invoices": [
#             {
#                 "invoice_number": 1,
#                 "customer_name": "ubaid",
#                 "amount": 10000000,
#                 "today": datetime.now()
#             },
#             {
#                 "invoice_number": 2,
#                 "customer_name": "uzair",
#                 "amount": 100000,
#                 "today": datetime.now()
#             },
#             {
#                 "invoice_number": 3,
#                 "customer_name": "usman",
#                 "amount": 1000000,
#                 "today": datetime.now()
#             },
#         ]
#     }

#     return render(
#         request,
#         "invoices/home1.html",
#         data
#     )

# # Show sample student marks
# def invoice(request):
#     invoicess = {
#         "all_invoices": [
#             {
#                 "invoice_number": 1,
#                 "customer_name": "ubaid",
#                 "amount": 10000000,
#                 "today": datetime.now()
#             },
#             {
#                 "invoice_number": 2,
#                 "customer_name": "uzair",
#                 "amount": 100000,
#                 "today": datetime.now()
#             },
#             {
#                 "invoice_number": 3,
#                 "customer_name": "usman",
#                 "amount": 1000000,
#                 "today": datetime.now()
#             },
#         ]
#     }

#     return render(
#         request,
#         "invoices/invoice.html",
#         invoicess
#     )











from decimal import Decimal

from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Invoice
from .forms import InvoiceForm


def home(request):
    invoices = Invoice.objects.all().order_by("-date_created")


    context = {
        "total_invoices": invoices.count(),
        "paid_count": invoices.filter(is_paid=True).count(),
        "unpaid_count": invoices.filter(is_paid=False).count(),
        "total_revenue": (
            invoices.filter(is_paid=True).aggregate(
                total=Sum("amount")
            )["total"] or Decimal("0.00")
        ),
        "recent_invoices": invoices[:5],
    }

    return render(request, "invoices/home1.html", context)



def invoice(request):
    invoices = Invoice.objects.all().order_by("-date_created")

    
    context = {
        "invoices": invoices[:5],
        "total_invoices": invoices.count(),
        "paid_count": invoices.filter(is_paid=True).count(),
        "unpaid_count": invoices.filter(is_paid=False).count(),
    }

    return render(request, "invoices/invoice.html", context)


def show_invoices(request):
    search_query = request.GET.get("q", "").strip()

    
    invoices = Invoice.objects.all().order_by("-date_created")

    if search_query:
        invoices = invoices.filter(
            customer_name__icontains=search_query
        ) | invoices.filter(
            invoice_number__icontains=search_query
        )

    context = {
        "invoices": invoices,
        "search_query": search_query,
    }

    return render(request, "invoices/all_invoices.html", context)


def add_invoice(request):
    if request.method == "POST":
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.date_created = timezone.now()
            invoice.save()

            messages.success(request, "Invoice created successfully.")
            return redirect("all_invoices")
    else:
        form = InvoiceForm()

    return render(
        request,
        "invoices/add_invoice.html",
        {"form": form}
    )



def delete_invoice(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)

    if request.method == "POST":
        invoice.delete()
        messages.success(request, "Invoice deleted successfully.")
        return redirect("all_invoices")

    return redirect("all_invoices")



def create_invoice(request):
    return redirect("add_invoice")

def show_one_invoice(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)

    return render(
        request,
        "invoices/invoice_details.html",
        {"invoice": invoice}
    )

def show_unpaid(request):
    invoices = Invoice.objects.filter(
    is_paid=False
    ).order_by("-date_created")

    
    context = {
        "invoices": invoices,
        "unpaid_count": invoices.count(),
        "unpaid_total": (
            invoices.aggregate(total=Sum("amount"))["total"]
            or Decimal("0.00")
        ),
    }

    return render(
        request,
        "invoices/unpaid_invoices.html",
        context
    )


def mark_as_paid(request, pk):
    if request.method != "POST":
        return redirect("all_invoices")


    invoice = get_object_or_404(Invoice, pk=pk)
    invoice.is_paid = True
    invoice.save(update_fields=["is_paid"])

    messages.success(
        request,
        f"Invoice {invoice.invoice_number} marked as paid."
    )

    return redirect("show_one_invoice", pk=invoice.pk)

