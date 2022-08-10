from django.shortcuts import render  # noqa
from django.http import HttpResponse
import boto3

# Create your views here.


def index(request):
    return HttpResponse("Hello Django!")


def Upload(request):
    s3 = boto3.resource("s3")
    file = request.FILES["file"]
    s3.Bucket("todol").put_object(Key=file.name, Body=file)
    return HttpResponse("Uploaded")


def Read(request):
    s3 = boto3.resource("s3")
    obj = s3.Object("todol", "test.txt")
    return HttpResponse(obj.get()["Body"].read().decode("utf-8"))
