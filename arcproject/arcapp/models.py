from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# def validate_box_number(value):
#     if not value.isdigit() or len(value) != 6:
#         raise ValidationError("Box number must be exactly 6 digits.")

BOX_TYPE_CHOICES = [
    ('Archiving Claims', 'Archiving Claims'),
    ('retrieval_claims', 'Retrieval Claims'),
    ('ri', 'RI'),
    ('statement', 'Statement'),
    ('archiving_nbe', 'Archiving NBE'),
    ]

from django.conf import settings

# Normalized tables for master data
class BoxType(models.Model):
    name = models.CharField(max_length=250, unique=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        editable=False,
        db_column='CREATED_BY'
    )
    data_entrance_date = models.DateTimeField(
        default=now, 
        editable=False, 
        db_column='DATA_ENTRANCE_DATE'
    )
    
    class Meta:
        db_table = 'ARCAPP_BOXTYPE'
        
    def __str__(self):
        return self.name

class BoxLocation(models.Model):
    name = models.CharField(max_length=250, unique=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        editable=False,
        db_column='CREATED_BY'
    )
    data_entrance_date = models.DateTimeField(
        default=now, 
        editable=False, 
        db_column='DATA_ENTRANCE_DATE'
    )
    
    class Meta:
        db_table = 'ARCAPP_BOXLOCATION'
        
    def __str__(self):
        return self.name
    


class ClaimStatus(models.Model):
    name = models.CharField(max_length=250, unique=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        editable=False,
        db_column='CREATED_BY'
    )
    data_entrance_date = models.DateTimeField(
        default=now, 
        editable=False, 
        db_column='DATA_ENTRANCE_DATE'
    )
    
    class Meta:
        db_table = 'ARCAPP_CLAIMSTATUS'
        
    def __str__(self):
        return self.name
    


class InsuranceCompany(models.Model):
    name = models.CharField(max_length=250, unique=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        editable=False,
        db_column='CREATED_BY'
    )
    data_entrance_date = models.DateTimeField(
        default=now, 
        editable=False, 
        db_column='DATA_ENTRANCE_DATE'
    )
    
    class Meta:
        db_table = 'ARCAPP_INSURANCECOMPANY'
        
    def __str__(self):
        return self.name
    


class audit_by(models.Model):
    name = models.CharField(max_length=250, unique=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        editable=False,
        db_column='CREATED_BY'
    )
    data_entrance_date = models.DateTimeField(
        default=now, 
        editable=False, 
        db_column='DATA_ENTRANCE_DATE'
    )
    
    class Meta:
        db_table = 'ARCAPP_audit_by'
        
    def __str__(self):
        return self.name
    

# class BoxStatus(models.Model):
#     name = models.CharField(max_length=250, unique=True)
#     created_by = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.SET_NULL,
#         null=True,
#         editable=False,
#         db_column='CREATED_BY'
#     )
#     data_entrance_date = models.DateTimeField(
#         default=now, 
#         editable=False, 
#         db_column='DATA_ENTRANCE_DATE'
#     )
    
#     class Meta:
#         db_table = 'ARCAPP_BOXSTATUS'
        
#     def __str__(self):
#         return self.name

# Keep the old master_data class for backward compatibility during migration
# You can remove this after migration is complete and data is transferred



class return_by_user(models.Model):
    name = models.CharField(max_length=250, unique=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        editable=False,
        db_column='CREATED_BY'
    )
    data_entrance_date = models.DateTimeField(
        default=now,
        editable=False,
        db_column='DATA_ENTRANCE_DATE'
    )

    class Meta:
        db_table = 'ARCAPP_RETURNBYUSER' 

    def __str__(self):
        return self.name
    

class segregation_by(models.Model):
    name = models.CharField(max_length=250, unique=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        editable=False,
        db_column='CREATED_BY'
    )
    data_entrance_date = models.DateTimeField(
        default=now,
        editable=False,
        db_column='DATA_ENTRANCE_DATE'
    )

    class Meta:
        db_table = 'ARCAPP_SegregationBy' 

    def __str__(self):
        return self.name
