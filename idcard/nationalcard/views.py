from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import  viewsets
from rest_framework import status
from .serializer import *
from .models import *
from django.utils import timezone
import datetime
from rest_framework.decorators import  api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from django.http import HttpResponse
from django.http import HttpRequest
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication,TokenAuthentication,BaseAuthentication

# Create your views here.
@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([AllowAny])
@api_view(['post'])
#1
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = User.objects.create_user(
            email=request.data["email"],
            username=request.data["username"],
            password=request.data["password"],
            
            
            )
        if user is not None:
                user.save()
        info_user = userInfo(user=user,
             national_number=request.data["national_number"],
             phone=request.data["phone"],
             email=request.data["email"],
             username=request.data["username"],
             password=request.data["phone"],
         )
        if info_user:
            info_user.save()
            token =Token.objects.create(user=user)

        return Response(token.key)


#2
@api_view(['POST'])
@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    usre_name = request.data['username']
    password = request.data['password']

    user = authenticate(username=usre_name, password=password)
    if user is not None:
        print(user)
        info= userInfo.objects.get(user_id=user.id)
        return Response({
            'username':info.user.username,
            'fname':info.fName,
            'lname':info.lName,
            'national_number':info.national_number
        })
 #3       
@api_view(['POST'])
def card_info(request):
    # current_user= User.objects.get(id=request.user.id)
    user = User.objects.get(id=request.data["card_user"])

    serializer = CardSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print('33   ')
        card_Instance = card(
            print('666666'),
                        FirstName=request.data["FirstName"],
                        SecondName=request.data["SecondName"],
                        ThirdName=request.data["ThirdName"],
                        FourtName=request.data["FourtName"],
                        Birthdate=request.data["Birthdate"],
                        Placeof_Birth=request.data["Placeof_Birth"],
                        Blood_Type=request.data["Blood_Type"],
                        Center=request.data["Center"],
                        Job=request.data["Job"],
                        Address=request.data["Address"],
                        Phone=request.data["Phone"],
                        Old_id=request.data["Old_id"],
                        card_user=user,)
        print('111111')
        if card_Instance:
            card_Instance.save()
            return Response("done")
 #4

        
@api_view(['POST'])
def Payment_confirmation(request):
        process_number=request.data["process_number"],
        payment_instance = Payment.objects.filter(process_number=process_number)
        data = []
        for x in payment_instance:
            field = {
                "name": x.card.FirstName,
                "payment_date": x.payment_date,
            }
            data.append(field)
        return Response(data)
        

        

        
@api_view(['POST'])
def Payment_infos(request):
    serializer = PaymentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        payment_Instance = Payment(
            payment_Notification=request.FILES["payment_Notification"],
            process_number=request.data["process_number"],
                       )
        if payment_Instance:
            payment_Instance.save()
            return Response("done")

        
 #5       
@api_view(['GET'])
def get_user_request(request):
    cards= card.objects.all()
    if cards is not None:
        myrequest= card.objects.all()
        data =[]
        for x in myrequest:
            field = {
                "FirstName": x.FirstName,
                "SecondName":x.SecondName,
                "ThirdName": x.ThirdName,
                "FourtName": x.FourtName,
            }
            data.append(field)
        return Response(data)
#6
@api_view(['GET'])
def get_user_datails(request):
   details_id=card.objects.all()
   serializer=CardSerializer(details_id,many=True)
   return  Response(serializer.data)

#7
@api_view(['POST','GET'])
def show_my_report(request):
    
    print("FIRST")
    
    if request.method=='GET':
        print("get")
        serializer=reportSerializer()
        return  Response(serializer.data)
    
    
    elif request.method=='POST':
        print("POST")
        serializer=reportSerializer(data=request.data)
        if serializer.is_valid():
            print("valid serializer")
            
            start_date = str(request.data["start_date"])
            end_date = str(request.data["end_date"])
            print(start_date,end_date)
            
            card_instance = card.objects.filter(card_date__gt=start_date,card_date__lt=end_date)
            
            data =[]
            for x in card_instance:
                field = {
                "FirstName": x.FirstName,
                "SecondName"   : x.SecondName
               
            }
            
            
            data.append(field)
        
            return Response(data)
@authentication_classes([TokenAuthentication, BaseAuthentication, SessionAuthentication])
@permission_classes([AllowAny])
@api_view(['POST'])
def get_token(request):
    usre_name = request.data['username']
    password = request.data['password']
    user = authenticate(username=usre_name, password=password)
    if user is not None:
        token = Token.objects.get(user_id=user)
        return Response(token.key)
    else :
       return Response('Incorrect username or password')