import json
from login import Login
from userbalance import CheckBalance
from deposite import Deposite
from withdraw import Withdraw


class FrontPage:

    def log_page(self):


        l = Login()

        global uid 
        uid = l.datas()
        c = l.data()
        

        if c == True:
            f.menu()       


  
        
    def menu(self):

        x = int(input("""1. DEPOSITE
        
        2.  WITHDRAW
        
        3. BALANCE  """))


        if x == 1:

            d = Deposite()
            current_balance = d.dep_amount(uid)
            print("Balance :",current_balance)



        if x == 2:

            wd = Withdraw()
            bala = wd.draw_amount(uid)

            print("Balance :",bala)

        
        
        
        elif x == 3:

            cb = CheckBalance()

            cb.balancee(uid)
        
        
f = FrontPage()
f.log_page()




    


        




                















