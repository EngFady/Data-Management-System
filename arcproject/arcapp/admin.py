from django.contrib import admin
from .models import Box, ProviderSegregation, ReimbursementSegregation, insurance_policy, master_data


from django.contrib.auth.admin import UserAdmin
from .models import User



@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    list_display = ('box_number', 'box_type', 'box_location', 'insurance_company', 'data_entrance_date', 'created_by')
    search_fields = ('box_number', 'box_type', 'insurance_company')
    list_filter = ('box_type', 'insurance_company')
    def created_by_username(self, obj):
        return obj.created_by.username if obj.created_by else "-"
    created_by_username.short_description = 'Created By'

@admin.register(ProviderSegregation)
class ProviderSegregationAdmin(admin.ModelAdmin):
    list_display = ('box_number', 'ClaimCode', 'Member_name', 'Provider_name', 'Segregation_date')
    search_fields = ('ClaimCode', 'Member_name', 'Provider_name')
    #list_filter = ('Box_status', 'claimscan')
    date_hierarchy = 'Segregation_date'

@admin.register(ReimbursementSegregation)
class ReimbursementSegregationAdmin(admin.ModelAdmin):
    list_display = ('box_number', 'Claim_Code', 'English_name', 'Payer', 'Policy')
    search_fields = ('Claim_Code', 'English_name', 'Arab_name')
    list_filter = ('Payer', 'Batch_type')
    date_hierarchy = 'Audit_date'



admin.site.register(User, UserAdmin)  # Register with default UserAdmin

admin.site.register(insurance_policy)
admin.site.register(master_data)


admin.site.site_header = "Batman 🦇"
admin.site.site_title = "Batman Admin Portal"
admin.site.index_title = "Welcome to the Batcave"