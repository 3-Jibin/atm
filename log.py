import json
#import login

def user_data():

        with open('bank.json', 'r') as b:

            json_objects = json.loads(b.read())

            return json_objects


def user_bala():

    with open('balance.json', 'r') as p:

            json_objects = json.loads(p.read())

            return json_objects

def new_balance(new_balances):

    with open("balance.json","w") as b:

        json.dump(new_balances,b,indent = 2)

            



            

        



