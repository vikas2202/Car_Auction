# from django.shortcuts import get_object_or_404, render, redirect
# from .models import Car, Bid
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
# from django.contrib import messages
# from django.utils.timezone import now
# from django.contrib.auth.decorators import login_required
# from django.core.mail import send_mail
# from .models import Car
# from rest_framework import generics, permissions
# from .models import Car, Bid
# from .serializers import CarSerializer, BidSerializer
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# from django.utils.timezone import now



# # Create your views here.
# class CarListAPIView(generics.ListAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer

# class CarDetailAPIView(generics.RetrieveAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer

# class PlaceBidAPIView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request, car_id):
#         car = Car.objects.get(id=car_id)
#         if now() > car.end_auction:
#             return Response({"error": "Auction has ended."}, status=status.HTTP_400_BAD_REQUEST)

#         amount = float(request.data.get("amount"))
#         if amount <= car.starting_bid:
#             return Response({"error": "Bid must be greater than starting bid."}, status=status.HTTP_400_BAD_REQUEST)

#         bid = Bid.objects.create(
#             car=car,
#             user=request.user,
#             amount=amount
#         )
#         return Response(BidSerializer(bid).data, status=status.HTTP_201_CREATED)
    



# # end 
# def home(request):
#     cars = Car.objects.all()
#     return render(request, 'home.html', {"cars": cars})


# def user_login(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
#         user = authenticate(request, username=username, password=password)
        
#         if user:
#             login(request, user)
#             return redirect('home')

#         return render(request, 'login.html', {'error': 'Invalid username or password'})
    
#     return render(request, 'login.html')












# def add_car(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         starting_bid = request.POST.get('starting_bid')
#         end_auction = request.POST.get('auction_end')
#         image = request.FILES.get('image')
#         Car.objects.create(
#             title=title,
#             description=description,
#             starting_bid=starting_bid,
#             end_auction=end_auction,
#             image=image,
#             owner=request.user
#         )
#         return redirect('home')
#     return render(request, 'add_car.html')
# # now add 
# # def about_view(request):
# #     return render(request, 'about.html')

# # def contact_view(request):
# #     return render(request, 'contact.html')

# # def terms_view(request):
# #     return render(request, 'terms.html')

# # def signup(request):
# #     return render(request, 'signup.html')


# def add_car(request):
#     return render(request, 'add_car.html')

# def signup(request):
#     return render(request, 'signup.html')

# def about(request):
#     return render(request, 'about.html')

# def contact(request):
#     return render(request, 'contact.html')

# def terms(request):
#     return render(request, 'terms.html')

# def user_logout(request):
#     logout(request)
#     return redirect('home')

# # end 
# def car_detail(request, ):
#     car = get_object_or_404(Car )
#     context = {
#         'car': car,
#     }
#     return render(request, 'car_detail.html', context)

















# @login_required
# def car_detail(request, id):
#     car = Car.objects.filter(id=id).first()
#     bids = car.bids.all().order_by('amount')
#     remaining_time = max((car.end_auction - now()).total_seconds(), 0)
#     auction_active = remaining_time > 0
#     error_message = None
#     winner = car.winner

#     if not auction_active and bids.exists() and not car.sold:  # Auction has ended
#         winner = bids.order_by('-amount').first().user  # Find the highest bidder
#         car.winner = winner
#         car.sold = True  # Mark the car as sold
#         car.save()

#         # Send email to winner
#         send_mail(
#             subject='Congratulations! You won the auction',
#             message=f'Hi {winner.username},\n\nYou have won the auction for the car "{car.title}".',
#             from_email=None,
#             recipient_list=[winner.email],
#             fail_silently=False,
#         )

#         # Send email to car owner
#         send_mail(
#             subject='Your car has been sold!',
#             message=f'Hi {car.owner.username},\n\nYour car "{car.title}" has been sold to {winner.username}.',
#             from_email=None,
#             recipient_list=[car.owner.email],
#             fail_silently=False,
#         )

