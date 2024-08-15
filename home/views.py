from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Person
from home.serializers import *

@api_view(['GET', 'POST'])
def index(request):
    courses = {
        "course_name" : "Python",
        "learn" : ["flask", "Django", "Tornado", "FastApi"],
        "course_provider" : "Scaler"
    }
    if request.method == "GET":
        print("Get methode")
        return Response(courses)
    elif request.method == "POST":
        data = request.data
        print(data)
        print("Post methode")
        return Response(courses)
    

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])    
def person(request):
    if request.method == "GET":
        obj = Person.objects.filter(color__isnull=False)
        serializer = PeopleSerializer(obj, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        data = request.data
        serializer = PeopleSerializer(data= data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == "PUT":
        data = request.data
        serializer = PeopleSerializer(data= data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == "PATCH":
        data = request.data
        obj = Person.objects.get(id = data["id"])
        serializer = PeopleSerializer(obj, data= data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        data = request.data
        obj = Person.objects.get(id = data["id"])
        obj.delete()
        return Response({"message" : "Person deleted"})
