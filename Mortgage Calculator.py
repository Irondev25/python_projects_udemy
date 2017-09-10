y = 'y'


while y == 'y':
    principle = float(input("Enter amount taken: "))
    rate = float(input("Enter rate of interest: "))/100
    time = float(input("Enter tenure of loan in years: "))
    amount = 0
    print("Option:\n 1. Daily \n 2.Weekly \n 3.Monthly \n 4.Yearly \n 5.Calculate all")
    option = input("Enter your option: ")
    if option == 1:
        amount = principle*((1+(rate/365))**(365*time))
        print("Your total amount is %0.4f" % (amount))
    elif option == 2:
        amount = principle*((1+(rate/52))**(52*time))
        print("Your total amount is %0.4f" % (amount))
    elif option == 3:
        amount = principle*((1+(rate/12))**(12*time))
        print("Your total amount is %0.4f" % (amount))
    elif option == 4:
        amount = principle*((1+rate)**time)
        print("Your total amount is %0.4f" % (amount))
    else:
        amount = principle*((1+(rate/365))**(365*time))
        print("Your total amount(daily) is %0.4f" % (amount))
        amount = principle*((1+(rate/52))**(52*time))
        print("Your total amount(weekly) is %0.4f" % (amount))
        amount = principle*((1+(rate/12))**(12*time))
        print("Your total amount(monthly) is %0.4f" % (amount))
        amount = principle*((1+rate)**time)
        print("Your total amount(yearly) is %0.4f" % (amount))

    y = input("Do you want to calculate for other mortgage.(y/n)")
