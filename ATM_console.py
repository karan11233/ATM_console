'''Write a python program for ATM console.
1. Withdrawal
2. Deposit
3. Mini statement
4. Exit
'''

bal=20000
l=[0,0,0,0,0]

while True:
    inp=int(input("Enter Operation: "))
    if inp==1:
        w=int(input("Enter The Withdrawal Amount: "))
        if(w<=bal):
            if (w%100==0):
                if(w>=10000):
                    otp=input("Enter The 4 Digit OTP: ")
                    if (len(otp)==4):
                        print("Withdrawal Successful and Remaining Balance in your Account is:", bal-w)
                    else:
                        print("Invalid OTP.")
                else:
                    print("Invalid Denomination.")
            else:
                print("Insufficient Funds.")
        else:
            print("Invalid Amount.")
        l.append(w)  
    elif inp==2:
        denom=int(input("Enter The Denomination: "))
        a=int(input("Enter Amount: "))

        if (a% 100 == 0):
            if ((a/denom)<=200):
                print("Deposit Successful and Total Balance in your Account is:", bal+a)
            else:
                print("More than 200.")
        else:
            print("Invalid Denomination.")
        l.append(a)
    elif inp==3:
        print(l)
    elif inp==4:
        SystemExit(0)
    else:
        print("Inavalid Input.")