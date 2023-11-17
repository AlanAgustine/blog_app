from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from blog.serializer import blogSerializers
from blog.models import blogModel
from blog.serializer import userSerializers
from blog.models import userModel
from django.db.models import Q
# Create your views here.


@csrf_exempt
def viewBlog(request):
    if request.method == "POST":
        blogtList=blogModel.objects.all()
        serialized=blogSerializers(blogtList,many=True)
        return HttpResponse(json.dumps(serialized.data))
    
@csrf_exempt
def addBlog(request):
    if request.method== "POST":
        recieveddata=json.loads(request.body)
        print(recieveddata)
        serializer_check=blogSerializers(data=recieveddata)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"Success"}))
        else:
             return HttpResponse(json.dumps({"status":"FAiled"}))


@csrf_exempt       
def userBlog(request):
    if request.method == "POST":
        recived_data=json.loads(request.body)
        getuserid=recived_data["user_id"]
        data=list(blogModel.objects.filter(Q(user_id__icontains=getuserid)).values())
        return HttpResponse(json.dumps(data))