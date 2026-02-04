from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import ProductSerializer
from . import Services as services

class ProductViewSet(viewsets.ModelViewSet):
    queryset = services.get_all_products()
    serializer_class = ProductSerializer

    def create(self,request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        try:
            new_product = services.create_new_product(
                name=data['name'], 
                description=data['description'], 
                price=data['price'], 
                image_url=data.get('imageUrl')
            )
            
            response_serializer = self.get_serializer(new_product)
            
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)    
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

