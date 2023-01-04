from rest_framework import views, status, viewsets
from rest_framework.response import Response
from accounts.serialzers import ChangePasswordSerializer,ProfileSerializer
from django.contrib.auth.models import User
from rest_framework.generics import UpdateAPIView
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist   
from accounts.models import Profile
from django.shortcuts import get_object_or_404

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


class UserProfile(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    
    def list(self, request):
        queryset = Profile.objects.all()
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Profile.objects.all()
        profile = get_object_or_404(queryset, pk=pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
        
