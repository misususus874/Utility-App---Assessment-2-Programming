print('***********************************************************')
print('                 VENDING MACHINE     ')
print('               ------ MENU ------    ')
print('\n(A1): Water - $1.00   (A2): Strawberry Milk - $2.00\n'
      '(A3): Banana Milk - $1.00    (A4): Canned Coffee - $2.00\n'
      '(A5): Pocky - $4.00   (B1): Dango - $2.00\n'
      '(B2): Japanese Cheesecake - $5.00    (B3): Takoyaki - 3.00\n'
      '(B4): Melon Bun - $2.50   (B5): Strawberry Sandwich - $3.00' )
print('\n***********************************************************')
#A menu display where the user can choose from


class VendingMachine:
    def __init__(self):
        self.menu = {
            'A1': ('Water', 1.00),
            'A2': ('Strawberry Milk', 2.00),
            'A3': ('Banana Milk', 1.00),
            'A4': ('Canned Coffee', 2.00),
            'A5': ('Pocky', 4.00),
            'B1': ('Dango', 2.00),
            'B2': ('Japanese Cheesecake', 5.00),
            'B3': ('Takoyaki', 3.00),
            'B4': ('Melon Bun', 2.50),
            'B5': ('Strawberry Sandwich', 3.00)
        }
#The menu is a dictionary containing tuples  to access items easily through code
    def payment(self):
        while True:
            try:
                amount = float(input('\nInsert money: $'))
                if amount <= 0:
                    print('Please insert a valid amount.')
                    continue #loops back to the input function
                else:
                    return amount
            except ValueError:
                print('Please insert a valid amount.')
#The payment method is for the user to enter an amount to buy an item
#This amount will be returned to buy an item after their selection
    def selection(self):
        while True:
            code = input('Enter a code from the menu: ').upper()
            if code in self.menu:
                name, price = self.menu[code] #tuple unpacking
                self.name = name
                self.price = price
                print(f'Selected: {name} - ${price:.2f}')
                return name, price
            else:
                print('Invalid code')
                continue
#The selection method is where the user inputs a code from the menu
#This is where tuple unpacking happens to retrieve the name and price for later printed messages and calculation
    def process_purchase(self):
        while True:

            money = self.payment()
            self.selection()
            #This is where the methods above are called

            if money < self.price:
                print('\nInsufficient amount of money')
                print('Returning Money. . . . . . ')
                break

            change = money - self.price
            #subtracting change


            print(f'\nDispensing {self.name}. . .')
            print(f'{self.name} dispensed!')
            print(f'\nYour change is ${change:.2f}')

            while True:
                purchase_again = input('Would you like to purchase again? (y/n): ').lower()
                if purchase_again == 'y':
                    break
                elif purchase_again == 'n':
                    print('Thank you for purchasing!')
                    return
                else:
                    print('Please enter a valid option')
            #This loop is specifically for the option to purchase more items
#The process_purchase method is where a successful purchase is completed but also where the user can buy more items
machine = VendingMachine()
machine.process_purchase()


