from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


def user_to_json(user: User):
    return {
        'id': user.id,
        'email': user.email,
        'username': user.username,
        'last_name': user.last_name,
        'first_name': user.first_name,
        'url': reverse('user_details', kwargs={'user_id': user.id})
    }
