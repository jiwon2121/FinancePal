from rest_framework import serializers
from .models import Deposit, DepositOption, Saving, SavingOption
from accounts.serializers import UserSerializer

class DepositOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOption
        fields = '__all__'
        read_only_fields = ('product',)


class DepositSerializer(serializers.ModelSerializer):
    user_set = UserSerializer(many=True, read_only=True)
    depositoption_set = DepositOptionSerializer(many=True, read_only=True)
    class Meta:
        model = Deposit
        fields = '__all__'


class SavingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOption
        fields = '__all__'
        read_only_fields = ('product',)


class SavingSerializer(serializers.ModelSerializer):
    user_set = UserSerializer(many=True, read_only=True)
    savingoption_set = SavingOptionSerializer(many=True, read_only=True)
    class Meta:
        model = Saving
        fields = '__all__'