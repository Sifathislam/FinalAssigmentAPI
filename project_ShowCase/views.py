from django.shortcuts import render
from rest_framework import viewsets,filters, pagination
from . import models
from . import serializers
# Create your views here.
class ProjectPagination(pagination.PageNumberPagination):  
    page_size = 6
    page_size_query_param = page_size
    max_page_size = 100


class ProjectDetailsViewSet (viewsets.ModelViewSet):
    queryset = models.ProjectDetailsModel.objects.all()
    serializer_class = serializers.ProjectDetailsSerializer
    pagination_class = ProjectPagination

class ProjectImageViewSet(viewsets.ModelViewSet):
    queryset = models.ProjectImage.objects.all()
    serializer_class = serializers.ProjectImageSerializer
  
class TechStakViewSet(viewsets.ModelViewSet):
    queryset = models.TechStack.objects.all()
    serializer_class = serializers.TechStackSerializer
  
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
  
class RatingsViewSet(viewsets.ModelViewSet):
    queryset = models.Ratings.objects.all()
    serializer_class = serializers.RatingSerializer
  