from django.forms import ValidationError
from arcapp.models import Box, master_data, BoxType,BoxLocation, InsuranceCompany  # import master_data model
from django.db import transaction
import csv


class BoxProcessor:
    def __init__(self):
        self.updated_count = 0
        self.errors = []

    def process_csv(self, csv_file):
        try:
            csv_data = csv.DictReader(csv_file.read().decode('utf-8').splitlines())
            with transaction.atomic():
                self._process_rows(csv_data)
        except Exception as e:
            self.errors.append(f"CSV processing failed: {str(e)}")
        return self.updated_count, self.errors

    def _process_rows(self, csv_data):
        for row_idx, row in enumerate(csv_data, 1):
            try:
                self._process_row(row_idx, row)
            except Exception as e:
                self.errors.append(f"Row {row_idx}: Unexpected error - {str(e)}")

    def _process_row(self, row_idx, row):
        # This method must be here, indented correctly!
        box_number = row.get('box_number')
        if not box_number:
            self.errors.append(f"Row {row_idx}: Missing box_number")
            return

        try:
            box = Box.objects.get(box_number=box_number)
            updated = False

            for field in row:
                if field == 'box_number':
                    continue

                value = row[field].strip()
                if not value:
                    continue

                try:
                    if field == 'box_type':
                        related_obj = BoxType.objects.get(name__iexact=value)
                        setattr(box, field, related_obj)
                        updated = True
                    elif field == 'box_location':
                        related_obj = BoxLocation.objects.get(name__iexact=value)
                        setattr(box, field, related_obj)
                        updated = True
                    # elif field == 'box_status':
                    #     related_obj = BoxStatus.objects.get(name__iexact=value)
                    #     setattr(box, field, related_obj)
                    #     updated = True
                    elif field == 'insurance_company':
                        related_obj = InsuranceCompany.objects.get(name__iexact=value)
                        setattr(box, field, related_obj)
                        updated = True
                    elif hasattr(box, field):
                        setattr(box, field, value)
                        updated = True
                except BoxType.DoesNotExist:
                    self.errors.append(f"Row {row_idx}: '{value}' not found in Box Type for {field}")
                    continue
                # except BoxStatus.DoesNotExist:
                #     self.errors.append(f"Row {row_idx}: '{value}' not found in Box Status for {field}")
                #     continue
                except BoxLocation.DoesNotExist:
                    self.errors.append(f"Row {row_idx}: '{value}' not found in Box Location for {field}")
                    continue
                except InsuranceCompany.DoesNotExist:
                    self.errors.append(f"Row {row_idx}: '{value}' not found in Insurance Company for {field}")
                    continue

            if updated:
                try:
                    box.full_clean()
                    box.save()
                    self.updated_count += 1
                except ValidationError as e:
                    self.errors.append(f"Row {row_idx}: Validation error - {', '.join(e.messages)}")
                except Exception as e:
                    self.errors.append(f"Row {row_idx}: Save error - {str(e)}")

        except Box.DoesNotExist:
            self.errors.append(f"Row {row_idx}: Box {box_number} not found")
        except Exception as e:
            self.errors.append(f"Row {row_idx}: {str(e)}")
