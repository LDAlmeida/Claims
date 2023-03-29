from django.db import models
from django.urls import reverse

# Create your models here.


class Vehicle(models.Model):
	make = models.CharField(blank=False, max_length=30)
	model = models.CharField(blank=False, max_length=30)
	year = models.CharField(blank=False, max_length=4)
	plate_number = models.CharField(blank = True, max_length=10)
	color = models.CharField(blank= True, max_length=20)
	turo_link = models.CharField(blank=True, max_length=100)

	class Meta:
		verbose_name = "Vehicle"
		verbose_name_plural = "Vehicles"

	def __str__(self):
		return f'{self.make} {self.model} {self.year}'

	def get_absolute_url(self):
		return reverse("vehicle_detail", kwargs={"pk": self.pk})


class Guest(models.Model):

	full_name = models.CharField(blank=False, max_length=100)
	phone_number = models.CharField(blank=False, max_length=50)
	drivers_license = models.FileField(
		blank=False, upload_to="Claims/media/GuestPhotos/DL/")
	insurance = models.FileField(
		blank=False, upload_to="Claims/media/GuestPhotos/Insurance/")

	class Meta:
		verbose_name = "Guest"
		verbose_name_plural = "Guests"

	def __str__(self):
		return self.full_name

	def get_absolute_url(self):
		return reverse("guest_detail", kwargs={"pk": self.pk})


class InsuranceCompany(models.Model):
	name = models.CharField(blank=False, max_length=50)
	phone_number = models.CharField(blank=True, max_length=50)

	class Meta:
		verbose_name = "Insurance company"
		verbose_name_plural = "Insurance companies"

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("insurancecompany_detail", kwargs={"pk": self.pk})


class Adjuster(models.Model):

	name = models.CharField(max_length=100)
	company = models.ForeignKey(InsuranceCompany, blank=False, verbose_name=(
		"Insurance Company"), on_delete=models.CASCADE)
	phone_number = models.CharField(max_length=50)

	class Meta:
		verbose_name = "Adjuster"
		verbose_name_plural = "Adjusters"

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("adjuster_detail", kwargs={"pk": self.pk})


class AutoShop(models.Model):

	name = models.CharField(blank=False, max_length=100)
	phone_number = models.CharField(blank=True, max_length=50)

	class Meta:
		verbose_name = "Auto shop"
		verbose_name_plural = "Auto shops"

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("autoshop_detail", kwargs={"pk": self.pk})


class Damage(models.Model):
	date = models.DateField(
		blank=False, help_text="Date of return from Turo/Date of damage")
	description = models.TextField(
		blank=False, max_length=1024, help_text="Description of damages and where they are")
	reservation_number = models.CharField(blank=False, max_length=8)
	vehicle = models.ForeignKey(Vehicle, blank=False, verbose_name=(
		"Vehicle"), on_delete=models.CASCADE)
	guest = models.ForeignKey(Guest, blank=False, verbose_name=(
		"Guest"), on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Damage"
		verbose_name_plural = "Damages"

	def __str__(self):
		return f'{self.vehicle.model} Damage - {self.guest.full_name}'

	def get_absolute_url(self):
		return reverse("damage_detail", kwargs={"pk": self.pk})


class DamagePhoto(models.Model):
	class BeforeOrAfter(models.TextChoices):
		BEFORE = 'Before'
		AFTER = 'After'
	
	photo = models.FileField(upload_to="Claims/media/DamagePhotos/")
	damage = models.ForeignKey(
		Damage, on_delete=models.CASCADE, related_name='Photos')
	before_or_after = models.CharField(choices=BeforeOrAfter.choices, max_length=20)

	def __str__(self):
		return f'{self.damage.guest.full_name} - {self.damage.vehicle.model}'

	class Meta:
		verbose_name = "Damage photo"
		verbose_name_plural = "Damage photos"

class Claim(models.Model):
	class Status(models.TextChoices):
		OPEN = "Open recently"
		WAITING_ESTIMATE = "Waiting on estimate"
		ESTIMATE_READY = "Estimate ready"
		ESTIMATE_SENT = "Estimate sent to insurance company"
		DENIED = "Denied"
		DEMAND_SENT = "Demand letter sent"
		WAITING_PAYMENT = "Waiting on payment from insurance company/Guest"
		PAID = "Paid"
		DEDUCTIBLE = "Needs Deductible"
		CLOSED = "Closed"
	
	status = models.CharField(choices=Status.choices, max_length=200)
	damage = models.ForeignKey(Damage, verbose_name= "Damage", on_delete=models.CASCADE)
	rental_agreement = models.FileField(null = True, upload_to="Claims/media/RentalAgreements/")
	claim_number = models.CharField(max_length=50)
	insurance_company = models.ForeignKey(InsuranceCompany, blank = True, verbose_name="Insurance Company", on_delete=models.CASCADE)
	adjuster = models.ForeignKey(Adjuster, blank= True, verbose_name="Name of the adjuster", on_delete=models.CASCADE)
	estimate_made = models.BooleanField()
	estimate_file = models.FileField(blank = True, upload_to="Claims/media/Estimates/")
	auto_shop = models.ForeignKey(AutoShop, blank= True, verbose_name="Auto/Body shop", on_delete=models.CASCADE)
	demand_made = models.BooleanField()
	demand_file = models.FileField(blank = True, upload_to="Claims/media/DemandLetters/")
	demand_intake = models.CharField(blank = True, max_length=10)
	observation = models.TextField(
	blank=True, null=True, max_length=1024, help_text="Observations and notes about the claim")
 
	class Meta:
		verbose_name = "Claim"
		verbose_name_plural = "Claims"

	def __str__(self):
		if self.claim_number:
			return self.claim_number
		else: 
			return self.damage

	def get_absolute_url(self):
		return reverse("claim_detail", kwargs={"pk": self.pk})
