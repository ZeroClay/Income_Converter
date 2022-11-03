def income_converter():
    res = str(input("Do you need Hourly program or Salary program? (H) or (S) ")).lower()
    if res == "h":
        def hourly_income():
            inc = float(input("Enter hourly rate: "))
            if inc <= 0:
                print("Invalid input, must be greater than zero.")
                inc = float(input("Please try another amount: "))
            while inc <= 0:
                inc = float(input("Please try another amount: "))
            hr = inc
            inc = inc * 2080
            incm = inc / 12
            incbwk = inc / 52
            incot = hr * 1.5
            incbwkc = "${:,.2f}".format(incbwk)
            incotc = "${:,.2f}".format(incot)
            incmc = "${:,.2f}".format(incm)
            incc = "${:,.2f}".format(inc)
            print(f"Overtime rate {incotc}. \nBi-weekly rate {incbwkc}. \nMonthly rate {incmc}. \nAnnual rate {incc}.")      
        hourly_income()
    if res == "s":
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
            mon = income / 12
            monc = "${:,.2f}".format(mon)
            print(f"Monthly rate {monc}. \nBi-weekly rate {biwkc}. \nOvertime rate {otc}. \nHourly rate {hrc}.")
        salary_income()
income_converter()
