from django.shortcuts import redirect
from django.http import HttpResponse
""" This decorator prevents other users to access the allowed groups """ 
def allowed_users(allowed_groups=[]): 
    def decor(view_function):
        def wrapper(request, *args,**kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_groups:
                return view_function(request, *args, **kwargs)
            else:
                return HttpResponse('Unauthorised Access')
        return wrapper
    return decor

def login_excluded(redirect_to):
    """ This decorator kicks authenticated users out of a view """ 
    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to) 
            return view_method(request, *args, **kwargs)
        return _arguments_wrapper
    return _method_wrapper