class request_by(models.Model):
    name = models.CharField(max_length=250, unique = True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        editable=False,
        db_column = 'CREATED_BY'
    )
    data_entrance_date = models.DateTimeField(
        default=now,
        editable=False,
        db_column='DATA_ENTRANCE_DATE'
    )

    class Meta:
        db_table = 'ARCAPP_RequestBy'
    def __str__(self):
        return self.name


class master_data(models.Model):
    box_type = models.CharField(max_length=250, unique=True)
    box_location = models.CharField(max_length=250, unique= True)
    #box_status = models.CharField(max_length=250, unique=True)
    insurance_company = models.CharField(max_length=250, unique = True)
    

    ############ thy claimsttats$####################$#$#$#$#$ 
    claim_status = models.CharField(max_length=250, unique=True)
    audit_by = models.CharField(max_length= 250, unique=True)
    return_by_user = models.CharField(max_length=250, unique=True)
    segregation_by_user = models.CharField(max_length=250, unique=True)
    request_by_user = models.CharField(max_length=250, unique=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        editable=False,
        db_column='CREATED_BY'
    )
    data_entrance_date = models.DateTimeField(
        default=now, 
        editable=False, 
        db_column='DATA_ENTRANCE_DATE'
    )
    class Meta:
        db_table = 'ARCAPP_MASTERDATA'
    def __str__(self):
        return f'{self.insurance_company or self.box_type or self.box_location}'

class Box(models.Model):
    box_number = models.CharField(
        max_length=255, 
        unique=True, 
        #validators = [validate_box_number],
        db_column='BOX_NUMBER'
    )
    # Update foreign keys to point to the new normalized tables
    box_type = models.ForeignKey(
        BoxType,
        on_delete=models.CASCADE,
        db_column='BOX_TYPE'
    )
    box_location = models.ForeignKey(
        BoxLocation,
        on_delete=models.CASCADE,
        db_column='BOX_LOCATION'
    )
    # box_status = models.ForeignKey(
    #     BoxStatus,
    #     on_delete=models.CASCADE,
    #     db_column='BOX_STATUS'
    # )
    insurance_company = models.ForeignKey(
        InsuranceCompany,
        on_delete=models.CASCADE,
        db_column='INSURANCE_COMPANY'
    )
    data_entrance_date = models.DateTimeField(
        default=now, 
        editable=False, 
        db_column='DATA_ENTRANCE_DATE'
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        editable=False,
        db_column='CREATED_BY'
    )
    Update_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='boxes_updated',
        editable=False,
    )
    
    def __str__(self):
        return self.box_number
        
    class Meta:
        db_table = 'ARCAPP_BOX'
        permissions = [
            ('can_create_box', 'Can create a new box'),
            ('can_view_box', 'Can view box details'),
            ('can_update_box', 'Can update a box'),
            ('can_delete_box', 'Can delete a box'),
        ]

class Client(models.Model):
    name = models.CharField(max_length=255)
    client_id = models.IntegerField(unique=True)
    
    class Meta:
        db_table = 'ARCAPP_CLIENT'

class insurance_policy(models.Model):
    # Update foreign key to point to the new InsuranceCompany model
    insurance_company = models.ForeignKey(
        InsuranceCompany, 
        on_delete=models.CASCADE,
        db_column='INSURANCE_COMPANY_ID'
    )
    
    policy_id = models.IntegerField(unique=True)  
    client_name = models.CharField(max_length=255, null=True, blank=True)
    client_id = models.CharField(max_length=200, null = True, blank= True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        editable=False,
        db_column='CREATED_BY'
    )
    Update_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='insurance_updated_by', 
        editable=False
    )

    class Meta:
        db_table = 'ARCAPP_INSURANCECPOLICY'
        permissions = [
            ('can_create_insurance', 'Can create a new insurance'),
            ('can_view_inurance', 'Can view box insurance'),
            ('can_update_insurance', 'Can update a insurance'),
            ('can_delete_insurance', 'Can delete a insurance'),
        ]
        
    def __str__(self):
        return f'{self.policy_id}'

