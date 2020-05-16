# Generated by Django 3.0.5 on 2020-05-16 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(choices=[('Red', 'Red'), ('Green', 'Green'), ('Black', 'Black'), ('Withe', 'Withe'), ('Gray', 'Gray')], max_length=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmition',
            field=models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic'), ('Robot', 'Robot')], max_length=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='year_of_issue',
            field=models.IntegerField(),
        ),
    ]
