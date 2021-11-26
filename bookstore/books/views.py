from books.models import Book
from books.serializers import BookSerializer, MutableBookSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class BookViewSet(ModelViewSet):
    permission_classes = []
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get_serializer_class(self):
        return MutableBookSerializer

    def perform_create(self, serializer):
        serializer.save()

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)
