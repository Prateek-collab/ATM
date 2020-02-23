class Atm:
                pin=""
                __balance=0    #encapsulation
                __counter=1001

                def __init__(self):
                                self.accno=Atm.__counter
                                self.pin=input("set your new atm pin")
                                print("pin set successfully")
                                print("Your account no is", self.accno)
                                Atm.__counter=Atm.__counter+1

                @staticmethod
                def get_counter():
                                return Atm.__counter

                def get_balance(self):
                                print(self.__balance)
                                
                def set_balance(self,value):
                                if type(value)==int:
                                                self.__balance=value
                                                print("Done")
                                else:
                                                print("Invalid ",value)
                                
                def deposit(self):
                                temp=input("Enter pin")
                                if self.pin==temp:
                                                amount=int(input("Amount to be deposited"))
                                                self.__balance=self.__balance+amount
                                                print("Deposited")
                                else:
                                                print("Incorrect pin")
                def checkBalance(self):
                                temp=input("Enter pin")
                                if self.pin==temp:
                                                print("Your balance is",self.__balance)
                                else:
                                                print("Incorrect pin")
                def withdrawal(self):
                                temp=input("Enter pin")
                                if self.pin==temp:
                                                amount=int(input("Amount to be withdrawn"))
                                                if amount<self.__balance:
                                                                self.__balance=self.__balance-amount
                                                                print("collect your cash")
                                                else:
                                                                print("not enough balance")
                                else:
                                                print("Incorrect pin")
                                                
                                
                                
