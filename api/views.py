from rest_framework import status
from rest_framework.views import APIView
from api.serializers import QuoteSerializer
from utils.response import Response

# Create your views here.

class QuoteView(APIView):

    def post(self, request):
        serializer = QuoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'quotes': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
