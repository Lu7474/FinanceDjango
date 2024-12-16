# Generated by Django 4.2.17 on 2024-12-16 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0002_remove_category_name_alter_expense_category_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expense",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="expenses",
                to="dashboard.category",
                verbose_name="Категория",
            ),
        ),
        migrations.AlterField(
            model_name="income",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="incomes",
                to="dashboard.category",
                verbose_name="Категория",
            ),
        ),
    ]
