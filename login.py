from back import BackEnd

class Login:

    
    def datas(self):
        
        
        global uid, p
        uid = input("Enter your user ID   : ")
        p = int(input("Enter your pin   :"))
        return uid
        
    def data(self):
        l = BackEnd()
        a = l.check(uid,p)  
        if a == True:
            return a

             








        







