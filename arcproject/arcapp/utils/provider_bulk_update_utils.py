import csv
from datetime import datetime
from django.db import transaction
from arcapp.models import Box, ProviderSegregation, insurance_policy

def process_provider_segregation_csv(csv_file, request):
    """
    Process a CSV file to update ProviderSegregation records.
    Handles both regular fields and foreign key fields properly.
    """
    updated_count = 0
    errors = []
    
    try:
        decoded_file = csv_file.read().decode("utf-8").splitlines()
        csv_data = csv.DictReader(decoded_file)
        
        # Check required columns
        headers = csv_data.fieldnames
        if 'ClaimCode' not in headers:
            return 0, ["CSV file must contain a 'ClaimCode' column"]
        
        # Process in a transaction to ensure data consistency
        with transaction.atomic():
            for row_num, row in enumerate(csv_data, start=2):  # Start from 2 for header offset
                try:
                    # Get ClaimCode which is required for lookup
                    claim_code = row.get('ClaimCode', '').strip()
                    if not claim_code:
                        errors.append(f"Row {row_num}: Missing ClaimCode")
                        continue
                    
                    # Find the record by ClaimCode
                    try:
                        record = ProviderSegregation.objects.get(ClaimCode=claim_code)
                    except ProviderSegregation.DoesNotExist:
                        errors.append(f"Row {row_num}: Record with ClaimCode '{claim_code}' not found")
                        continue
                    
                    # Prepare data for update
                    regular_updates = {}
                    fk_updates = {}
                    
                    # Process each field
                    for field, value in row.items():
                        # Skip the ClaimCode field and empty values
                        if field == 'ClaimCode' or not value or not value.strip():
                            continue
                        
                        clean_value = value.strip()
                        
                        # Handle special cases for foreign keys
                        if field == 'box_number':
                            try:
                                box = Box.objects.get(box_number=clean_value)
                                # Get the actual DB column name for the foreign key
                                box_column = ProviderSegregation._meta.get_field('box_number').column
                                fk_updates[f"{box_column}_id"] = box.id
                            except Box.DoesNotExist:
                                errors.append(f"Row {row_num}: Box '{clean_value}' not found")
                            continue
                            
                        elif field == 'PolicyId':
                            try:
                                policy_id_int = int(clean_value)
                                policy = insurance_policy.objects.get(policy_id=policy_id_int)
                                # Get the actual DB column name for the foreign key
                                policy_column = ProviderSegregation._meta.get_field('PolicyId').column
                                fk_updates[f"{policy_column}_id"] = policy.id
                            except ValueError:
                                errors.append(f"Row {row_num}: Invalid PolicyId format '{clean_value}'")
                            except insurance_policy.DoesNotExist:
                                errors.append(f"Row {row_num}: Policy '{clean_value}' not found")
                            continue
                        
                        # Skip fields that aren't in the model
                        if not hasattr(record, field):
                            errors.append(f"Row {row_num}: Unknown field '{field}'")
                            continue
                        
                        # Handle different field types
                        try:
                            field_obj = ProviderSegregation._meta.get_field(field)
                            
                            # Process based on field type
                            if field in ['Receive_date', 'Issuance_date', 'Segregation_date', 'Audit_date', 'request_date']:
                                # Handle date fields
                                for fmt in ('%d/%m/%Y', '%Y-%m-%d', '%m/%d/%Y'):
                                    try:
                                        parsed_date = datetime.strptime(clean_value, fmt).date()
                                        regular_updates[field] = parsed_date
                                        break
                                    except ValueError:
                                        continue
                                else:
                                    errors.append(f"Row {row_num}: Invalid date format for {field}: {clean_value}")
                            
                            elif field == "claimscan":
                                # Handle boolean field
                                regular_updates[field] = clean_value.lower() in ['true', 'yes', '1', 't', 'y']
                            
                            elif field == "DeductedAmount" and clean_value:
                                # Handle numeric field
                                regular_updates[field] = float(clean_value)
                            
                            else:
                                # Regular string field
                                regular_updates[field] = clean_value
                                
                        except Exception as e:
                            errors.append(f"Row {row_num}: Error processing {field}={clean_value}: {str(e)}")
                    
                    # Update the record if we have any changes
                    if regular_updates:
                        ProviderSegregation.objects.filter(id=record.id).update(**regular_updates)
                    
                    # Update foreign keys directly in database
                    if fk_updates:
                        ProviderSegregation.objects.filter(id=record.id).update(**fk_updates)
                    
                    # Count as updated if any changes were made
                    if regular_updates or fk_updates:
                        updated_count += 1
                        
                except Exception as e:
                    errors.append(f"Row {row_num}: Unexpected error: {str(e)}")
                    
        return updated_count, errors
        
    except Exception as e:
        errors.append(f"CSV processing failed: {str(e)}")
        return 0, errors