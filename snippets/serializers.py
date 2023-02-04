from rest_framework import serializers
from snippets.models import Snippet, Author
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = '__all__'

# Storing the owner field as a readOnly field and not as an object
#ReadOnlyField only read and stores the username of the owner out of the user object
class SnippetSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')
  class Meta:
    model = Snippet
    fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
  snippets = SnippetSerializer(Snippet.objects.all(), many= True)
  class Meta:
    model = User
    fields = ["id", 'username', 'snippets']