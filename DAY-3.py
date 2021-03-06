#OOPR-Exer-7
#Start writing your code here
class Ticket:
    counter=0
    def __init__(self,passenger_name,source,destination):
        self.__passenger_name=passenger_name
        self.__ticket_id=None
        self.__source=source
        self.__destination=destination
        
    def get_source(self):
        return self.__source
        
    def get_ticket_id(self):
        return self.__ticket_id
    
    def get_destination(self):
        return self.__destination
        
    def get_passenger_name(self):
        return self.__passenger_name
        
    def validate_source_destination(self):
        if((self.__source.upper()=="DELHI") and (self.__destination.upper()=="MUMBAI" or self.__destination.upper()=="CHENNAI" or self.__destination.upper()=="PUNE" or self.__destination.upper()=="KOLKATA")):
            return True
        else:
            return False
    
    def generate_ticket(self):
        if(self.validate_source_destination()):
            Ticket.counter+=1
            if(len(str(Ticket.counter))==1):
                a="0"+str(Ticket.counter)
            else:
                a=str(Ticket.counter)
            
            self.__ticket_id=self.__source[0]+self.__destination[0]+a
            
            
John=Ticket("John","DelHi","Kolkata")
John.generate_ticket()


#OOPR-Exer-8
class Juggler:
    def __init__(self,name):
        self.__name=name

    def juggles(self,jugglingitem):
        self.__jugglingitem=jugglingitem
        print(self.__name ,"is juggling with ",self.__jugglingitem)

class JugglingItem:
    def __init__(self,name):
        self.__name=name

    def get_name(self):
        return self.__name
s=JugglingItem("Balls")
Jack=Juggler("Jack")
Jack.juggles(s.get_name())



#ASS 15
class Parrot:
    __counter=7000
    def __init__(self,name,color):
        self.__name=name
        self.__color=color
        Parrot.__counter+=1
        self.__unique_number=Parrot.__counter
        
        
    def get_color(self):
        return __self.color
    
    def get_name(self):
        return __self.name
    
    def get_unique_number(self):
        return __uniqe_number
        
p=Parrot("kali","red")
k=Parrot("guru","yellow")
p=Parrot("kali","red")
k=Parrot("guru","yellow")
p=Parrot("kali","red")
k=Parrot("guru","yellow")


class Customer:
    def __init__(self,phone_no,name,age):
        self.phone_no=phone_no
        self.name=name
        self.age=age
        self.list_of_calls=None

class CallDetail:
    def __init__(self,phone_no,called_no,duration):
        self.phone_no=phone_no
        self.called_no=called_no
        self.duration=duration

class Util:
    def __init__(self):
        self.cust_phn=None
        self.list_of_call=None
        
    def parse_customer(self,list_of_customers,list_of_calls):
        for i in list_of_customers:
            for j in list_of_calls:
                self.cust_phn=i.phone_no
                if i.phone_no==j.phone_no:
                    self.list_of_call=j.called_no
                
cust1=Customer(9900009901,'cust1',23)
cust2=Customer(9900009902,'cust2',24)
cust3=Customer(9900009903,'cust3',25)
list_of_customers=[cust1,cust2,cust3]

call1=CallDetail(9900009901,8800123401,5)
call2=CallDetail(9900009903,8800123402,10)
call3=CallDetail(9900009902,8800123403,2)
call4=CallDetail(9900009901,8800123404,8)
call5=CallDetail(9900009901,8800123405,7)
call6=CallDetail(9900009903,8800123406,9)
call7=CallDetail(9900009903,8800123407,4)
list_of_calls=[call1,call2,call3,call4,call5,call6,call7]

Util().parse_customer(list_of_customers, list_of_calls)

