# Add more functionality to the account class

class Account:
    def __init__(self):
        self.debits = []
        self.credits = []
    
    def add_to_debits(self, value):
        self.debits.append(value)
    
    def add_to_credits(self, value):
        self.credits.append(value)
    
    def total_value(self):
        return sum(self.credits) - sum(self.debits)
    
    def check_debits(self):
        print(self.debits)
    
    def transfer(self, other, amount):
        self.add_to_debits(amount) # 내 계좌 지출
        other.add_to_credits(amount) # 상대 계좌 수입
        
my_acc = Account()
your_acc = Account()