from django.shortcuts import redirect
from functools import wraps


def verified_email_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated and not user.verified_email:
            return redirect('verify_email')  # Redirect to the email verification page
        return view_func(request, *args, **kwargs)
    return _wrapped_view
