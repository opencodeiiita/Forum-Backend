from rest_framework import views, status
from rest_framework.response import Response
from accounts.serialzers import ChangePasswordSerializer
from django.contrib.auth.models import User
from rest_framework.generics import UpdateAPIView
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist   
class ChangePasswordView(UpdateAPIView):
        serializer_class = ChangePasswordSerializer
        model = User
        def update(self, request, *args, **kwargs):
            self.object = self.request.user
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'message': 'Password updated successfully',
                }
                return Response(status= status.HTTP_200_OK, data = response)
            return Response(status=status.HTTP_400_BAD_REQUEST)


def logout_view(request):
    if request.method == "GET":
        res = {'message': 'Logged out successfully',}
        logout(request)
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass
        return Response(status = status.HTTP_200_OK)
    return Response(status = status.HTTP_400_BAD_REQUEST, data = res)
