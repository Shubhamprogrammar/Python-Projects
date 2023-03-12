class rbi:
    __secure="RBI Bank details"
    def __init__(self,name,margin):
        self.name=name
        self.margin=margin
        self.amount=100000000
        self.bankrec={}
        self.banksen={}

    def curreceive(self):
        """This function takes input from the bank that how much amount they want to take from the bank"""
        amo=int(input("How much amount you want to take from the bank\n"))
        ban=input("Enter the name of the person\n")
        if self.margin > amo:
            if self.amount > amo:
                self.bankrec.update({amo:ban})
                self.amount=self.amount-amo
                return f"The {ban} bank has taken the {amo} amount from the RBL Bank and {self.bankrec}"
            elif self.amount < amo:
                return f"This much amount '{amo}' is not present in bank and total amount we have {self.amount}"
            else:
                return "We can't give total amount"
        elif self.margin < amo:
            return "We cannot give amount to the bank who has less margin in a year"
        else:
            return "We can't give equal amount of the margin"

    def cursend(self):
        """This function takes input from the bank that how much amount they want to give to the bank"""
        amo=int(input("Enter how much amount you want to give back to bank\n"))
        ban=input("Enter the name of the person\n")
        self.banksen.update({amo:ban})
        self.amount=self.amount+amo
        return f"The {ban} bank has given the {amo} amount to the RBI Bank and {self.banksen}"

rbl=rbi("RBL",10000000)
yes=rbi("YES",100000)
canara=rbi("CANARA",5000000)

while True:
    print("Enter 0 for rbl, 1 for yes and 2 for canara")
    try:
        a=int(input("Enter the number for the bank\t"))
        if a==0:
            b=input("What do you want to do deposit or receive, for deposit enter 's' or 'send' and for receive enter 'r' or 'receive'\t")
            if b=="r" or b=="receive":
                print(rbl.curreceive())
            elif b=="s" or b=="send":
                print(rbl.cursend())
            else:
                print("You have entered something wrong")
        elif a==1:
            b=input("What do you want to do deposit or receive, for deposit enter 's' or 'send' and for receive enter 'r' or 'receive'\t")
            if b=="r" or b=="receive":
                print(yes.curreceive())
            elif b=="s" or b=="send":
                print(yes.cursend())
            else:
                print("You have entered something wrong")
        elif a==2:
            b=input("What do you want to do deposit or receive, for deposit enter 's' or 'send' and for receive enter 'r' or 'receive'\t")
            if b=="r" or b=="receive":
                print(canara.curreceive())
            elif b=="s" or b=="send":
                print(canara.cursend())
            else:
                print("You have entered something wrong")
        else:
            print("You have entered some wrong input")
    except ValueError:
        print("Enter Integers only")