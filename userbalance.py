import json

from log import user_bala

class CheckBalance:


    def balancee(self,id):

        k = user_bala()
            
        for item in k:
            if item['user_id'] == id:

                print((item['amount']))
      



