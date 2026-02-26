from app1.models import Drink
from app1.serializers import DrinkSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
# passing format=None would help us to 
# view the objects in json format
def drinkList(request, format=None): 
    
    if request.method == 'GET':
        # get all the drinks
        # serialize them
        # return json
        drinks = Drink.objects.all()
        serializer = DrinkSerializers(instance=drinks, many=True)
        return Response(serializer.data)

    
    if request.method == 'POST':
        # take the data they sent us
        # deserialize the coming data
        # create drink object out of it
        serializer = DrinkSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def drinkDetail(request, id, format=None):
    # get object if exist's
    # else return DoesNotExist
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # simply GET object
    if request.method == 'GET':
        serializer = DrinkSerializers(drink)
        return Response(serializer.data)
    
    # update or completely replace existing object
    elif request.method == 'PUT':
        serializer = DrinkSerializers(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # delete an existing object
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
