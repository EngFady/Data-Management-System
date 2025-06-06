from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView
from . import views
from django.contrib.auth.views import PasswordChangeView

urlpatterns = [
    path('box_list', views.box_lists.as_view(), name='box_list'),
    
    path('boxes/new/', views.box_create, name='box_create'),
    path('provider-segregation/new/', views.provider_segregation_create, name='provider_segregation_create'),
    path('reimbursement-segregation/new/', views.reimbursement_segregation_create, name='reimbursement_segregation_create'),
    path('bos', views.box_search, name='search_box'),
    path('bou', views.box_update, name='update_box'),
    # path('bod', views.box_delete, name='delete_box'),
    path('pss', views.provider_search, name='search_provider'),
    path('psu', views.provider_update, name='update_provider'),
    path('psd', views.provider_delete, name='delete_provider'),
    path('rss', views.riem_search, name='search_riem'),
    path('rsu', views.reimbursement_update, name='update_riem'),
    path('rsd', views.riem_delete, name='delete_riem'),



    # path("mcttd", views.provider_segregation_crud),
    # path("mtadd", views.reim_crud),
    path('bib', views.bulk_insert_box, name='upload_csv'),
    # path('na', views.upload_csv, name='upload_csv'),
    path('bip', views.bulk_insert_claims, name='bulk_insert_claims'),
    path('bir', views.reimbursement_insert_claims, name='bulk_insert_reim_claims'),
    path('bub', views.bulk_update_boxes_csv, name='bulk_update_boxes'), 

    path("bupsegre", views.bulk_update_provider, name="bulk_update_provider_segregation"),

    # path("bupsegre", views.bulk_update_provider_segregation, name="bulk_update_provider_segregation"),


    path("bursegre", views.bulk_update_reimbursement_segregation, name="bulk_update_reim_segre"),
    path("bdb", views.bulk_delete_boxes, name = "bulk_delete_boxes"),
    path("bdpsegre", views.bulk_delete_provider_segre, name = 'bulk_delete_claims'),
    path("bdrsegre", views.bulk_delete_riem_segre, name = 'bulk_delete_riem_segre'),
    path('top_deductions', views.data_visuslization, name='top_deductions'),
    path("cr",views.claim_retrieval,name="cl_retrieval"),

    ######## first page ht7wl 3la login #######################

    path('', RedirectView.as_view(url='/users/login/', permanent=False), name='home'),

    path('users/login/', views.login_view, name='login'),

    path('download-reim-sample-sheet/', views.reimbursement_insert_sample_sheet, name='download_reim_sample_sheet'),
    path('download-prov-sample-sheet/', views.provider_insert_by_bulk_sample_sheet, name='download_prov_sample_sheet'),
    path('download-box-sample-sheet/', views.box_insert_by_bulk_sample_sheet, name='download_box_sample_sheet'),
    path('download-box-update-sample-sheet/', views.box_update_by_bulk_sample_sheet, name='download_box_update_sample_sheet'),
    path('download-provider-update-sample-sheet/', views.provider_update_by_bulk_sample_sheet, name='download_provider_update_sample_sheet'),
    path('download-reimbursement-update-sample-sheet/', views.reimbursement_update_sample_sheet, name='download_reimbursement_update_sample_sheet'),
    path('rbdssh', views.generate_sample_bulk_delete_csv, name='reim_bulk_delete_sample_sheet'),
    path("bdbssh", views.generate_sample_bulk_delete_boxes_csv, name = "bulk_ddelete_boxes_sample_sheet"),
    path("bdpsssh", views.generate_sample_bulk_delete_provider_segre_csv, name = "bulk_delete_provider_segregation_sample_sheet"),
    path("deuctions", views.deduct, name = "deduct"),
    path('bod', views.delete_box_by_number, name='delete_box'),

    

    path('password-change/', PasswordChangeView.as_view(template_name='arcapp/users/password_change.html'), name='password_change'),
    path('password_change/', views.custom_password_change_view, name='password_change'),




    #path('box-autocomplete/', views.BoxAutocomplete.as_view(), name='box-autocomplete'),

    
    path('provider-segregation/create/', views.provider_segregation_create, name='provider_segregation_create'),
    path('ajax/get-policy-info/', views.get_policy_info, name='get_policy_info'),
    path('ajax/get-box-details/', views.get_box_details, name='box-details'),

    path('box-autocomplete/', views.box_autocomplete, name='box-autocomplete'),

    path('home', views.home_dashboard, name = 'home_kpi'),


    path('manage-master-data/', views.manage_master_data, name='manage_master_data'),
    path('manage-policies/', views.manage_insurance_policy, name='manage_insurance_policy'),

    path('insurance-policies-vis/', views.view_insurance_policies, name='view_insurance_policies'),

    path('export-policies-csv/', views.export_policies_csv, name='export_policies_csv'),
    path('export-policies-csv/', views.export_policies_csv, name='export_policies_csv'),


    #path('ins-autocomplete/', views.insurance_company_search_request, name='ins-autocomplete'),
    path('insurance-company/search/', views.insurance_company_search_request, name='ins-autocomplete'),
    #path('policid-autocomplete/', views.insurance_policy_search_request, name='policid-autocomplete'),
    path('policyid-autocomplete/', views.policyid_autocomplete, name='policyid-autocomplete'),
    path("inspolic", views.update_insurance_policy, name = 'update_insurance'),
    path('insdel', views.delete_insurance, name = 'ddelete_insurance'),


    path('master-data/list/', views.master_data_list, name='master_data_list'),
    path('master-data/update/<str:model_type>/<int:id>/', views.update_master_data, name='update_master_data'),
    path('master-data/delete/<str:model_type>/<int:id>/', views.delete_master_data, name='delete_master_data'),
    

    path('claims-per-incpolic', views.claims_report, name = 'claims_per_policy_repo'),

    path('claims-per-box/', views.claims_per_box, name = 'claims_per_box'),
    path('download-sample/', views.generate_sample_sheet_claims_per_box, name='generate_sample_sheet'),

    path('claims-per-batch', views.claims_per_batch_report, name = 'claims_per_batch_report'),
    path('claims-per-requestDate', views.claims_per_request_date_report, name = 'claims_per_request_date_report'),
    path('count-per-insurance', views.count_per_insurance_report, name = 'count_per_insurance_report'),
    path('box-stats', views.box_stats_report, name='box_stats_report'), 
    path('claims-per-date/', views.claims_per_date, name='claims_per_date'),
    path('claims-per-actor/', views.claims_per_actor, name='claims_per_actor'),



    #################### data staging ##################لسه مكملتهاش #
    path('seg-step', views.segregation_step_list, name='segregation_step_list'),
    path('create/', views.segregation_step_create, name='segregation_step_create'),
    path('<int:pk>/', views.segregation_step_detail, name='segregation_step_detail'),
    path('<int:pk>/update/', views.segregation_step_update, name='segregation_step_update'),
    path('<int:pk>/delete/', views.segregation_step_delete, name='segregation_step_delete'),


    ##################### claim ret work loads ############

    path('claimret', views.claim_retrieval_workload, name = 'claim_ret'),






]

  