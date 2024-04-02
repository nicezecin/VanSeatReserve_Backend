from rest_framework import viewsets
from .models import User
from .serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        username = self.request.query_params.get("username")
        role = self.request.query_params.get("role")
        firstName = self.request.query_params.get("firstName")
        lastName = self.request.query_params.get("lastName")


        if username:
            queryset = queryset.filter(username__icontains=username)
        if role:
            queryset = queryset.filter(role__icontains=role)
        if firstName:
            queryset = queryset.filter(firstName__icontains=firstName)
        if lastName:
            queryset = queryset.filter(lastName__icontains=lastName)
            
        return queryset
    
    def get_queryset(self):
        queryset = AddRoutes.objects.all()
        startRoute_id = self.request.query_params.get("startRoute_id")
        endRoute_id = self.request.query_params.get("endRoute_id")
        date = self.request.query_params.get("date")

        if startRoute_id:
            queryset = queryset.filter(startRoute_id=startRoute_id)
        if endRoute_id:
            queryset = queryset.filter(endRoute_id=endRoute_id)
        if date:
            queryset = queryset.filter(date__icontains=date)
            
        return queryset
