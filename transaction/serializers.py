from rest_framework import serializers
from . models import Transaction
from account.models import UserAccount
from pet.models import Pet
from . constants import TRANSACTION_TYPE
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

