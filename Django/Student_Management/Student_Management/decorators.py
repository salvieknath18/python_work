from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied

def role_required(allowed_roles):
    def decor(view_func):
        def wrap(request, *args, **kwargs):
            if request.user.is_authenticated:
                if request.user.profile.profilerole.name in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponseRedirect(reverse('user_logout'))
            else:
                return HttpResponseRedirect(reverse('user_login'))
        return wrap
    return decor
