# Generated by Django 4.1.7 on 2023-03-14 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adjuster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'adjuster',
                'verbose_name_plural': 'adjusters',
            },
        ),
        migrations.CreateModel(
            name='AutoShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'autoshop',
                'verbose_name_plural': 'autoshops',
            },
        ),
        migrations.CreateModel(
            name='Damage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='Date of return from Turo/Date of damage')),
                ('description', models.TextField(help_text='Description of damages and where they are', max_length=1024)),
                ('reservation_number', models.CharField(max_length=8)),
            ],
            options={
                'verbose_name': 'damage',
                'verbose_name_plural': 'damages',
            },
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=50)),
                ('drivers_license', models.FileField(upload_to='GuestPhotos/DL/')),
                ('insurance', models.FileField(upload_to='GuestPhotos/Insurance/')),
            ],
            options={
                'verbose_name': 'guest',
                'verbose_name_plural': 'guests',
            },
        ),
        migrations.CreateModel(
            name='InsuranceCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'insurancecompany',
                'verbose_name_plural': 'insurancecompanies',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30)),
                ('year', models.CharField(max_length=4)),
                ('turo_link', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'vehicle',
                'verbose_name_plural': 'vehicles',
            },
        ),
        migrations.CreateModel(
            name='DamagePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='DamagePhotos/')),
                ('before_or_after', models.CharField(choices=[('Before', 'Before'), ('After', 'After')], max_length=20)),
                ('damage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Photos', to='claims.damage')),
            ],
            options={
                'verbose_name': 'damagephoto',
                'verbose_name_plural': 'damagephotos',
            },
        ),
        migrations.AddField(
            model_name='damage',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='claims.guest', verbose_name='Guest'),
        ),
        migrations.AddField(
            model_name='damage',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='claims.vehicle', verbose_name='Vehicle'),
        ),
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Open recently', 'Open'), ('Waiting on estimate', 'Waiting Estimate'), ('Estimate ready', 'Estimate Ready'), ('Estimate sent to insurance company', 'Estimate Sent'), ('Denied', 'Denied'), ('Demand letter sent', 'Demand Sent'), ('Waiting on payment from insurance company/Guest', 'Waiting Payment'), ('Paid', 'Paid'), ('Closed', 'Closed')], max_length=200)),
                ('claim_number', models.CharField(max_length=50)),
                ('estimate_made', models.BooleanField()),
                ('estimate_file', models.FileField(upload_to='Estimates/')),
                ('demand_made', models.BooleanField()),
                ('demand_file', models.FileField(upload_to='DemandLetters/')),
                ('demand_intake', models.CharField(max_length=10)),
                ('adjuster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='claims.adjuster', verbose_name='Name of the adjuster')),
                ('auto_shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='claims.autoshop', verbose_name='Auto/Body shop')),
                ('damage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='claims.damage', verbose_name='Damage')),
                ('insurance_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='claims.insurancecompany', verbose_name='Insurance Company')),
            ],
            options={
                'verbose_name': 'claim',
                'verbose_name_plural': 'claims',
            },
        ),
        migrations.AddField(
            model_name='adjuster',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='claims.insurancecompany', verbose_name='Insurance Company'),
        ),
    ]
