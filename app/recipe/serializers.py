"""
Serializers for recipe APIS
"""

from core.models import Recipe
from rest_framework import serializers


class RecipeDetailSerializer(serializers.ModelSerializer):
    """Serializer for recipes"""

    class Meta:
        model = Recipe
        fields = ["id", "title", "time_minutes", "price", "link"]
        read_only_fields = ["id"]