#     # Handling POST request for placing bids
#     if request.method == 'POST':
#         if car.sold:  # If the car is sold, prevent further bidding
#             error_message = "This auction has ended. The car has already been sold."
#         elif not auction_active:
#             error_message = "The auction has ended. No more bids are accepted."
#         else:
#             amount = request.POST.get('amount')
#             if float(amount) > car.starting_bid:
#                 Bid.objects.create(
#                     car=car,
#                     user=request.user,
#                     amount=amount
#                 )
#             else:
#                 error_message = f"Your Bid must be higher than ${car.starting_bid:.2f}."

#     context = {
#         'car': car,
#         'bids': bids,
#         'remaining_time': remaining_time,
#         'error_message': error_message,
#         'auction_active': auction_active,
#         'winner': winner,
#     }

#     return render(request, "car_detail.html", context)














from django.shortcuts import get_object_or_404, render, redirect
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Car, Bid
from .serializers import CarSerializer, BidSerializer


# DRF API Views
class CarListAPIView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDetailAPIView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class PlaceBidAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, car_id):
        car = get_object_or_404(Car, id=car_id)
        if now() > car.end_auction:
            return Response({"error": "Auction has ended."}, status=status.HTTP_400_BAD_REQUEST)

        amount = request.data.get("amount")
        if amount is None:
            return Response({"error": "Bid amount required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            amount = float(amount)
        except ValueError:
            return Response({"error": "Invalid bid amount."}, status=status.HTTP_400_BAD_REQUEST)

        if amount <= car.starting_bid:
            return Response({"error": "Bid must be greater than starting bid."}, status=status.HTTP_400_BAD_REQUEST)

        bid = Bid.objects.create(
            car=car,
            user=request.user,
            amount=amount
        )
        return Response(BidSerializer(bid).data, status=status.HTTP_201_CREATED)


# Web Views

def home(request):
    cars = Car.objects.all()
    return render(request, 'home.html', {"cars": cars})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('home')

        return render(request, 'login.html', {'error': 'Invalid username or password'})
    
    return render(request, 'login.html')
def user_logout(request):
    logout(request)
    return redirect('home')

def signup(request):
    return render(request, 'signup.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def terms(request):
    return render(request, 'terms.html')





@login_required
def add_car(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        starting_bid = request.POST.get('starting_bid')
        end_auction = request.POST.get('auction_end')
        image = request.FILES.get('image')
        Car.objects.create(
            title=title,
            description=description,
            starting_bid=starting_bid,
            end_auction=end_auction,
            image=image,
            owner=request.user
        )
        return redirect('home')
    return render(request, 'add_car.html')


@login_required
def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    bids = car.bids.all().order_by('amount')
    remaining_time = max((car.end_auction - now()).total_seconds(), 0)
    auction_active = remaining_time > 0
    error_message = None
    winner = car.winner





    if not auction_active and bids.exists() and not car.sold:
        winner = bids.order_by('-amount').first().user
        car.winner = winner
        car.sold = True
        car.save()

        # Email to winner
        send_mail(
            subject='Congratulations! You won the auction',
            message=f'Hi {winner.username},\n\nYou have won the auction for the car "{car.title}".',
            from_email=None,
            recipient_list=[winner.email],
            fail_silently=False,
        )

        # Email to owner
        send_mail(
            subject='Your car has been sold!',
            message=f'Hi {car.owner.username},\n\nYour car "{car.title}" has been sold to {winner.username}.',
            from_email=None,
            recipient_list=[car.owner.email],
            fail_silently=False,
        )

    if request.method == 'POST':
        if car.sold:
            error_message = "This auction has ended. The car has already been sold."
        elif not auction_active:
            error_message = "The auction has ended. No more bids are accepted."
        else:
            amount = request.POST.get('amount')
            if amount and float(amount) > car.starting_bid:
                Bid.objects.create(
                    car=car,
                    user=request.user,
                    amount=amount
                )
            else:
                error_message = f"Your bid must be higher than ${car.starting_bid:.2f}."

    context = {
        'car': car,
        'bids': bids,
        'remaining_time': remaining_time,
        'error_message': error_message,
        'auction_active': auction_active,
        'winner': winner,
    }
    return render(request, "car_detail.html", context)


