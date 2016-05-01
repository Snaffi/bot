import rmr.views
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


def user_to_json(user: User):
    return {
        'id': user.id,
        'email': user.email,
        'username': user.username,
        'last_name': user.last_name,
        'first_name': user.first_name,
        'url': reverse('user_details', kwargs={'user_id': user.id})
    }


class UserList(rmr.views.Json):

    def get(self, request):
        # users = list()
        # for user in User.objects.all():
        #     users.append(user_to_json(user))

        # users = list()
        # append = users.append
        # for user in User.objects.all():
        #     append(user_to_json(user))

        # users = list(map(user_to_json, User.objects.all()))

        users = [user_to_json(user) for user in User.objects.all() if user.is_active]

        return {
            'users': users,
        }

    def post(self, request):
        username = request.POST.get('username')
        if username is None:
            raise rmr.ClientError(
                'error',
                code='username_required'
            )

        password = request.POST.get('password')
        if password is None:
            raise rmr.ClientError(
                'error',
                code='password_required'
            )

        user = User.objects.filter(username=username).first()
        if user:
            raise rmr.ClientError(
                'error',
                code='user_with_username_exists'
            )

        email = request.POST.get('email', '')
        user = User.objects.filter(email=email).first()
        if user:
            raise rmr.ClientError(
                'error',
                code='user_with_email_exists'
            )
        user = User(
            email=email,
            username=username,
            first_name=request.POST.get('first_name', ''),
            last_name=request.POST.get('last_name', ''),
        )

        user.set_password(password)
        user.save()
        return {
            'user': user_to_json(user)
        }

    # @classmethod
    # def foo(cls, buzz): pass
    #
    # @staticmethod
    # def bla(): pass


class Auth(rmr.views.Json):
    def post(self, request):
        username = request.POST.get('username')
        if username is None:
            raise rmr.ClientError(
                'error',
                code='username_required'
            )

        password = request.POST.get('password')
        if password is None:
            raise rmr.ClientError(
                'error',
                code='password_required'
            )

        user = authenticate(username=username, password=password)
        if user is None:
            raise rmr.ClientError(
                'error',
                code='user_not_found'
            )

        login(request, user)
        return user_to_json(user)


def user_details(request, user_id: int):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    else:
        raise Exception()

    return JsonResponse(
        {
            'data': {
                'user': user_to_json(get_object_or_404(User, pk=user_id))
            }
        }
    )

#
# def foo(buzz, aaa=None, bbb=None, aaaa=None):
#     pass
#
# params = {
#     'buzz': 12322
# }
#
# foo(**params)
