# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02} eur"
    
    def __eq__(self, another:"Money"):
        self_money = f"{self.__euros}.{self.__cents:02} eur"
        another_money = f"{another.__euros}.{another.__cents:02} eur"

        return self_money == another_money
    
    def __ne__(self, another: "Money"):
        self_money = f"{self.__euros}.{self.__cents:02} eur"
        another_money = f"{another.__euros}.{another.__cents:02} eur"

        return self_money != another_money
    
    def __lt__(self,another: "Money"):
        self_money = f"{self.__euros}.{self.__cents:02} eur"
        another_money = f"{another.__euros}.{another.__cents:02} eur"

        return self_money < another_money
    
    def __gt__(self,another: "Money"):
        self_money = f"{self.__euros}.{self.__cents:02} eur"
        another_money = f"{another.__euros}.{another.__cents:02} eur"

        return self_money > another_money
    
    def __add__(self,another: "Money"):
        self_money = f"{self.__euros}.{self.__cents:02}"
        another_money = f"{another.__euros}.{another.__cents:02}"
        total = str(float(self_money) + float(another_money))
        euros,cents = total.split(".")
        return Money(euros,cents)
    
    def __sub__(self,another: "Money"):
        self_money = f"{self.__euros}.{self.__cents:02}"
        another_money = f"{another.__euros}.{another.__cents:02}"
        
        total = str(round(float(self_money) - float(another_money),2))
        
        if "-" in total:
            raise ValueError("a negative result is not allowed")
     
        euros,cents = total.split(".")
        return Money(euros,cents)
