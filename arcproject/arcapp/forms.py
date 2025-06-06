from django import forms
from django_select2 import forms as s2forms
from .models import Box, ProviderSegregation, request_by,segregation_by,ReimbursementSegregation, insurance_policy, BoxType, BoxLocation, InsuranceCompany, ClaimStatus, audit_by, return_by_user
import re
from .models import SegregationStep


class InsurancePolicyForm(forms.ModelForm):
    class Meta:
        model = insurance_policy
        exclude = ['created_by', 'Update_by']
        fields = ['insurance_company', 'policy_id', 'client_name', 'client_id']
        widgets = {
            'insurance_company': forms.Select(attrs={
                'class': 'select2-ajax form-control',
                'id': 'id_insurance_company',
                'data-placeholder': 'Search for an insurance company...'
            }),
            'policy_id': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter  Policy ID',
                'style': 'border-radius: 25px; text-align: center;'
            }),
            'client_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter Client Name',
                'style': 'border-radius: 25px; text-align: center;'
            }),
                'client_id': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter Client id',
                'style': 'border-radius: 25px; text-align: center;'
            })
        }

    def clean_policy_id(self):
        policy_id = self.cleaned_data['policy_id']
        if len(str(policy_id)) > 4:
            raise forms.ValidationError("Policy ID must be a 4-digit number")
        return policy_id

# Updated form for managing master data entries
class BoxTypeForm(forms.ModelForm):
    class Meta:
        model = BoxType
        exclude = ['created_by', 'data_entrance_date']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'animated-input form-control', 
                'placeholder': 'Enter Box Type'
            })
        }






class AuditByForm(forms.ModelForm):
    class Meta:
        model = audit_by
        exclude = ['created_by', 'data_entrance_date']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'animated-input form-control', 
                'placeholder': 'Enter the Audit User'
            })
        }







class ReurnByUsrForm(forms.ModelForm):
    class Meta:
        model = return_by_user
        exclude = ['created_by', 'data_entrance_date']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'animated-input form-control', 
                'placeholder': 'Enter the return User'
            })
        }


class SegregationByUsrForm(forms.ModelForm):
    class Meta:
        model = segregation_by
        exclude = ['created_by', 'data_entrance_date']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'animated-input form-control', 
                'placeholder': 'Enter the segregation By User'
            })
        }

class RequestByUsrForm(forms.ModelForm):
    class Meta:
        model = request_by
        exclude = ['created_by', 'data_entrance_date']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'animated-input form-control', 
                'placeholder': 'Enter the user who request'
            })
        }



class ClaimStatusForm(forms.ModelForm):
    class Meta:
        model = ClaimStatus
        exclude = ['created_by', 'data_entrance_date']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'animated-input form-control', 
                'placeholder': 'Enter Claim Status'
            })
        }


class BoxLocationForm(forms.ModelForm):
    class Meta:
        model = BoxLocation
        exclude = ['created_by', 'data_entrance_date']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'animated-input form-control',
                'placeholder': 'Enter Box Location'
            })
        }
# class BoxStatusForm(forms.ModelForm):
#     class Meta:
#         model = BoxStatus
#         exclude = ['created_by', 'data_entrance_date']
#         widgets = {
#             'name': forms.TextInput(attrs={
#                 'class': 'animated-input form-control', 
#                 'placeholder': 'Enter Box Status'
#             })
#         }
class InsuranceCompanyForm(forms.ModelForm):
    class Meta:
        model = InsuranceCompany
        exclude = ['created_by', 'data_entrance_date']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'animated-input form-control',
                'placeholder': 'Enter Insurance Company Name'
            })
        }

# Master data form for backward compatibility (you can remove after migration)
FIELD_CHOICES = [
    ('box_type', 'Box Type'),
    ('box_location', 'Box Location'),
    #('box_status', 'Box Status'),
    ('claim_status', 'Claim Status'),
    ('insurance_company', 'Insurance Company'),
    ('audit_by', 'Audit By'),
    ('return_by_usr', 'Return By User'),
    ('segregation_by_usr', 'Segregation By User'),
    ('request_by_user', 'Request By User'),




]

class MasterDataForm(forms.Form):
    field_type = forms.ChoiceField(
        choices=FIELD_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'radio-select'}),
        label="Select Field Type"
    )
    field_value = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'animated-input', 'style': 'display: none;'}),
        label="Enter Value"
    )

