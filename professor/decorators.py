# decorators.py
from django.shortcuts import redirect

def logout_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('professor:dashboard')  # Redirect authenticated users to the dashboard
        return view_func(request, *args, **kwargs)
    return _wrapped_view
