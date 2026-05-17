# challenge level 

class ATM_simulator:
   
  carddic = {65261645: 18122006, 12345678: 123456}
  balance_check ={65261645: 1000000, 12345678: 50000}

  def card_details (self):
   try: 
     self.card_info = int(input("Please enter you card detials : "))

     if self.card_info in self.carddic:
       self.cardsave = self.card_info
       print(f"Your card number is : {self.cardsave}\n")
     
       self.pin_info = int(input("please enter you pin detials : "))

       if self.pin_info == self.carddic[self.card_info]:
         print(f"Your pin is correct!")
         print("=================================\n")
         return self.cardsave
       else:
        print("Incorrect PIN! ")
        return None
     else:
      print(" You need to visit bank we cann't find details provied by user.....!")
      return None
     
   except ValueError:
     print("Please enter a valid card number!")
     return None 
     

  def check_balance(self):
   
    card_numder = self.cardsave
    balance = self.balance_check[card_numder]

    print("====================================\n")
    print(f"Your bank balance is {balance}")
    print("press any key for continue.....")
    print("=====================================\n")

 

  def withdraw_cash(self):
    try:
     amount = int(input("Enter amount to withdraw :"))
     if amount <= 0:
        print("Amount must be positive!")
        return
                
      # Add validation for multiples of 100 (common ATM rule)
     if amount % 100 != 0:
        print("Amount must be in multiples of 100!")
        return

     card_numder = self.cardsave
     balance = self.balance_check[card_numder]
     if amount > balance:
          print("Insufficient balance!")
          print(f"Your current balance: Rs. {balance}")
          return
       
     print("======================\n")
     print("processing.....")
     print("Please take your cash"  )

     available =  balance - amount
     self.balance_check[card_numder] = available

     print("Withdraw successful")
     print(f"New Balance : RS. {available}")
     print("=========================\n")

    except ValueError :
        print("Please enter a valid amount!")


  def Deposit(self):
    try:
     amount = int(input("Enter amount to Deposit :"))
     
     if amount <= 0:
        print("Amount must be positive!")
        return
                
     if amount > 100000:  # Optional: Add deposit limit
       print("Maximum deposit limit is Rs. 100,000!")
       return
     
     card_numder = self.cardsave
     balance = self.balance_check[card_numder]

     print("========================\n")
     print("processing.....")
     print("Please insert your cash")

     available = balance + amount
     self.balance_check[card_numder] = available

     print("Deposit successful")
     print(f"New Balance : RS. {available}")
     print("==========================\n")

    except ValueError:
        print("Please enter a valid amount!")

  def change_pin(self):
    try:
       
      enter_pin = int(input("Enter your current Pin : "))
      card_number = self.cardsave

      if enter_pin == self.carddic[card_number]:
       print("your Pin is correct..... now change it ")

       new_pin = int(input("Enter your new PIN : "))

       if len(str(new_pin)) != 6:
         print("PIN must be 6 digits!")
         return
       
       confirm_pin = int(input("Re-enter your PIN : "))

       if new_pin == confirm_pin:
         self.carddic[card_number] = new_pin
         print("="*30)
         print("Now your pin is change successfully! ")
         print(f" Now the current PIN is : {self.carddic[card_number]}")
         print ("="*30)

       else:
         print("Pin does not match .... try again ")

      else:
       print("you Pin in invaild please check it first ! ")

    except ValueError:
           print("Please enter numbers only!")

        

  def menu (self):
    while True:
      print("\n" + "="*30)
      self.title ="WELCOME TO ATM SERVICES"
      print(self.title.center(20))
      print("="*30)
     
      print("\n1. Insert card")
      print("2.Exit")
      try:
        initial_choice = int(input("Enter Your Choice : "))

        if initial_choice == 1 :
          self.card_input = self.card_details()

          if self.card_input in self.carddic:
            self.show_opretion_menu()
          else:
            print("Access decline . Please try again.")
        
        elif initial_choice == 2:
          print("Thank you for useing ATM . Goodbye! ")
          break

        else:
          print("Invalid chioce ! please enter 1 or 2 .")
      except ValueError:
        print("Please enter a vaild number!")

  def show_opretion_menu(self):
    while True:    
     print("Main menu:")
     print("1. check balance ")
     print("2. Withdraw Cash ")
     print("3. Deposit Cash")
     print("4. Change PIN")
     print("5. Exit\n")
     print("==========================")
     try:
        choice = int(input("Enter your choice : "))

        if choice == 1 :
         self.check_balance()
        elif choice == 2 :
         self.withdraw_cash()
        elif choice == 3 :
         self.Deposit()
        elif choice == 4 :
         self.change_pin()
        elif choice == 5:
         print("Thank you for using ATM. Goodbye!")
         break

        else:
          print("Invalid choice! Please enter 1-5.")
     except ValueError:
         print("Please enter a valid number!")



if __name__ == "__main__":
    kunj = ATM_simulator()
    kunj.menu()