class BoxSelect2Widget(s2forms.ModelSelect2Widget):
    search_fields = ['box_number__icontains']
    
    class Media:
        css = {
            'all': ('https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/css/select2.min.css',)
        }
        js = ('https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/js/select2.min.js',)

class BoxForm(forms.ModelForm):
    class Meta:
        model = Box
        exclude = ['created_by']
        fields = '__all__'
        widgets = {
            'box_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a box number'
            }),
            'box_type': forms.Select(attrs={'class': 'form-control'}),
            'box_location': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Search box location'}),
            'insurance_company': forms.Select(attrs={
                'class': 'select2-ajax form-control',
                'data-placeholder': 'Search for an insurance company...'
            }),
        }

    def clean_box_number(self):
        box_number = self.cleaned_data.get('box_number')
        # if not box_number.isdigit() or len(box_number) != 6:
        #     raise forms.ValidationError("Box number must be exactly 6 digits.")
        return box_number

# class ProviderSegregationForm(forms.ModelForm):
#     class Meta:
#         model = ProviderSegregation
#         exclude = ['created_by']
#         fields = '__all__'
#         widgets = {
#             'box_number': forms.Select(attrs={
#                 'class': 'select2-ajax form-control',
#                 'data-placeholder': 'Search for a box number...'
#             }),
#             'ClaimCode': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter Claim Code'
#             }),
#             'PolicyId': forms.Select(attrs={
#                 'class': 'select2-ajax form-control',
#                 'data-placeholder': '🔍 Search for a policy ID...'
#             }),
#             'policyname': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter Policy Name'
#             }),
#             'ClientId': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter Client ID'
#             }),
#             'Member_name': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter Member Name'
#             }),
#             'Provider_name': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter Provider Name'
#             }),
#             'Receive_date': forms.DateInput(attrs={
#                 'class': 'form-control',
#                 'type': 'date'
#             }),
#             'Issuance_date': forms.DateInput(attrs={
#                 'class': 'form-control',
#                 'type': 'date'
#             }),
#             'Segregation_date': forms.DateInput(attrs={
#                 'class': 'form-control',
#                 'type': 'date'
#             }),
#             'Segregation_by': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter Name of Person'
#             }),
#             'Audit_date': forms.DateInput(attrs={
#                 'class': 'form-control',
#                 'type': 'date'
#             }),
#             'Audit_by': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter Auditor Name'
#             }),
#             'Box_status': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter Box Status'
#             }),
#             'batchID': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter Batch ID'
#             }),
#             'request_by': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Requester name'
#             }),
#             'Client_name': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter Client Name'
#             }),
#             'claimscan': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
#             'DeductedAmount': forms.NumberInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter Deducted Amount'
#             }),
#         }

#     def clean_ClaimCode(self):
#         claim_code = self.cleaned_data.get('ClaimCode')
        
#         # Validate the format using regex
#         if not re.match(r'^\d+-\d+$', claim_code):
#             raise forms.ValidationError(
#                 "Claim Code must be in the format NNNN-XX (numbers separated by a hyphen). Example: 181014-32"
#             )
        
#         return claim_code

#     def clean_DeductedAmount(self):
#         deducted_amount = self.cleaned_data.get('DeductedAmount')
#         if deducted_amount < 0:
#             raise forms.ValidationError("Deducted amount cannot be negative.")
#         return deducted_amount





