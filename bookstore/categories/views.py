from categories.models import Category
from categories.serializers import CategorySerializer, MutableCategorySerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class CategoryViewSet(ModelViewSet):
    permission_classes = []
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_serializer_class(self):
        return MutableCategorySerializer

    def perform_create(self, serializer):
        serializer.save()

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)
