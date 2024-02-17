from rest_framework import status
import datetime
from config.helpers.error_response import error_response
from .models import User


class CustomLoginRequiredMixin():

    def dispatch(self,request,*args, **kwargs):
        if 'Authorization' not in request.headers:
            return error_response('please set Auth-Token.', status.HTTP_401_UNAUTHORIZED)
        
        token=request.headers['Authorization']
        now=datetime.datetime.now()
        login_user = User.objects.filter(token = token, token_expires_gt=now)
        if len(login_user) ==[0]:

            return error_response('The totken is invalid or expired.', status.HTTP_401_UNAUTHORIZED)
        request.login_user=login_user(0)
        return super().dispatch(request, *args, **kwargs)