class ProviderSegregationForm(forms.ModelForm):
    class Meta:
        model = ProviderSegregation
        exclude = ['created_by']
        fields = [
            'box_number', 'ClaimCode', 'PolicyId', 
            'ClientId', 'Member_name', 'Provider_name', 'Receive_date', 
            'Issuance_date', 'Segregation_date', 'Segregation_by', 
            'Audit_date', 'Audit_by', 'batchID', 
            'request_by', 'request_date', 'Client_name','claim_status',  
            'claimscan', 'DeductedAmount', 'note', 'retrieval_date', 
            'return_by', 'return_date', 'comment'
        ]
        widgets = {
            'box_number': forms.Select(attrs={
                'class': 'select2-ajax form-control',
                'data-placeholder': 'Search for a box number...'
            }),
            'ClaimCode': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Claim Code'
            }),
            'PolicyId': forms.Select(attrs={
                'class': 'select2-ajax form-control',
                'data-placeholder': '🔍 Search for a policy ID...'
            }),
            # 'policyname': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Enter Policy Name'
            # }),
            'ClientId': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Client ID',
                'readonly': 'readonly'
            }),
            'Member_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Member Name'
            }),
            'Provider_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Provider Name'
            }),
            'Receive_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'Issuance_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'Segregation_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'Segregation_by': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Name of Person'
            }),
            'Audit_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'Audit_by': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Auditor Name'
            }),
            # 'Box_status': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Enter Box Status'
            # }),
            'batchID': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Batch ID'
            }),
            'request_by': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Requester name'
            }),
            'Client_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Client Name',
                'readonly': 'readonly'  # Make this field read-only for auto-fill
            }),




            'claim_status': forms.Select(attrs={
                'class': 'select2-ajax form-control',
                'data-placeholder': 'claim stats...'
            }),

            'claimscan': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'DeductedAmount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Deducted Amount'
            }),

            'retrieval_date' : forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'return_by' : forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'return_by',
            }),
            'return_date' : forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'comment' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Comment',
            }),


        }

    def clean(self):
        cleaned_data = super().clean()
        box = cleaned_data.get('box_number')
        policy = cleaned_data.get('PolicyId')
        
        # Perform validation to ensure box and policy belong to the same insurance company
        if box and policy and box.insurance_company.id != policy.insurance_company.id:
            self.add_error(
                'PolicyId', 
                f'Policy ID belongs to {policy.insurance_company.name} but box belongs to {box.insurance_company.name}. They must match.'
            )
        
        return cleaned_data

    def clean_DeductedAmount(self):
        deducted_amount = self.cleaned_data.get('DeductedAmount')
        if deducted_amount is not None and deducted_amount < 0:
            raise forms.ValidationError("Deducted amount cannot be negative.")
        return deducted_amount
    
    def clean_ClaimCode(self):
        claim_code = self.cleaned_data.get('ClaimCode')
        
        # Validate the format using regex
        if not re.match(r'^\d+-\d+$', claim_code):
            raise forms.ValidationError(
                "Claim Code must be in the format NNNN-XX (numbers separated by a hyphen). Example: 181014-32"
            )
        
        return claim_code








class ReimbursementSegregationForm(forms.ModelForm):
    class Meta:
        model = ReimbursementSegregation
        exclude = ['created_by', 'Update_by']
        fields = [
            'box_number', 'Claim_Code', 'Batch_num', 'Batch_type', 'English_name',
            'Arab_name', 'Payer', 'Policy', 'Hof', 'Audit_user', 'Audit_date'
        ]
        widgets = {
            'box_number': forms.Select(attrs={
                'class': 'select2-ajax form-control',
                'data-placeholder': 'Search for a box number...'
            }),
            'Claim_Code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Claim Code'
            }),
            'Batch_num': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Batch Number'
            }),
            'Batch_type': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Batch Type'
            }),
            'English_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter English Name'
            }),
            'Arab_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Arabic Name'
            }),
            'Payer': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Payer Name'
            }),
            'Policy': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Policy'
            }),
            'Hof': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter HOF'
            }),
            'Audit_user': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Auditor Name'
            }),
            'Audit_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }

class BoxSearchForm(forms.Form):
    box_number = forms.CharField(
        label="Box Number",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Box Number'
        })
    )

class SegreSearcForm(forms.Form):
    claim_code = forms.CharField(
        label="Claim Code",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Claim Code'
        })
    )

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label='Select CSV File')
    
class ProviderSegreeDataFile(forms.Form):
    csv_file = forms.FileField(label='Select CSV File')

class bub(forms.Form):
    csv_file = forms.FileField(help_text="Upload a CSV file with the columns: box_number, box_type, box_location, insurance_company")

class bupsegre(forms.Form):
    csv_file = forms.FileField(
        help_text="Deras Kindly upload the provider sheet to be processed"
    )
    
class bursegre(forms.Form):
    csv_file = forms.FileField(
        help_text="Deras Kindly upload the reimbursement sheet to be processed"
    )
    
class bdb(forms.Form):
    file = forms.FileField(label="Upload CSV File")

class bdr(forms.Form):
    file = forms.FileField(label="venom")


