class bank:
    def __init__(self):
        self.cash = 1500
        self.password = 1234
        self.total_amount =1500
        self.cas =0


    def password_(self):
        self.pas = int(input('enter your password \n'))
        return self.pas

    def opration_(self):
        self.opr = input('for cash press c , deposit d , balance b ')
        if self.opr == 'c':
            self.cas = int(input('send needed amount'))
            if self.cas > self.total_amount:
                self.cas = int(input(f'amount is not avabale your ballace is {self.total_amount}send needed amount '))
                self.total_amount = self.total_amount - self.cas
                print(f'your balance  is {self.total_amount}')
            elif self.cas < self.total_amount:

                self.total_amount = self.total_amount - self.cas
                print(f'your balance  is {self.total_amount}')

        elif self.opr == 'd':
           self.amount = int(input('give amount '))
           self.total_amount = self.amount+self.total_amount
           return print(self.total_amount)

        elif self.opr == 'b':
            print(f'balance is {self.total_amount}')

b1 = bank()

if b1.password_() != b1.password:
    for i in range(2):
        b1.password_()
        if b1.pas == b1.password:
            while True:
                b1.opration_()

elif b1.pas == b1.password:
    while True:
        b1.opration_()