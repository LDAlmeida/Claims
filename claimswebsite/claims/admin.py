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
    list_display = ["vehicle", "reservation_number","guest", "description","date"]
    search_fields = ["vehicle", "reservation_number","guest", "description"]
    list_filter = ["vehicle"]
    
@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    model= Claim
    list_display = ["damage", "status", "claim_number","insurance_company"]
    search_fields = ["damage", "status", "claim_number","insurance_company"]
    list_filter = ["status", "insurance_company"]
    
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
    




