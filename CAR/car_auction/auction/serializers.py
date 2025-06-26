from rest_framework import serializers
from .models import Car, Bid
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class BidSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Bid
        fields = ['id', 'amount', 'timestamp', 'user']

class CarSerializer(serializers.ModelSerializer):
    bids = BidSerializer(many=True, read_only=True)
    winner = UserSerializer(read_only=True)
    
    class Meta:
        model = Car
        fields = ['id', 'title', 'description', 'starting_bid', 'end_auction', 'image', 'bids', 'winner']
