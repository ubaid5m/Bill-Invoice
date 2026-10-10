from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Invoice

# Create your views here.

# def homepageview(request):
#     #return HttpResponse("Your home page!")
#     return render(request, 'home.html')

# def invoiceslist(request):
#     #return HttpResponse("Your invoices page!")
#     return render(request,'invoices.html')
def showinvoice(request):
    return HttpResponse("your page")




# Create your views here.

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