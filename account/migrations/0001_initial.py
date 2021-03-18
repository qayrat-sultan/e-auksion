# Generated by Django 3.1.7 on 2021-03-13 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('parent_name', models.CharField(max_length=50, verbose_name='Отчество')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('password', models.CharField(max_length=50, verbose_name='Пароль')),
                ('date_of_birth', models.DateField()),
                ('sex', models.IntegerField(choices=[(1, 'Мужской'), (2, 'Женский')], verbose_name='Пол')),
                ('phone_number', models.IntegerField(unique=True, verbose_name='Телефонный номер')),
                ('stir', models.IntegerField(unique=True, verbose_name='ИНН')),
                ('person', models.IntegerField(choices=[(1, 'Физическое лицо'), (2, 'Юридическое лицо')], verbose_name='Принадлежность лица')),
                ('passport', models.CharField(max_length=10, unique=True, verbose_name='Паспортные данные')),
                ('date_of_passport', models.DateField()),
                ('passport_issued_by', models.CharField(max_length=100, verbose_name='Кем выдан паспорт')),
                ('pinfl', models.IntegerField(verbose_name='ПИНФЛ')),
                ('region', models.CharField(max_length=15, verbose_name='Регион')),
                ('area', models.CharField(max_length=20, verbose_name='Район')),
                ('address', models.CharField(max_length=120, verbose_name='Адрес')),
                ('organizatsion', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Наименование организации')),
                ('stir_yur', models.PositiveIntegerField(blank=True, null=True, unique=True, verbose_name='ИНН юр лица')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]