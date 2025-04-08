from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import CustomUser
from .serializers import UserSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.AllowAny()]  # همه می‌تونن ثبت‌نام کنن
        return [permissions.IsAdminUser()]  # فقط ادمین‌ها لیست کاربران رو ببینن
    
class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user