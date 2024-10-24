from datetime import datetime
from src.exceptions import WithdrawalTimeRestrictionError, InsufficientFundsError

class BankAccount:
    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction('Cuenta Creada')

    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, 'a') as f:
                f.write(f'{message}\n')

    def deposit(self, amount):
        if amount < 0:
            raise ValueError('Deposito con saldo negativo')
        if amount > 0:
            self.balance += amount
            self._log_transaction(f'Deposited {amount}. New balance: {self.balance}')
        return self.balance 

    def withdraw(self, amount):
        now = datetime.now()
        if now.hour < 8 or now.hour > 17:
            raise WithdrawalTimeRestrictionError('withdrawl son permitidos')
        
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Withdrawal of {amount} exceeds balance {self.balance}"
            )

        if amount > 0:
            self.balance -= amount
            self._log_transaction(f'withdraw {amount}. New balance: {self.balance}')
        return self.balance

    def get_balance(self):
        self._log_transaction(f'get_balance. New balance: {self.balance}')
        return self.balance   
    
    def transfer(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print(f'Transferencia de fondos Ok')
        else:
            print(f'el monto {amount} no esta disponible para transferirir. Intenta uno menor')    
        return self.balance       