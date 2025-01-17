
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add_employee, name='add_employee'),
    path('edit/<int:pk>/', views.edit_employee, name='edit_employee'),
    path('delete/<int:pk>/', views.delete_employee, name='delete_employee'),
    path('statistics/', views.statistics, name='statistics'),  # Page des statistiques
    path('settings/', views.settings, name='settings'),  # Page des paramètres
    path('profile/', views.profile, name='profile'),  # Page de profil
    # path('departments/', views.departments, name='departments'),  # Page des départements
    # path('leaves/', views.leaves, name='leaves'),  # Page des congés

    # URLs pour les départements
    path('departments/', views.department_list, name='department_list'),
    path('departments/add/', views.department_add, name='department_add'),
    path('departments/edit/<int:pk>/', views.department_edit, name='department_edit'),
    path('departments/delete/<int:pk>/', views.department_delete, name='department_delete'),

    path('leaves/', views.leave_list, name='leave_list'),
    path('leaves/add/', views.leave_add, name='leave_add'),
    path('leaves/edit/<int:pk>/', views.leave_edit, name='leave_edit'),
    path('leaves/delete/<int:pk>/', views.leave_delete, name='leave_delete'),
]