import requests
import json
from django.conf import settings
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class DotNetApiService:
    def __init__(self):
        # Add this to your Django settings.py
        self.base_url = getattr(settings, 'DOTNET_API_BASE_URL', 'https://localhost:7000/api')
        self.timeout = getattr(settings, 'DOTNET_API_TIMEOUT', 30)
    
    def send_reimbursement_data(self, provider_segregation_instance):
        """
        Send provider segregation data to .NET API
        """
        try:
            # Map Django model fields to .NET model
            payload = {
                'claimCode': getattr(provider_segregation_instance, 'claim_code', ''),
                'batchNum': getattr(provider_segregation_instance, 'batch_number', ''),
                'batchType': getattr(provider_segregation_instance, 'batch_type', ''),
                'englishName': getattr(provider_segregation_instance, 'english_name', ''),
                'arabName': getattr(provider_segregation_instance, 'arab_name', ''),
                'payer': getattr(provider_segregation_instance, 'payer', ''),
                'policy': str(provider_segregation_instance.PolicyId.id) if provider_segregation_instance.PolicyId else '',
                'hof': getattr(provider_segregation_instance, 'hof', ''),
                'auditUser': provider_segregation_instance.created_by.username if provider_segregation_instance.created_by else '',
                'boxNumberId': provider_segregation_instance.box_number.id if provider_segregation_instance.box_number else 0,
                'createdBy': provider_segregation_instance.created_by.id if provider_segregation_instance.created_by else None,
                'updateById': None  # Set if you have update functionality
            }
            
            headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
            
            # Add authentication if needed
            api_key = getattr(settings, 'DOTNET_API_KEY', None)
            if api_key:
                headers['Authorization'] = f'Bearer {api_key}'
            
            url = f"{self.base_url}/reimbursement"
            
            logger.info(f"Sending data to .NET API: {url}")
            logger.debug(f"Payload: {json.dumps(payload, indent=2)}")
            
            response = requests.post(
                url,
                json=payload,
                headers=headers,
                timeout=self.timeout,
                verify=True  # Set to False for development with self-signed certificates
            )
            
            response.raise_for_status()
            
            result = response.json()
            logger.info(f"Successfully sent data to .NET API. Response: {result}")
            
            return {
                'success': True,
                'data': result,
                'status_code': response.status_code
            }
            
        except requests.exceptions.Timeout:
            logger.error("Timeout when calling .NET API")
            return {
                'success': False,
                'error': 'API request timed out',
                'status_code': None
            }
            
        except requests.exceptions.ConnectionError:
            logger.error("Connection error when calling .NET API")
            return {
                'success': False,
                'error': 'Could not connect to .NET API',
                'status_code': None
            }
            
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP error when calling .NET API: {e}")
            error_detail = "Unknown error"
            try:
                error_detail = response.json().get('message', str(e))
            except:
                error_detail = str(e)
                
            return {
                'success': False,
                'error': f'API error: {error_detail}',
                'status_code': response.status_code
            }
            
        except Exception as e:
            logger.error(f"Unexpected error when calling .NET API: {e}")
            return {
                'success': False,
                'error': f'Unexpected error: {str(e)}',
                'status_code': None
            }