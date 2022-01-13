import json
from log import user_data


class BackEnd:


    def check(self,user_id,pin):
        
        
        a = user_data()
        

        

        try:

            if next(x for x in a if (x["user_id"] == user_id and x["password"] == pin)):

                return True
                

        except StopIteration :

            print("Error!!")

            

        





    





    

    

    