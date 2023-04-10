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
    list_display = ["vehicle", "reservation_number","guest", "description","date", "is_referenced"]
    search_fields = ["vehicle", "reservation_number","guest", "description"]
    list_filter = ["vehicle"]
    
    def is_referenced(self, obj):
        return Claim.objects.filter(damage_id=obj.id).exists()
    is_referenced.boolean = True
    is_referenced.short_description = 'Referenced by Claim'
    
@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    model= Claim
    list_display = ["damage", "status", "estimate_made", "demand_made", "claim_number","insurance_company"]
    search_fields = ["damage", "status", "claim_number","insurance_company"]
    list_filter = ["status", "insurance_company"]
    readonly_fields = ["estimate_made", "demand_made"]
    
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
    list_display = ["make", "model", "year","plate_number", "color", "turo_link"]
    search_fields = ["make", "model", "year","plate_number", "color", "turo_link"]
    list_filter = ["make", "model", "year","plate_number", "color", "turo_link"]
    




