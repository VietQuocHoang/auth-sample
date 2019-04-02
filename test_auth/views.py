from rest_framework import viewsets
from rest_framework.response import Response


class TestView(viewsets.ViewSet):

    def list(self, request):
        return Response(data={"message": "hello"})


class AdminView(viewsets.ViewSet):

    def list(self, request):
        return Response(data={"message": "hello admin"})

class StaffView(viewsets.ViewSet):

    def list(self, request):
        return Response(data={"message": "hello staff"})
