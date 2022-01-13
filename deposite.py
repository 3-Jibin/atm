import json
from log import user_bala, new_balance

class Deposite:

    def dep_amount(self,id):

        dep = int(input("Enter the amount to deposite  :"))

        items = user_bala()
            
                    
        for item in items:
            if item['user_id'] == id:

                balance = item['amount']


                sum = balance + dep 

                item['amount'] = sum
                
                new_balance(items)

        


        return sum

        
        


