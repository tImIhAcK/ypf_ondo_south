# Generated by Django 4.0.6 on 2023-02-18 08:20

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('custom_admin', '0003_alter_convert_options_alter_participant_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convert',
            name='category',
            field=models.CharField(choices=[('', 'Select category'), ('ENT', 'Enterprenuer'), ('UNGRAD', 'Undergraduate'), ('GRAD', 'Graduate'), ('CORP', 'Corper'), ('PRIVATE/GOVR', 'Private/Goverment Worker'), ('YOUNG PROF', 'Young Professionals'), ('RES', 'Researcher'), ('TERT STAFF', 'Tertiary Institution Worker'), ('POST SEC', 'Post Secondary School Student'), ('OTH', 'Others')], max_length=20, null=True, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='convert',
            name='denomination',
            field=models.CharField(choices=[('', 'Select denomination'), ('DLBC', 'Deeper Life Bible Church'), ('RCCG', 'The Redeemed Christian Church Of God'), ('CAC', 'Christ Apostolic Church'), ('AFC', 'Apostolic Faith Church'), ('MFM', 'Mountain of Fire and Miracle Ministry'), ('GOFAMINT', 'Gospel Faith Mission'), ('LFC', 'Living Faith Church'), ('CATH', 'Catholic Church'), ('ANG', 'Anglican Church'), ('BAP', 'Baptist Church'), ('CEM', 'Christ Embassy'), ('MTH', 'Methodist Church'), ('TLC', "The Lord's Chosen"), ('CCC', 'Celestial Church of Christ'), ('C&S', 'Cherubim and Seraphim'), ('OTH', 'Others')], max_length=10, null=True, verbose_name='Denomination'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='category',
            field=models.CharField(choices=[('', 'Select category'), ('ENT', 'Enterprenuer'), ('UNGRAD', 'Undergraduate'), ('GRAD', 'Graduate'), ('CORP', 'Corper'), ('PRIVATE/GOVR', 'Private/Goverment Worker'), ('YOUNG PROF', 'Young Professionals'), ('RES', 'Researcher'), ('TERT STAFF', 'Tertiary Institution Worker'), ('POST SEC', 'Post Secondary School Student'), ('OTH', 'Others')], max_length=20, null=True, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='denomination',
            field=models.CharField(choices=[('', 'Select denomination'), ('DLBC', 'Deeper Life Bible Church'), ('RCCG', 'The Redeemed Christian Church Of God'), ('CAC', 'Christ Apostolic Church'), ('AFC', 'Apostolic Faith Church'), ('MFM', 'Mountain of Fire and Miracle Ministry'), ('GOFAMINT', 'Gospel Faith Mission'), ('LFC', 'Living Faith Church'), ('CATH', 'Catholic Church'), ('ANG', 'Anglican Church'), ('BAP', 'Baptist Church'), ('CEM', 'Christ Embassy'), ('MTH', 'Methodist Church'), ('TLC', "The Lord's Chosen"), ('CCC', 'Celestial Church of Christ'), ('C&S', 'Cherubim and Seraphim'), ('OTH', 'Others')], max_length=10, null=True, verbose_name='Denomination'),
        ),
        migrations.CreateModel(
            name='Newcomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32, verbose_name='First name')),
                ('last_name', models.CharField(max_length=32, verbose_name='Last name')),
                ('gender', models.CharField(choices=[('', 'Select gender'), ('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='Gender')),
                ('age', models.CharField(choices=[('', 'Select age group'), ('16-20', '16-20'), ('21-25', '21-25'), ('26-30', '26-30'), ('30-35', '30-35'), ('36-40', '36-40'), ('41-45', '41-45'), ('46-50', '46-50'), ('51-55', '51-55'), ('56-60', '56-60'), ('Above 60', 'Above 60')], max_length=10, verbose_name='Age')),
                ('phone_no', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('linkedin', models.CharField(blank=True, max_length=60, null=True, verbose_name='LinkedIn')),
                ('address', models.CharField(max_length=100, null=True, verbose_name='Address')),
                ('city', models.CharField(max_length=20, null=True, verbose_name='City/Town')),
                ('category', models.CharField(choices=[('', 'Select category'), ('ENT', 'Enterprenuer'), ('UNGRAD', 'Undergraduate'), ('GRAD', 'Graduate'), ('CORP', 'Corper'), ('PRIVATE/GOVR', 'Private/Goverment Worker'), ('YOUNG PROF', 'Young Professionals'), ('RES', 'Researcher'), ('TERT STAFF', 'Tertiary Institution Worker'), ('POST SEC', 'Post Secondary School Student'), ('OTH', 'Others')], max_length=20, null=True, verbose_name='Category')),
                ('school', models.CharField(max_length=100, null=True, verbose_name='School/Work Address')),
                ('denomination', models.CharField(choices=[('', 'Select denomination'), ('DLBC', 'Deeper Life Bible Church'), ('RCCG', 'The Redeemed Christian Church Of God'), ('CAC', 'Christ Apostolic Church'), ('AFC', 'Apostolic Faith Church'), ('MFM', 'Mountain of Fire and Miracle Ministry'), ('GOFAMINT', 'Gospel Faith Mission'), ('LFC', 'Living Faith Church'), ('CATH', 'Catholic Church'), ('ANG', 'Anglican Church'), ('BAP', 'Baptist Church'), ('CEM', 'Christ Embassy'), ('MTH', 'Methodist Church'), ('TLC', "The Lord's Chosen"), ('CCC', 'Celestial Church of Christ'), ('C&S', 'Cherubim and Seraphim'), ('OTH', 'Others')], max_length=10, null=True, verbose_name='Denomination')),
                ('registered_date', models.DateTimeField(auto_now_add=True)),
                ('region', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='state', chained_model_field='state', on_delete=django.db.models.deletion.CASCADE, to='custom_admin.region')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='newcomer_state', to='custom_admin.state')),
            ],
            options={
                'verbose_name': 'newcomer',
                'verbose_name_plural': 'newcomers',
                'ordering': ['-registered_date'],
            },
        ),
    ]
