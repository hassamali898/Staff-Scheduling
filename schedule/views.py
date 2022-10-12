
from rest_framework import generics, permissions
# Create your views here.
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from schedule.serializers import ScheduleSerializer
from schedule.models import Schedule
from user.models import User

class GetUserSchedule(generics.GenericAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = ScheduleSerializer

    def get(self, request, *args, **kwargs):
        data = Schedule.objects.filter(user=request.user.username)
        return Response({
            "data": ScheduleSerializer(data, many=True).data,
        })

    def post(self, request, *args, **kwargs):
        if(request.user.role == 'ADMIN'):
            user = User.objects.get(username=request.data['user'])
            if not user:
                return Response({
                    "message": "User not found",
                })
            data = Schedule.objects.filter(room=request.data['room'],
                building=request.data['building'],
                start_time__gte=request.data['start_time'],
                end_time__lte=request.data['end_time']
                )
            if not data:
                serializer  = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({'message': 'Schedule created'})
            else:
                return Response({'message': 'Schedule already exists'})

        return Response({
            "message": "Please login as admin",
        })