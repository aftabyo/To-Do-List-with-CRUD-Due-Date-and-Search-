# Generated by Django 5.0 on 2024-02-29 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_task_options_alter_task_order_with_respect_to'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['complete']},
        ),
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterOrderWithRespectTo(
            name='task',
            order_with_respect_to=None,
        ),
    ]