from django.contrib import admin

# Register your models here.
# gestion/admin.py
from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'position', 'hire_date', 'salary')  # Champs à afficher
    search_fields = ('first_name', 'last_name', 'email', 'position')  # Champs pour la recherche dans l'admin
    list_filter = ('position', 'hire_date')  # Filtres dans l'admin