############# box_stats_repo ###########
class BoxStatsReportForm(forms.Form):
    locations = forms.ModelMultipleChoiceField(
        queryset=BoxLocation.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )
    # statuses = forms.ModelMultipleChoiceField(
    #     queryset=BoxStatus.objects.all(),
    #     required=False,
    #     widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    # )
    types = forms.ModelMultipleChoiceField(
        queryset=BoxType.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )
    insurance_companies = forms.ModelMultipleChoiceField(
        queryset=InsuranceCompany.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        error_messages={
            'invalid_choice': 'Please select valid insurance companies',
            'invalid_list': 'Invalid insurance company selection'
        }
    )


################ claims per date form ########3
class DateFilterForm(forms.Form):
    DATE_FIELD_CHOICES = [
        ('Receive_date', 'Receive Date'),
        ('Issuance_date', 'Issuance Date'),
        ('Segregation_date', 'Segregation Date'),
        ('Audit_date', 'Audit Date'),
        ('request_date', 'Request Date'),
    ]
    
    EXPORT_FORMATS = [
        ('html', 'Web View'),
        ('csv', 'CSV'),
        ('xlsx', 'Excel (XLSX)'),
    ]

    date_field = forms.ChoiceField(
        choices=DATE_FIELD_CHOICES,
        initial='Segregation_date',
        label='Filter By Date Field'
    )
    start_date = forms.DateField(
        label='Start Date', 
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    end_date = forms.DateField(
        label='End Date', 
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    export_format = forms.ChoiceField(
        choices=EXPORT_FORMATS,
        initial='html',
        label='Export Format'
    )

########### claims by actor form ################

class ActorFilterForm(forms.Form):
    ACTOR_CHOICES = [
        ('Segregation_by', 'Segregated By'),
        ('Audit_by', 'Audited By'),
        ('request_by', 'Requested By'),
    ]
    
    DATE_CHOICES = [
        ('Segregation_date', 'Segregation Date'),
        ('Audit_date', 'Audit Date'),
        ('request_date', 'Request Date'),
    ]
    
    EXPORT_FORMATS = [
        ('html', 'Web View'),
        ('csv', 'CSV'),
        ('xlsx', 'Excel'),
    ]
         
    actor_type = forms.ChoiceField(choices=ACTOR_CHOICES, label='Actor Type')
    date_type = forms.ChoiceField(choices=DATE_CHOICES, label='Date Type')
    actor_query = forms.CharField(label='Actor Name', required=False)
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    export_format = forms.ChoiceField(choices=EXPORT_FORMATS, initial='html')







################## data stagging statging ###################

class SegregationStepForm(forms.ModelForm):
    class Meta:
        model = SegregationStep
        fields = [
            'policy_id_1', 'policy_id_2', 'client_id', 'insurance_company',
            'client_name', 'member_name', 'card_number', 'emp_code',
            'batch_receiving', 'parent_bid', 'batch_type', 'provider_type_name',
            'pid', 'claim_code', 'service_date', 'claim_type',
            'provider_memo_code', 'provider_memo', 'approved_amount', 'deducted_amount'
        ]
        
        widgets = {
            'policy_id_1': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            
            'client_id': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'insurance_company': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'client_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'member_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'card_number': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'emp_code': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'batch_receiving': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'parent_bid': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'batch_type': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'provider_type_name': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'pid': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'claim_code': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'service_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': True}),
            'claim_type': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'provider_memo_code': forms.TextInput(attrs={'class': 'form-control'}),
            'provider_memo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'approved_amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'required': True}),
            'deducted_amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
        }
    
    def clean_approved_amount(self):
        amount = self.cleaned_data.get('approved_amount')
        if amount and amount < 0:
            raise forms.ValidationError("Approved amount cannot be negative.")
        return amount
    
    def clean_deducted_amount(self):
        amount = self.cleaned_data.get('deducted_amount')
        if amount and amount < 0:
            raise forms.ValidationError("Deducted amount cannot be negative.")
        return amount
    
    def clean(self):
        cleaned_data = super().clean()
        approved_amount = cleaned_data.get('approved_amount')
        deducted_amount = cleaned_data.get('deducted_amount')
        
        if approved_amount and deducted_amount:
            if deducted_amount > approved_amount:
                raise forms.ValidationError("Deducted amount cannot be greater than approved amount.")
        
        return cleaned_data
    

class SegreStgCsvForm(forms.Form):
    csv_file = forms.FileField(
        label='Select a CSV file',
        help_text='The file must have mentioneddddd columns.'
    )