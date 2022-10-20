def income_converter():
    res = str(input("Do you need hourly program or salary program? "))
    if res == "hourly" or res == "h":
        print("Providing hourly program for you now. ")

        def hourly_income():
            try:
                inb = float(input("Enter hourly rate: "))
            except:
                inb = float(input("Invalid input, please try again: "))
            if inb <= 0:
                print("Invalid input, must be greater than zero.")
                inb = float(input("Please try another amount: "))
            while inb <= 0:
                inb = float(input("Please try another amount: "))
            inc = inb * 2080
            print("Year rate would be $", "${:,.2f}".format(inc))
            res = str(input("Are you interested in knowing rate for shift pay? Yes or No "))
            if res == "yes" or res == "y":
                try:
                    hrs = int(input("Please enter the hours you are looking to work: "))
                except:
                    hrs = int(input("Invalid input, please enter the hours you are looking to work: "))
                if hrs <= 0:
                    print("Invalid input, must be greater than zero.")
                    hrs = int(input("Please try another amount: "))
                while hrs <= 0:
                    hrs = int(input("Please try another amount: "))
                hrworked = hrs * inb
                hrworkedfl = float(hrworked)
                hrworkedc = "${:,.2f}".format(hrworkedfl)
                print("If you worked", hrs, "hours, your days pay would be", hrworkedc)
            else:
                print("Session has ended.")

        hourly_income()
    if res == "salary" or res == "s":
        print("Providing salary program for you now. ")

        def salary_income():
            income = float(input("Enter the salary or annual income: "))
            if income <= 0:
                print("Invalid input, must be greater than zero.")
                income = float(input("Please try another amount: "))
            while income <= 0:
                income = float(input("Please try another amount: "))
            hr = income / 2080
            hrc = "${:,.2f}".format(hr)
            ot = hr * 1.5
            otc = "${:,.2f}".format(ot)
            biwk = income / 52
            biwkc = "${:,.2f}".format(biwk)
            print("Hourly pay rate ", hrc)
            print("Bi-weekly rate ", biwkc)
            print("Overtime rate ", otc)

        salary_income()



income_converter()
