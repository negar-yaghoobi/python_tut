class Deposit:
    def __init__(self, name, amount=0):
        self.owner = name
        self.amount = amount
    
    def __str__(self):
        return f'Owner: {self.owner} | amount: {self.amount}'
    
    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.owner}, amount={self.amount})'            # ~ f'Deposit(name={self.owner}, amount={self.amount})'
    
    def __add__(self,other):
        new_account = Deposit( f'{self.owner}+{other.owner}',  self.amount + other.amount)
        return new_account
    
    def __iadd__(self, other):
        self.amount += other.amount
        other.amount = 0
        return self

    def __eq__(self, other):              # ~ equal
        return self.amount == other.amount

    def transfer(self, transfer_user, transfer_value):
        if self.amount < transfer_value:
            print('not enough money.')
            return
        
        self.amount -= transfer_value
        transfer_user.amount += transfer_value

        print(f'{self.owner} - {transfer_value} | {transfer_user.owner} + {transfer_value}')
    
    def withdraw(self, withdraw_value):
        if withdraw_value <=0:
            print('amount should be positive.')
            return
        if self.amount < withdraw_value:
            print('not enough money.')
            return
        
        self.amount -= withdraw_value
        print(f'{self.owner} - {withdraw_value}')
    
    def deposit(self, deposit_value):
        if deposit_value <=0:
            print('deposit amount should be positive.')
            return
        
        self.amount += deposit_value
        print(f'{self.owner} + {deposit_value}')


john_dep = Deposit('john', 1000)
david_dep = Deposit('david', 200)

# call __str__
print(john_dep)       # ~ print(str(john_dep))
print(david_dep)

# call __repr__
print(repr(john_dep))
print(repr(david_dep))

# check == between two amount
print(john_dep == david_dep)

# sum two account
print(john_dep + david_dep)

# += between two amount of objects
john_dep += david_dep
print(john_dep)
print(david_dep)

# transfer money
john_dep.transfer(david_dep, 350)

print(john_dep)
print(david_dep)

john_dep.withdraw( 200)

print(john_dep)
print(david_dep)

john_dep.deposit(1300)

print(john_dep)
print(david_dep)