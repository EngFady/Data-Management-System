import csv
from datetime import datetime
from django.db import transaction
from arcapp.models import Box, ReimbursementSegregation

# utils/bulk_update_utils.py
def process_reimbursement_csv(csv_file):
    updated_count = 0
    errors = []
    
    try:
        csv_data = csv.DictReader(csv_file.read().decode("utf-8").splitlines())
        
        with transaction.atomic():
            for row_idx, row in enumerate(csv_data, 1):
                try:
                    claim_code = row.get("Claim_Code")
                    box_number = row.get("box_number")
                    
                    if not claim_code:
                        errors.append(f"Row {row_idx}: Missing Claim_Code")
                        continue
                        
                    # Try to find existing record by Claim_Code
                    try:
                        obj = ReimbursementSegregation.objects.get(Claim_Code=claim_code)
                        existing = True
                    except ReimbursementSegregation.DoesNotExist:
                        existing = False
                    
                    # Handle box_number logic
                    if existing:
                        # Update existing record: box_number is optional
                        if box_number:
                            try:
                                new_box = Box.objects.get(box_number=box_number)
                                obj.box_number = new_box
                            except Box.DoesNotExist:
                                errors.append(f"Row {row_idx}: Box {box_number} not found")
                                continue
                    else:
                        # New entry: box_number is required
                        if not box_number:
                            errors.append(f"Row {row_idx}: Missing box_number for new entry")
                            continue
                        try:
                            box = Box.objects.get(box_number=box_number)
                        except Box.DoesNotExist:
                            errors.append(f"Row {row_idx}: Box {box_number} not found")
                            continue
                    
                    defaults = {}
                    for field in row:
                        if field in ["box_number", "Claim_Code"]:
                            continue  # Already processed
                        value = row[field].strip()
                        if value:
                            try:
                                if field == "Audit_date":
                                    defaults[field] = datetime.strptime(value, "%Y-%m-%d").date()
                                else:
                                    defaults[field] = value
                            except ValueError as e:
                                errors.append(f"Row {row_idx}: Invalid format for {field} - {value}")
                                continue
                    
                    if existing:
                        # Update existing object
                        for key, val in defaults.items():
                            setattr(obj, key, val)
                        obj.save()
                        updated_count += 1
                    else:
                        # Create new entry
                        if 'English_name' not in defaults:
                            errors.append(f"Row {row_idx}: Missing required field English_name for new entry")
                            continue
                        ReimbursementSegregation.objects.create(
                            box_number=box,
                            Claim_Code=claim_code,
                            **defaults
                        )
                        updated_count += 1
                        
                except Exception as e:
                    errors.append(f"Row {row_idx}: {str(e)}")

        return updated_count, errors
    except Exception as e:
        errors.append(f"CSV processing failed: {str(e)}")
        return 0, errors