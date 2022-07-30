# Generated by Django 4.0.6 on 2022-07-29 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Convert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32, verbose_name='First name')),
                ('last_name', models.CharField(max_length=32, verbose_name='Last name')),
                ('phone_no', models.CharField(max_length=11, verbose_name='Phone number')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('address', models.CharField(max_length=100, null=True, verbose_name='Address')),
                ('town', models.CharField(max_length=100, null=True, verbose_name='Town/City')),
                ('state', models.CharField(max_length=100, null=True, verbose_name='State')),
                ('school', models.CharField(max_length=100, null=True, verbose_name='School')),
                ('profession', models.CharField(max_length=100, null=True, verbose_name='Profession')),
                ('program', models.CharField(max_length=50, null=True, verbose_name='Program')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32, verbose_name='First name')),
                ('last_name', models.CharField(max_length=32, verbose_name='Last name')),
                ('phone_no', models.CharField(max_length=11, verbose_name='Phone number')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('linkedin', models.CharField(max_length=60, null=True, verbose_name='LinkedIn')),
                ('address', models.CharField(max_length=100, null=True, verbose_name='Address')),
                ('town', models.CharField(max_length=100, null=True, verbose_name='Town/City')),
                ('state', models.CharField(max_length=100, null=True, verbose_name='State')),
                ('school', models.CharField(max_length=100, null=True, verbose_name='School')),
                ('profession', models.CharField(max_length=100, null=True, verbose_name='Profession')),
                ('member', models.CharField(max_length=5, verbose_name='DLBC Member')),
                ('denomination', models.CharField(max_length=254, null=True, verbose_name='Denomination')),
                ('program', models.CharField(max_length=50, null=True, verbose_name='Program')),
            ],
        ),
        migrations.AlterField(
            model_name='location',
            name='district',
            field=models.CharField(max_length=32, verbose_name='District'),
        ),
        migrations.AlterField(
            model_name='location',
            name='group',
            field=models.CharField(max_length=32, verbose_name='Group'),
        ),
        migrations.AlterField(
            model_name='location',
            name='region',
            field=models.CharField(max_length=32, verbose_name='Region'),
        ),
    ]