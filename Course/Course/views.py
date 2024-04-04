from django.shortcuts import render
from .models import Course
from .serializers import CourseSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404


class courseListView(APIView):
    def get(self,request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    

class courseDetailView(APIView):
    def get_course(self,pk):
        try:
            return Course.objects.get(pk = pk)
        except Course.DoesNotExist:
            raise Http404
            
    def get(self,request,pk):
        courses = self.get_course(pk)
        print(courses)
        serializer = CourseSerializer(courses)
        return Response(serializer.data)
    
    def delete(self,request,pk):
        self.get_course(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self,request,pk):
        courses= self.get_course(pk)
        serializer = CourseSerializer(courses,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)