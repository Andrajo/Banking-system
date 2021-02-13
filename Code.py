# Write your code here
import random
import sqlite3


def Luhn_Algorithm(credit):
    copy_credit=credit
    suma=0
    for i in range(len(copy_credit)):
        if i%2==0:
            if 2*int(copy_credit[i])>9:
                suma+=2*int(copy_credit[i])-9
            else:
                suma+=2*int(copy_credit[i])
        elif i%2!=0:
            suma+=int(copy_credit[i])
    if suma%10==0:
        return True
    return False



def card_creation():
    credit=['400000']
    seventh=random.choice(range(100000000,999999999))
    while accounts.count(seventh)!=0:
        seventh=random.choice(range(100000000,999999999))
    accounts.append(seventh)
    credit.append(str(seventh))
    suma=0
    copy_credit=''.join(credit)
    for i in range(len(copy_credit)):
        if i%2==0:
            if 2*int(copy_credit[i])>9:
                suma+=2*int(copy_credit[i])-9
            else:
                suma+=2*int(copy_credit[i])
        elif i%2!=0:
            suma+=int(copy_credit[i])
    if suma%10==0:
        credit.append('0')
    else:
        credit.append(str(10-(suma%10)))
    credit=''.join(credit)
    return credit




def pin_creation():
    pin=str(random.randint(1000,10000))
    return pin


def validity(credit,pin):
    ok=-1
    if credit in credit_cards:
        ok=0
        if credit_cards[credit]==pin:
            ok=1
    if ok==-1 or ok==0:
        return False
    if ok==1:
        return True




connnection=sqlite3.connect('card.s3db')
cursor=connnection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS card (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        number TEXT,
        pin TEXT,
        balance INTEGER DEFAULT 0
    )""")
connnection.commit()




def second_comands(credit):
    second_command=int(input("""1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit\n"""))
    breakup=0
    while second_command!=5:
        if second_command==0:
            breakup=1
            break
        if second_command==1:
            print("Balance: {}".format(credit_money[credit]))
        if second_command==2:
            add=int(input("Enter income:\n"))
            print("Income was added!")
            credit_money[credit]+=add
            for i in credits_ids.keys():
                if i==credit:
                    poz=credits_ids[i]
                    break
            cursor.execute("UPDATE card SET balance = {} WHERE id = {}".format(credit_money[credit],poz))
            connnection.commit()
        if second_command==3:
            second_credit=input("Transfer\nEnter card number:\n")
            if second_credit==credit:
                print("You can't transfer money to the same account!")
            else:
                if Luhn_Algorithm(second_credit)==False:
                    print("Probably you made mistake in the card number. Please try again!")
                else:
                    if second_credit in credit_cards:
                        add=int(input("Enter how much money you want to transfer:\n"))
                        if add>credit_money[credit]:
                            print("Not enough money!")
                        else:
                            print("Success!")
                            credit_money[credit]-=add
                            credit_money[second_credit]+=add
                            for i in credits_ids.keys():
                                if i==credit:
                                    poz=credits_ids[i]
                                    break
                            cursor.execute("UPDATE card SET balance = {} WHERE id = {}".format(credit_money[credit],poz))
                            connnection.commit()
                            for i in credits_ids.keys():
                                if i==second_credit:
                                    poz=credits_ids[i]
                                    break
                            cursor.execute("UPDATE card SET balance = {} WHERE id = {}".format(credit_money[second_credit],poz))
                            connnection.commit()
                            #cursor.execute("SELECT * FROM card")
                            #rows=cursor.fetchall()
                            #for i in rows:
                            #    print(i)
                    else:
                        print("Such a card does not exist.")
        if second_command==4:
            print("The account has been closed!")
            cursor.execute("DELETE FROM card WHERE number = {}".format(credit))
            connnection.commit()
            break
        second_command=int(input("""1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit\n"""))
        if command==5:
            print("You have successfully logged out!")
    return breakup





command=int(input("""1. Create an account
2. Log into account
0. Exit\n"""))
accounts=[]
credit_cards= {}
credit_money={}
credits_ids={}
breakup=0
while command!=0:
    if command==1:
        print("Your card has been created")
        credit=card_creation()
        print(credit)
        print("Your card PIN:")
        pin=pin_creation()
        print(pin)
        credit_cards[credit]=pin
        credit_money[credit]=0
        cursor.execute("INSERT INTO card(number, pin, balance) VALUES ({}, {}, {})".format(credit,credit_cards[credit],credit_money[credit]))
        connnection.commit()
        credits_ids[credit]=cursor.lastrowid
    if command==2:
        credit=input("Enter your card number:")
        pin=input("Enter your PIN:")
        x=validity(credit,pin)
        if x==False:
            print("Wrong card number or PIN!")
        if x==True:
            print("You have successfully logged in!")
            breakup=second_comands(credit)
        if command==0:
            break
    if breakup==1:
        break
    command=int(input("""1. Create an account
2. Log into account
0. Exit\n"""))
connnection.close()
print("Bye!")
