from rest_framework import serializers
from . models import Transaction
from account.models import UserAccount
from pet.models import Pet
from . constants import TRANSACTION_TYPE
from django.db import transaction
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['account', 'amount']
        read_only_fields = ["balance_after_transaction", "transaction_type"]
    
    def validate_account(self, value):
        try:
            account = UserAccount.objects.get(id=value.id)
        except UserAccount.DoesNotExist:
            raise serializers.ValidationError({'error' : 'Account does not exist'})
        return account
    def validate_amount(self, value):
        min_deposit_amount = 100
        
        if value > min_deposit_amount:
            return value
        else:
            raise serializers.ValidationError(f'Minimum deposit amount is {min_deposit_amount}')
        return value
    
    def create(self, validated_data):
        account = validated_data['account']
        amount = validated_data['amount']
        
        current_balance = account.balance
        new_balance = current_balance + amount
        
        account.balance = new_balance
        validated_data['transaction_type'] = 'Deposit'
        account.save()
        
        transaction = Transaction.objects.create(account=account, amount=amount, balance_after_transaction=new_balance)
        print(transaction)
        return transaction

class PetAdoptSerializer(serializers.Serializer):
    pet_id = serializers.IntegerField()
    user_id = serializers.IntegerField()

    def validate(self, data):
        pet_id = data.get("pet_id")
        user_id = data.get("user_id")

        try:
            pet = Pet.objects.get(id=pet_id)
        except Pet.DoesNotExist:
            raise serializers.ValidationError("Invalid pet ID.")

        if pet.adopter:
            raise serializers.ValidationError("This pet has already been adopted.")

        try:
            user_account = UserAccount.objects.get(user_id=user_id)
        except UserAccount.DoesNotExist:
            raise serializers.ValidationError("Invalid user ID or account not found.")

        adopting_cost = pet.price

        if user_account.balance < adopting_cost:
            raise serializers.ValidationError("Insufficient balance to adopt the pet.")

        data["pet"] = pet
        data["user_account"] = user_account
        data["adopting_cost"] = adopting_cost

        return data

    def save(self):
        pet = self.validated_data["pet"]
        user_account = self.validated_data["user_account"]
        adopting_cost = self.validated_data["adopting_cost"]

        with transaction.atomic():
            pet.adopter_id = user_account.user_id
            pet.save()

            user_account.balance -= adopting_cost
            user_account.save(update_fields=["balance"])

            Transaction.objects.create(
                account=user_account,
                amount=adopting_cost,
                balance_after_transaction=user_account.balance,
                transaction_type="Pay",
            )

        return pet