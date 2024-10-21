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
        if amount > 0:
            self.balance += amount
            self._log_transaction(f'Deposited {amount}. New balance: {self.balance}')
        return self.balance 

    def withdraw(self, amount):
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