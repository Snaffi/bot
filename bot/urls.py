"""robobot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from bot.views.users import UserList, Auth

urlpatterns = [
    url(r'^users/$', UserList.as_view(), name='user_list'),
    url(r'^users/auth$', Auth.as_view(), name='auth'),
    url(r'^users/(?P<user_id>\d+)/$', 'bot.views.users.user_details', name='user_details')
]
