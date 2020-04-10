from .models import BlogPost
from django.http import Http404


def user_is_entry_author(function):
    def wrap(request, *args, **kwargs):
        entry = BlogPost.objects.get(slug=kwargs['slug'])
        if entry.shop_name == request.user:
            return function(request, *args, **kwargs)
        else:
            raise Http404('hello')
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap