import time
class car():
    def __init__(self,name,dob):
        self.name=name
        self.dob=dob
        self.unit=0

    def manufactured_unit(self):
        a=int(input("How many units you have manufactured today:--"))
        b=time.asctime()
        self.unit=self.unit + a
        return f"The today's date is {b}, the units you manufactured today is {a} and total units you have {self.unit}"

    def sold_unit(self):
        a=int(input("How many units of car you have sold today:--"))
        b=time.asctime()
        if self.unit > a:
            self.unit=self.unit - a 
            return f"The today's date is {b}, the units you sold today is {a} and total unit is {self.unit}"
        elif self.unit < a:
            return f"You cannot sold more than manufacturing unit and you have {self.unit} units"

    def display_unit(self):
        return f"The total units you have {self.unit}"

mahindra=car("Mahindra","29-06-2002")

def main():
    while True:
        b=input("Enter what you want to go for manufactured unit and sold unit, for manufactured unit enter 'm', for sold unit enter 's' and for display units enter 'd':==")
        if b=="m" or b=="manufacture":
            print(mahindra.manufactured_unit())
        elif b=="s" or b=="sold":
            print(mahindra.sold_unit())
        elif b=="d" or b=="display":
            print(mahindra.display_unit())
        else:
            print("Invalid input")
main()  

