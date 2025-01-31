# Generated by Django 4.2.7 on 2025-01-17 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_department_alter_employee_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaverequest',
            name='reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='leaverequest',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leave_requests', to='gestion.employee'),
        ),
        migrations.AlterField(
            model_name='leaverequest',
            name='status',
            field=models.CharField(choices=[('pending', 'En attente'), ('approved', 'Approuvé'), ('rejected', 'Rejeté')], default='pending', max_length=20),
        ),
    ]
