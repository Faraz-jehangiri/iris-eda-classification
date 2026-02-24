BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"
print("============================================")
print(f"{BOLD}{ITALIC}                 🏦OUR BANK🏦 {RESET}                ")
print(f"                 Welcome! 💓")
print("============================================")
print()
balance=10000000
i=0
pi=4567
try:
    name = input("Kindly type in your name: ")
    age = int(input("Kindly type in your age: "))
    pin = int(input("Kindly type in your pin: "))
    while True:
        if i >= 1:
            print()
            print("=======================  Hello again!  =========================")


        print()
        if pi == pin:
            print("What Service do you want from us today? ☀️.")
            print("1) Check Details\n2) Loan Categories\n3) Exit ")
            print()
            choice=int(input(f"Enter your choice\n( 1 for Check Details, 2 for Loan Categories, 3 for Exit ): "))
            if choice==1:
                print()
                print("============================================")
                print(f"{BOLD}{ITALIC}                  📜DETAILS📜 {RESET}                ")
                print("============================================")
                print()
                print(f"Name= {name}")
                print(f"Age= {age}")
                print(f"Pin= {pin}")
                print(f"Your Current Balance= {balance}")
                print()
                cnt=input("Do you want to choose some other service? (Y/N): ")
                if cnt.upper()=="N":
                    break

            elif choice==2:
                print()
                print("============================================")
                print(f"{BOLD}{ITALIC}             LOANS CATEGORIES {RESET}                ")
                print("============================================")
                print()
                print(f"We have 3 categories for loans")
                print()
                print("We offer 3 main loan Categories\n1) Personal Loan\n2) House Loan\n3) Car Loan")
                print()
                choose=int(input("Choose the Category you want Loan for ( 1 for Personal, 2 for House , 3 for Car ): "))
                if choose==1:
                    print("============================================")
                    print(f"{BOLD}{ITALIC}             🥸PERSONAL LOANS💰 {RESET}                ")
                    print("============================================")
                    print()
                    print("You can get following amounts of loans: \n1) 20 Lakhs PKR\n2) 40 Lakhs PKR\n3) 60 Lakhs PKR")
                    loan_amount=int(input("Enter your loan amount ( 1 for 20, 2 for 40, 3 for 60: "))
                    if loan_amount==1:
                        print()
                        salary=int(input("Kindly enter your salary to check eligibility: "))
                        formula=(2.5/100)*2000000

                        if salary>=int(formula):
                            print()
                            print(f"{BOLD}{UNDERLINE}Congrats you have been granted loan of PKR 20 LAKHS!.{RESET}")
                            print()
                            cnt=input("Do you want to check eligibility? (Y/N): ")
                            if cnt.upper()=="N":
                                break
                        else:
                            print(f"{BOLD}{UNDERLINE}Sorry your salary does not meet our requirements for this loan category😔.{RESET}")

                    elif loan_amount==2:
                        print()
                        salary = int(input("Kindly enter your salary to check eligibility: "))
                        formula = (5 / 100) * 4000000

                        if salary >= int(formula):
                            print(f"{BOLD}{UNDERLINE}Congrats you have been granted loan of PKR 40 LAKHS!.{RESET}")
                            print()
                            cnt = input("Do you want to check eligibility? (Y/N): ")
                            if cnt.upper() == "N":
                                break
                        else:
                            print(
                                f"{BOLD}{UNDERLINE}Sorry your salary does not meet our requirements for this loan category😔.{RESET}")

                    elif loan_amount==3:
                        print()
                        salary = int(input("Kindly enter your salary to check eligibility: "))
                        formula = (10 / 100) * 6000000

                        if salary >= int(formula):
                            print(f"{BOLD}{UNDERLINE}Congrats you have been granted loan of PKR 60 LAKHS!.{RESET}")
                            print()
                            cnt = input("Do you want to check eligibility? (Y/N): ")
                            if cnt.upper() == "N":
                                break
                        else:
                            print(
                                f"{BOLD}{UNDERLINE}Sorry your salary does not meet our requirements for this loan category😔.{RESET}")

                    else:
                        print("Please Enter a Valid Number.")
                elif choose==2:
                    print("============================================")
                    print(f"{BOLD}{ITALIC}              🏠HOUSE LOANS💰 {RESET} ")
                    print("============================================")
                    print()
                    print("You can get following amounts of loans: \n1) 50 Lakhs PKR\n2) 70 Lakhs PKR\n3) 90 Lakhs PKR")
                    loan_amount = int(input("Enter your loan amount ( 1 for 50, 2 for 70, 3 for 90: "))
                    if loan_amount == 1:
                        print()
                        salary = int(input("Kindly enter your salary to check eligibility: "))
                        formula = (2.5 / 100) * 5000000

                        if salary >= int(formula):
                            print(f"{BOLD}{UNDERLINE}Congrats you have been granted loan of PKR 50 LAKHS!.{RESET}")
                            print()
                            cnt = input("Do you want to check eligibility? (Y/N): ")
                            if cnt.upper() == "N":
                                break
                        else:
                            print(
                                f"{BOLD}{UNDERLINE}Sorry your salary does not meet our requirements for this loan category😔.{RESET}")

                    elif loan_amount == 2:
                        print()
                        salary = int(input("Kindly enter your salary to check eligibility: "))
                        formula = (5 / 100) * 7000000

                        if salary >= int(formula):
                            print(f"{BOLD}{UNDERLINE}Congrats you have been granted loan of PKR 70 LAKHS!.{RESET}")
                            print()
                            cnt = input("Do you want to check eligibility? (Y/N): ")
                            if cnt.upper() == "N":
                                break
                        else:
                            print(
                                f"{BOLD}{UNDERLINE}Sorry your salary does not meet our requirements for this loan category😔.{RESET}")

                    elif loan_amount == 3:
                        print()
                        salary = int(input("Kindly enter your salary to check eligibility: "))
                        formula = (10 / 100) * 9000000

                        if salary >= int(formula):
                            print(f"{BOLD}{UNDERLINE}Congrats you have been granted loan of PKR 90 LAKHS!.{RESET}")
                            print()
                            cnt = input("Do you want to check eligibility? (Y/N): ")
                            if cnt.upper() == "N":
                                break
                        else:
                            print(
                                f"{BOLD}{UNDERLINE}Sorry your salary does not meet our requirements for this loan category😔.{RESET}")

                    else:
                        print("Please Enter a Valid Number.")

                elif choose==3:
                    print("============================================")
                    print(f"{BOLD}{ITALIC}              🚗CAR LOANS💰 {RESET} ")
                    print("============================================")
                    print()
                    print("You can get following amounts of loans: \n1) 10 Lakhs PKR\n2) 20 Lakhs PKR\n3) 30 Lakhs PKR")
                    loan_amount = int(input("Enter your loan amount ( 1 for 10, 2 for 20, 3 for 30: "))
                    if loan_amount == 1:
                        print()
                        salary = int(input("Kindly enter your salary to check eligibility: "))
                        formula = (2.5 / 100) * 1000000

                        if salary >= int(formula):
                            print(f"{BOLD}{UNDERLINE}Congrats you have been granted loan of PKR 10 LAKHS!.{RESET}")
                            print()
                            cnt = input("Do you want to check eligibility? (Y/N): ")
                            if cnt.upper() == "N":
                                break
                        else:
                            print(
                                f"{BOLD}{UNDERLINE}Sorry your salary does not meet our requirements for this loan category😔.{RESET}")

                    elif loan_amount == 2:
                        print()
                        salary = int(input("Kindly enter your salary to check eligibility: "))
                        formula = (5 / 100) * 2000000

                        if salary >= int(formula):
                            print(f"{BOLD}{UNDERLINE}Congrats you have been granted loan of PKR 20 LAKHS!.{RESET}")
                            print()
                            cnt = input("Do you want to check eligibility? (Y/N): ")
                            if cnt.upper() == "N":
                                break
                        else:
                            print(
                                f"{BOLD}{UNDERLINE}Sorry your salary does not meet our requirements for this loan category😔.{RESET}")

                    elif loan_amount == 3:
                        print()
                        salary = int(input("Kindly enter your salary to check eligibility: "))
                        formula = (10 / 100) * 3000000

                        if salary >= int(formula):
                            print(f"{BOLD}{UNDERLINE}Congrats you have been granted loan of PKR 30 LAKHS!.{RESET}")
                            print()
                            cnt = input("Do you want to check eligibility? (Y/N): ")
                            if cnt.upper() == "N":
                                break
                        else:
                            print(
                                f"{BOLD}{UNDERLINE}Sorry your salary does not meet our requirements for this loan category😔.{RESET}")

                    else:
                        print("Please Enter a Valid Number.")

                else:
                    print("Enter a valid number.")





            elif choice==3:
                print(f"The program will Exit now")
                print()
                print("============================================")
                print(f"{BOLD}{ITALIC}  THANKS FOR CHOOSING OUR BANK💓 GOODBYE!👋 {RESET}                ")
                print("============================================")
                break

            i+=1
        else:
            print("Wrong Pin!.")


except ValueError:
    print(f"Invalid choice. Please try again.")

