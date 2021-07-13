from django.shortcuts import get_object_or_404
from rest_framework import status
from api.permissions import IsAdminOrReadOnly
from rest_framework.views import APIView
from api.serializers import QuoteSerializer
from api.models import Quote
from utils.response import Response


class QuoteView(APIView):
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminOrReadOnly]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'quotes': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        quotes = Quote.objects.all().order_by('id')
        serializer = self.serializer_class(quotes, many=True)
        return Response(data={'quotes': serializer.data}, status=status.HTTP_200_OK)


class QuoteDetailView(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request, id):
        quote = get_object_or_404(Quote, id=id)
        serializer = QuoteSerializer(quote)
        return Response(data={'quote': serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id):
        quote = get_object_or_404(Quote, id=id)
        serializer = QuoteSerializer(quote, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'quote': serializer.data}, status=status.HTTP_200_OK)
        return Response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        quote = get_object_or_404(Quote, id=id)
        quote.delete()
        return Response(data={'quote': {}}, status=status.HTTP_204_NO_CONTENT)
