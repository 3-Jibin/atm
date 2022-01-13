import json

from log import user_bala,new_balance

class Withdraw:

    def draw_amount(self,id):
        withdr = int(input("Enter the amount to WithDraw  :"))

        items = user_bala()
                    
        for item in items:
            if item['user_id'] == id:

                balance = item['amount']

                sub = balance - withdr

                item['amount'] = sub

                new_balance(items)




        return sub


