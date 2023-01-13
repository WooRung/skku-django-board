from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Students
from .serializers import StudentSerializer


@api_view(['GET'])
def StudentView(request):
   qs = Students.objects.all()
   serializer = StudentSerializer(qs, many=True)
   return Response(serializer.data)
