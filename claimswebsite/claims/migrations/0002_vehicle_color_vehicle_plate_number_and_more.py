# Generated by Django 4.1.7 on 2023-03-29 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("claims", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="vehicle",
            name="color",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name="vehicle",
            name="plate_number",
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name="autoshop",
            name="phone_number",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="claim",
            name="adjuster",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="claims.adjuster",
                verbose_name="Name of the adjuster",
            ),
        ),
        migrations.AlterField(
            model_name="claim",
            name="auto_shop",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="claims.autoshop",
                verbose_name="Auto/Body shop",
            ),
        ),
        migrations.AlterField(
            model_name="claim",
            name="demand_file",
            field=models.FileField(blank=True, upload_to="Claims/media/DemandLetters/"),
        ),
        migrations.AlterField(
            model_name="claim",
            name="demand_intake",
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name="claim",
            name="estimate_file",
            field=models.FileField(blank=True, upload_to="Claims/media/Estimates/"),
        ),
        migrations.AlterField(
            model_name="claim",
            name="insurance_company",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="claims.insurancecompany",
                verbose_name="Insurance Company",
            ),
        ),
        migrations.AlterField(
            model_name="claim",
            name="rental_agreement",
            field=models.FileField(
                null=True, upload_to="Claims/media/RentalAgreements/"
            ),
        ),
        migrations.AlterField(
            model_name="damagephoto",
            name="photo",
            field=models.FileField(upload_to="Claims/media/DamagePhotos/"),
        ),
        migrations.AlterField(
            model_name="guest",
            name="drivers_license",
            field=models.FileField(upload_to="Claims/media/GuestPhotos/DL/"),
        ),
        migrations.AlterField(
            model_name="guest",
            name="insurance",
            field=models.FileField(upload_to="Claims/media/GuestPhotos/Insurance/"),
        ),
        migrations.AlterField(
            model_name="insurancecompany",
            name="phone_number",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="turo_link",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
