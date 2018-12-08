from django.core.exceptions import PermissionDenied
from items.models import Item

def user_is_creator(function):
    def wrap(request, *args, **kwargs):
        item = Item.objects.get(pk=kwargs['item_id'])
        if item.user == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap