class Atm:

    __counter = 1

    def __init__(self):
        self.pin = ''
        self.__balance = 0
        self.cid = Atm.__counter
        Atm.__counter = Atm.__counter + 1
        self.menu()


    def menu(self):
        user_input = input("""
        1. Create Pin
        2. Change Pin
        3. Check Balance
        4. Withdral Amount
        5. Exit
        """)

        if user_input == '1':
            self.create_pin()
            self.menu()
        elif user_input == '2':
            self.change_pin()
            self.menu()
        elif user_input == '3':
            self.check_balance()
            self.menu()
        elif user_input == '4':
            self.withdral_amount()
            self.menu()
        else:
            exit()

    # Utility functions
    @staticmethod
    def get_counter():
        return Atm.__counter

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        if type(new_balance) == 'int':
            self.__balance = new_balance
        else:
            print('Invalid Balance.')

    def _check_access_pin(self):
        status = True
        pin = input('Enter your pin: ')
        if pin != self.pin:
            print('Wrong pin entered')
            status = False
        return status
    

    def create_pin(self):
        pin = input('Enter new pin: ')
        self.pin = pin

        balance = input('Enter your balance: ')
        self.__balance = int(balance)
        print('Pin created successfully.')
        self.menu()

    def change_pin(self):
        status = self._check_access_pin()
        if status:
            new_pin = input('Enter new pin: ')
            self.pin = new_pin        
            print('Pin changed successfully.')

    def check_balance(self):
        status = self._check_access_pin()
        if status:
            print(f'Your Balance: {self.__balance}')

    def withdral_amount(self):
        status = self._check_access_pin()
        if status:
            amount = int(input('Enter amount: '))
            if amount >= self.__balance:
                print('Insufficient Balance')
                return
            self.__balance = self.__balance - amount
            print(f'Withdral Amount: {amount}')

obj = Atm()