class ProviderSegregation(models.Model):
    box_number = models.ForeignKey(Box, on_delete=models.CASCADE) 
    ClaimCode = models.CharField(max_length=255, unique=True)
    PolicyId = models.ForeignKey(
        'insurance_policy',
        on_delete=models.CASCADE,
        db_column='POLICYID' 
    )
    # policyname = models.CharField(max_length=255)
    ClientId = models.CharField(max_length=255)
    Member_name = models.CharField(max_length=255)
    Provider_name = models.CharField(max_length=255)
    Receive_date = models.DateField(editable=True)
    Issuance_date = models.DateField()
    Segregation_date = models.DateField()


    #Segregation_by = models.CharField(max_length=255)

    Segregation_by = models.ForeignKey(
        
        segregation_by,
        null=True,
        on_delete=models.CASCADE,
        db_column='Seg_by'
    )

    Audit_date = models.DateField()

    
    #Audit_by = models.CharField(max_length=255)


    Audit_by = models.ForeignKey(
        
        audit_by,
        on_delete=models.CASCADE,
        db_column='audit_user'
    )

    request_by = models.ForeignKey(
        
        request_by,
        on_delete=models.CASCADE,
        null=True,
        
        db_column='REQUEST_BY'
    )

    #Box_status = models.CharField(max_length=255)
    batchID = models.CharField(max_length=255)
    #request_by = models.CharField(max_length=100, default='UNKOWN')
    request_date = models.DateField(default=now)
    Client_name = models.CharField(max_length=255)
    claimscan = models.BooleanField(max_length=100, null=True, blank=True)
    DeductedAmount = models.DecimalField(max_digits=10, decimal_places=2, null=True) 
    note = models.CharField(max_length=255, null=True, blank=True)
    retrieval_date = models.DateField(null=True, blank=True)


    #return_by = models.CharField(max_length=255, null=True, blank=True)
    return_by = models.ForeignKey(
    return_by_user,
    on_delete=models.SET_NULL, # Allows claim to exist if return_by_user is deleted
    null=True,
    blank=True,
    db_column='return_by_user'
)



    return_date = models.DateField(null = True, blank=True)
    comment = models.CharField(max_length=500, blank=True, null=True)
    data_entrance_date = models.DateTimeField(default=now, editable=False)
    claim_status = models.ForeignKey(
        ClaimStatus,
        on_delete=models.CASCADE,
        db_column= 'CLAIM_STATUS'
    )

    # box_status = models.ForeignKey(
    #     BoxStatus,
    #     on_delete=models.CASCADE,
    #     db_column='BOX_STATUS'
    # )


    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        editable=False,
        db_column='PROVIDER_CREATED_BY'
    )
    Update_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='provider_updated_by', 
        editable=False
    )

    def __str__(self):
        return f"Provider Segregation for Box {self.box_number}" 
    class Meta:
        permissions = [
            ('can_create_provider_segre', 'Can create a new providers'),
            ('can_view_provider_segre', 'Can view providers details'),
            ('can_update_provider_segre', 'Can update a providers'),
            ('can_delete_provider_segre', 'Can delete a providders'),
        ]
    

class ReimbursementSegregation(models.Model):
    box_number = models.ForeignKey(Box, on_delete=models.CASCADE) 
    Claim_Code = models.CharField(max_length=255, unique=True)
    Batch_num = models.CharField(max_length=255)
    Batch_type = models.CharField(max_length=255)
    English_name = models.CharField(max_length=255)
    Arab_name = models.CharField(max_length=255)
    Payer = models.CharField(max_length=255)
    Policy = models.CharField(max_length=255)
    Hof = models.CharField(max_length=255)
    Audit_user = models.CharField(max_length=255)
    Audit_date = models.DateField() 
    data_entrance_date = models.DateTimeField(default=now, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        editable=False,
        db_column='CREATED_BY'
    )
    Update_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='riembursement_updated_by', 
        editable=False
    )

    def __str__(self):
        return f"Reimbursement Segregation for Box {self.box_number}"
    class Meta:
                permissions = [
            ('can_create_rein_segre', 'Can create a new riembursements'),
            ('can_view_reim_segre', 'Can view riembursements details'),
            ('can_update_reim_segre', 'Can update a riembuursements'),
            ('can_delete_reim_segre', 'Can delete a riembursements'),
        ]

