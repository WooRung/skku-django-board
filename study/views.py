from rest_framework import status
from rest_framework.decorators import api_view, action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import Students, Score
from .serializers import StudentSerializer, ScoreSerializer


# @api_view(['GET', 'POST'])
# def StudentView(request):
#     if request.method == 'GET':
#         qs = Students.objects.all()
#         serializer = StudentSerializer(qs, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentView(APIView):
    """
    GET: 리스트 조회
    POST: 학생 등록
    method에 따라 같은 url(자원)에 다른 요청(함수)
    """

    def get(self, request):
        qs = Students.objects.all()
        serializer = StudentSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Students, pk=pk)

    def get(self, request, pk):
        qs = self.get_object(pk)
        serializer = StudentSerializer(qs)
        return Response(serializer.data)

    def put(self, request, pk):
        qs = self.get_object(pk)
        serializer = StudentSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        qs = self.get_object(pk)
        qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ScoreView(APIView):
    def get(self, request):
        qs = Score.objects.all()
        serializer = ScoreSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#
# class StudentViewSet(viewsets.ViewSet):
#     def get_object(self, pk):
#         return get_object_or_404(Students, pk=pk)
#     def list(self, request):
#         """get /students"""
#         qs = Students.objects.all()
#         serializer = StudentSerializer(qs, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk):
#         """get /students/<pk>"""
#         qs = self.get_object(pk)
#         serializer = StudentSerializer(qs)
#         return Response(serializer.data)
#
#     def create(self, request):
#         """post /students"""
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def update(self, request, pk):
#         """put /students/<pk>"""
#         qs = self.get_object(pk)
#         serializer = StudentSerializer(qs, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def destroy(self, request, pk):
#         """delete /students/<pk>"""
#         qs = self.get_object(pk)
#         qs.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework.decorators import action


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.prefetch_related('score_set').all()
    serializer_class = StudentSerializer

    @action(methods=['GET'], detail=False)
    def seoul(self, request):
        qs = self.get_queryset().filter(address="서울").all()
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
