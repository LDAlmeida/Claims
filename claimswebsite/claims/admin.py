from django.contrib import admin

from claims.models import *

# Register your models here.

class DamagePhotoInline(admin.StackedInline):
    model = DamagePhoto
    extra = 0

@admin.register(Damage)
class DamageAdmin(admin.ModelAdmin):
    model = Damage
    inlines = [DamagePhotoInline]
    
@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    model= Claim

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    model = Guest
    
@admin.register(Adjuster)
class AdjusterAdmin(admin.ModelAdmin):
    model = Adjuster
    
@admin.register(AutoShop)
class AutoShopAdmin(admin.ModelAdmin):
    model = AutoShop
    
@admin.register(InsuranceCompany)
class InsuranceCompanyAdmin(admin.ModelAdmin):
    model = InsuranceCompany
    
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    model = Vehicle
    