class User(AbstractUser):
    password_changed = models.BooleanField(default=False)

    class Meta:
        db_table = 'AUTH_USER'



######### data atagging ##########

from django.core.validators import MinValueValidator
from decimal import Decimal

class SegregationStep(models.Model):
    BATCH_TYPE_CHOICES = [
        ('inpatient', 'Inpatient'),
        ('outpatient', 'Outpatient'),
        ('pharmacy', 'Pharmacy'),
        ('dental', 'Dental'),
        ('vision', 'Vision'),
    ]
    
    CLAIM_TYPE_CHOICES = [
        ('medical', 'Medical'),
        ('pharmacy', 'Pharmacy'),
        ('dental', 'Dental'),
        ('vision', 'Vision'),
        ('other', 'Other'),
    ]
    
    PROVIDER_TYPE_CHOICES = [
        ('hospital', 'Hospital'),
        ('clinic', 'Clinic'),
        ('pharmacy', 'Pharmacy'),
        ('lab', 'Laboratory'),
        ('specialist', 'Specialist'),
    ]
    
    # Policy Information
    policy_id_1 = models.CharField(max_length=50, verbose_name="Policy ID 1")
    policy_id_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Policy ID 2")
    
    # Client Information
    client_id = models.CharField(max_length=50, verbose_name="Client ID")
    insurance_company = models.CharField(max_length=200, verbose_name="Insurance Company")
    client_name = models.CharField(max_length=200, verbose_name="Client Name")
    member_name = models.CharField(max_length=200, verbose_name="Member Name")
    card_number = models.CharField(max_length=50, verbose_name="Card Number")
    emp_code = models.CharField(max_length=50, verbose_name="Employee Code")
    
    # Batch Information
    batch_receiving = models.CharField(max_length=100, verbose_name="Batch Receiving")
    parent_bid = models.CharField(max_length=50, verbose_name="Parent BID")
    batch_type = models.CharField(max_length=20, choices=BATCH_TYPE_CHOICES, verbose_name="Batch Type")
    
    # Provider Information
    provider_type_name = models.CharField(max_length=20, choices=PROVIDER_TYPE_CHOICES, verbose_name="Provider Type")
    pid = models.CharField(max_length=50, verbose_name="PID")
    
    # Claim Information
    claim_code = models.CharField(max_length=100, unique=True, verbose_name="Claim Code (Our Identifier)")
    service_date = models.DateField(verbose_name="Service Date")
    claim_type = models.CharField(max_length=20, choices=CLAIM_TYPE_CHOICES, verbose_name="Claim Type")
    
    # Provider Memo
    provider_memo_code = models.CharField(max_length=50, blank=True, null=True, verbose_name="Provider Memo Code")
    provider_memo = models.TextField(blank=True, null=True, verbose_name="Provider Memo")
    
    # Financial Information
    approved_amount = models.DecimalField(
        max_digits=12, 
        decimal_places=2, 
        validators=[MinValueValidator(Decimal('0.00'))],
        verbose_name="Approved Amount"
    )
    deducted_amount = models.DecimalField(
        max_digits=12, 
        decimal_places=2, 
        validators=[MinValueValidator(Decimal('0.00'))],
        default=Decimal('0.00'),
        verbose_name="Deducted Amount"
    )
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'segregation_step'
        verbose_name = 'Segregation Step'
        verbose_name_plural = 'Segregation Steps'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.claim_code} - {self.member_name}"
    
    @property
    def net_amount(self):
        """Calculate net amount after deduction"""
        return self.approved_amount - self.deducted_amount