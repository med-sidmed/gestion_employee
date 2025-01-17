from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from django.contrib import messages

def dashboard(request):
    employees = Employee.objects.all()
    return render(request, 'dashboard.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        position = request.POST.get('position')
        hire_date = request.POST.get('hire_date')
        salary = request.POST.get('salary')
        contact = request.POST.get('contact')

        # Créer un nouvel employé
        Employee.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            position=position,
            hire_date=hire_date,
            salary=salary,
            contact=contact
        )
        messages.success(request, 'Employé ajouté avec succès.')
        return redirect('dashboard')
    return render(request, 'add_employee.html')

def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        # Mettre à jour les données de l'employé
        employee.first_name = request.POST.get('first_name')
        employee.last_name = request.POST.get('last_name')
        employee.email = request.POST.get('email')
        employee.position = request.POST.get('position')
        employee.hire_date = request.POST.get('hire_date')
        employee.salary = request.POST.get('salary')
        employee.contact = request.POST.get('contact')
        employee.save()
        messages.success(request, 'Employé modifié avec succès.')
        return redirect('dashboard')
    return render(request, 'edit_employee.html', {'employee': employee})

def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Employé supprimé avec succès.')
        return redirect('dashboard')
    return render(request, 'confirm_delete.html', {'employee': employee})




from django.shortcuts import render
from .models import Employee, Department, LeaveRequest

from django.shortcuts import render
from .models import Employee, Department, LeaveRequest
from django.db.models import Count

def statistics(request):
    # Nombre total d'employés
    total_employees = Employee.objects.count()

    # Nombre d'employés par département
    employees_by_department = Department.objects.annotate(num_employees=Count('employee')).values('name', 'num_employees')

    # Répartition des congés
    leave_status_counts = LeaveRequest.objects.values('status').annotate(count=Count('status'))

    # Évolution des embauches (exemple : par mois)
    hire_dates = Employee.objects.values_list('hire_date', flat=True)
    # Vous pouvez ajouter une logique pour regrouper les embauches par mois

    context = {
        'total_employees': total_employees,
        'employees_by_department': list(employees_by_department),
        'leave_status_counts': list(leave_status_counts),
    }
    return render(request, 'statistics.html', context)

from django.shortcuts import render, redirect
from django.contrib import messages

def settings(request):
    if request.method == 'POST':
        theme = request.POST.get('theme')
        # Sauvegarder le thème dans la session ou la base de données
        request.session['theme'] = theme
        messages.success(request, 'Thème mis à jour avec succès.')
        return redirect('settings')
    
    # Récupérer le thème actuel
    theme = request.session.get('theme', 'light')
    return render(request, 'settings.html', {'theme': theme})

def profile(request):
    # Page de profil
    return render(request, 'profile.html')

def departments(request):
    # Page des départements
    departments = Department.objects.all()
    return render(request, 'departments.html', {'departments': departments})

def leaves(request):
    # Page des congés
    leave_requests = LeaveRequest.objects.all()
    return render(request, 'leaves.html', {'leave_requests': leave_requests})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Department
from django.contrib import messages

# Liste des départements
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

# Ajouter un département
def department_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        if name:
            Department.objects.create(name=name, description=description)
            messages.success(request, 'Département ajouté avec succès.')
            return redirect('department_list')
    return render(request, 'department_form.html')

# Modifier un département
def department_edit(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        if name:
            department.name = name
            department.description = description
            department.save()
            messages.success(request, 'Département modifié avec succès.')
            return redirect('department_list')
    return render(request, 'department_form.html', {'department': department})

# Supprimer un département
def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        messages.success(request, 'Département supprimé avec succès.')
        return redirect('department_list')
    return render(request, 'department_confirm_delete.html', {'department': department})



from django.shortcuts import render, get_object_or_404, redirect
from .models import LeaveRequest, Employee
from django.contrib import messages

# Liste des congés
def leave_list(request):
    leave_requests = LeaveRequest.objects.all()
    return render(request, 'leaves.html', {'leave_requests': leave_requests})

# Ajouter un congé
def leave_add(request):
    employees = Employee.objects.all()
    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        status = request.POST.get('status')
        reason = request.POST.get('reason')

        if employee_id and start_date and end_date:
            employee = Employee.objects.get(pk=employee_id)
            LeaveRequest.objects.create(
                employee=employee,
                start_date=start_date,
                end_date=end_date,
                status=status,
                reason=reason
            )
            messages.success(request, 'Congé ajouté avec succès.')
            return redirect('leave_list')
    return render(request, 'leave_form.html', {'employees': employees})

# Modifier un congé
def leave_edit(request, pk):
    leave_request = get_object_or_404(LeaveRequest, pk=pk)
    employees = Employee.objects.all()
    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        status = request.POST.get('status')
        reason = request.POST.get('reason')

        if employee_id and start_date and end_date:
            employee = Employee.objects.get(pk=employee_id)
            leave_request.employee = employee
            leave_request.start_date = start_date
            leave_request.end_date = end_date
            leave_request.status = status
            leave_request.reason = reason
            leave_request.save()
            messages.success(request, 'Congé modifié avec succès.')
            return redirect('leave_list')
    return render(request, 'leave_form.html', {'leave_request': leave_request, 'employees': employees})

# Supprimer un congé
def leave_delete(request, pk):
    leave_request = get_object_or_404(LeaveRequest, pk=pk)
    if request.method == 'POST':
        leave_request.delete()
        messages.success(request, 'Congé supprimé avec succès.')
        return redirect('leave_list')
    return render(request, 'leave_confirm_delete.html', {'leave_request': leave_request})