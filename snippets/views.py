# import json
from django.shortcuts import render
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, AuthorSerializer
from rest_framework.parsers import JSONParser
from snippets.forms import AuthorForm, SnippetForm

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# from django.views.decorators.csrf import csrf_exempt




# Create your views here.

# views to retrieve all snippets and create new
def index(request):
  form = SnippetForm()
  return render(request, 'snippets/index.html', {'form': form})

@api_view(["GET", "POST"])
def all_snippets(request):
  if request.method == 'GET':
    snippets = Snippet.objects.all()
    serializer= SnippetSerializer(snippets,many=True)
    return Response(serializer.data)
      

  if request.method == 'POST':
    serializer = SnippetSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status = status.HTTP_201_CREATED)
  return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def single_snippet(request, pk):
  try:
    snippet = Snippet.objects.get(pk = pk)
  except Snippet.DoesNotExist:
    return Response(status = status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = SnippetSerializer(snippet)
    return Response(serializer.data, status= status.HTTP_200_OK)

  if request.method == 'PUT':
    serializer = SnippetSerializer(snippet, data= request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status= status.HTTP_205_RESET_CONTENT)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

  if request.method == 'DELETE':
    snippet.delete()
    return Response(status= status.HTTP_204_NO_CONTENT)
