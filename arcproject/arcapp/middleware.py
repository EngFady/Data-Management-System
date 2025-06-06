# In your middleware.py
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta

# class StrictAuthenticationMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
    
#     def __call__(self, request):
#         protected_paths = ['/box_list', '/box_list/', '/bos']
        
#         # Check if path matches protected paths
#         if any(request.path.startswith(path) for path in protected_paths):
#             # Always verify authentication
#             if not request.user.is_authenticated:
#                 return redirect(reverse('login'))
            
#             # Get the session
#             session = request.session
            
#             # Check if session has been idle too long
#             last_activity = session.get('last_activity')
#             if last_activity:
#                 last_activity = timezone.datetime.fromisoformat(last_activity)
#                 idle_time = timezone.now() - last_activity
#                 max_idle = timedelta(minutes=30)  # Customize this timeout
                
#                 if idle_time > max_idle:
#                     # Force logout if idle too long
#                     from django.contrib.auth import logout
#                     logout(request)
#                     request.session.flush()
#                     return redirect(reverse('login'))
            
#             # Update last activity timestamp
#             session['last_activity'] = timezone.now().isoformat()
#             session.modified = True
            
#         response = self.get_response(request)
#         return response



##############   second layer ##############

# class StrictAuthenticationMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
    
#     def __call__(self, request):
#         # Ensure we have the right HTTP_HOST
#         protected_paths = ['/box_list', '/box_list/', '/bos']
#         if not request.META.get('HTTP_HOST'):
#             request.META['HTTP_HOST'] = '192.168.50.56:8000'
        
#         # Debug information
#         print(f"Request path: {request.path}, User authenticated: {request.user.is_authenticated}")
        
#         protected_paths = ['/bl/', '/box_list/']  # Make sure these match your URL patterns exactly
        
#         # Check if path matches protected paths (using exact matching)
#         if any(path == request.path for path in protected_paths) or request.path.startswith('/bl/') or request.path.startswith('/box_list/'):
#             if not request.user.is_authenticated:
#                 print(f"Middleware: Redirecting unauthenticated user from {request.path} to login")
#                 return redirect(reverse('login'))
#             else:
#                 print(f"Middleware: User is authenticated, allowing access to {request.path}")
            
#             # Session management code...
        
#         response = self.get_response(request)
        
#         # Debug redirect information
#         if response.status_code == 302:
#             print(f"Redirect detected from {request.path} to {response.get('Location')}")
        
#         return response


class StrictAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Debug information
        print(f"Request path: {request.path}, User authenticated: {request.user.is_authenticated}")
        
        # Define protected paths - make sure these match exactly what you want to protect
        protected_paths = ['boxes/new/','/boxes/new/','/bos', '/bos/', '/bou', '/bou/', '/bod', '/bod/',
                           '/pss', '/pss/', '/psu', '/psu/', '/psd', '/psd/',
                           '/rss', '/rss/', '/rsu', '/rsu/', '/rsd', '/rsd/',
                           '/bib', '/bib/', '/bip', '/bip/', '/bir', '/bir/',
                           '/bub', '/bub/', '/bupsegre', '/bupsegre/', '/bursegre', '/bursegre/',
                           '/bdb', '/bdb/', '/bdpsegre', '/bdpsegre/', '/bdrsegre', '/bdrsegre/',
                            '/top_deductions', '/top_deductions/', '/cr', '/cr/', '/rbdssh', '/rbdssh/',
                            '/bdbssh', '/bdbssh/', '/bdpsssh', '/bdpsssh/', '/manage-master-data', '/manage-master-data/',
                            '/manage-policies', '/manage-policies/'
                           ]
        
        is_protected_path = request.path in protected_paths or any(
            request.path.startswith(path + '/') for path in protected_paths
        )
        
        if is_protected_path and not request.user.is_authenticated:
            print(f"⚠️ Blocking access to protected path: {request.path}")
            return redirect('login')
        
        if is_protected_path and request.user.is_authenticated:
            pass
        
        response = self.get_response(request)
        
        return response