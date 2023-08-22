from django.contrib import admin
from .models import Book,Loan,Customer

admin.site.register(Customer)
admin.site.register(Book)
admin.site.register(Loan)