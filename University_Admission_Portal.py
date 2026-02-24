BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"
Questions = [
    "What is the full form of RAM?",
    "Brain of the computer is?",
    "computer has system software and _____ software?",
    "What is the full form of CPU?",
    "What is the full form of ROM?",
    "Which of the following is volatile memory?",
    "Smallest unit of data in computer?",
    "What does WWW stand for?",
    "Father of Computer?",
    "What is the extension of plain text file?",
    "Which is not an input device?",
    "What does HTML stand for?"
]

Answers = [
    "Random Access Memory",
    "CPU",
    "Application",
    "Central Processing Unit",
    "Read Only Memory",
    "RAM",
    "Bit",
    "World Wide Web",
    "Charles Babbage",
    ".txt",
    "Monitor",
    "Hyper Text Markup Language"
]

choices = [
    "1) Random access memory\n2) Read only memory",
    "1) CPU \n2) Motherboard",
    "1) Application \n2) kernel",
    "1) Central Processing Unit \n2) Central Program Unit",
    "1) Read Only Memory \n2) Random Only Memory",
    "1) RAM \n2) ROM",
    "1) Bit \n2) Byte",
    "1) World Wide Web \n2) World Web Wide",
    "1) Charles Babbage \n2) Bill Gates",
    "1) .txt \n2) .doc",
    "1) Monitor \n2) Keyboard",
    "1) Hyper Text Markup Language \n2) Hyper Transfer Markup Language"
]

User_Answers = []
otl_CS = {"Years": 4, "Semesters": 8, "Credit Hours": 133, "Senior Design Project": 6}
otl_DS = {"Years": 4, "Semesters": 8, "Credit Hours": 130, "Senior Design Project": 6}
otl_AI = {"Years": 4, "Semesters": 8, "Credit Hours": 128, "Senior Design Project": 6}
otl_BA = {"Years": 4, "Semesters": 8, "Credit Hours": 120, "Senior Design Project": 3}
otl_SE = {"Years": 4, "Semesters": 8, "Credit Hours": 135, "Senior Design Project": 6}
otl_CE = {"Years": 4, "Semesters": 8, "Credit Hours": 140, "Senior Design Project": 6}

otl_MS_CS = {"Years": 2, "Semesters": 4, "Credit Hours": 30, "Thesis": 6}
otl_MS_Cyber = {"Years": 2, "Semesters": 4, "Credit Hours": 32, "Thesis": 6}
otl_MS_ML = {"Years": 2, "Semesters": 4, "Credit Hours": 30, "Thesis": 6}
otl_MS_SE = {"Years": 2, "Semesters": 4, "Credit Hours": 31, "Thesis": 6}
otl_MS_DS = {"Years": 2, "Semesters": 4, "Credit Hours": 30, "Thesis": 6}
otl_MS_Cloud = {"Years": 2, "Semesters": 4, "Credit Hours": 33, "Thesis": 6}

MS_Program = ["Computer Science", "Cyber Security", "Machine Learning", "Software Engineering",
              "Data Science/Analytics", "Cloud Engineering"]
BS_Program = ["Computer Science", "Data Science", "Artificial Intelligence", "Business Administration",
              "Software Engineering", "Computer Engineering"]

n = 1


age = int(input("Enter age: "))
print()
if 20 <= age < 30:
    marks = 0
    exam = input(
        "You have to complete an exam to get admission in any field. if you want to continue type 'continue': ")
    if exam.lower() == "continue":
        print("The Exam starts now! GoodLuck😊.")
        print()
        print(f"{BOLD}{ITALIC}{UNDERLINE}💀💀💀 Exam 💀💀💀{RESET}")

        for i in range(len(Questions)):
            print()
            print(Questions[i])
            print(choices[i])
            print()
            ans = input("Enter your Answer: ")
            User_Answers.append(ans)

        for i in range(len(User_Answers)):
            if User_Answers[i].lower() == Answers[i].lower():
                marks += 2
            else:
                marks -= 1
    print()
    if marks == 0:
        print(f"Marks = {marks} you have failed the exam. 😡")
    elif 1 <= marks <= 5:
        print(f"you have succeeded with Marks = {marks}. But your marks are enough for other programs.")
    else:
        print(f"hurrah! you have passed the exam with Marks= {marks}.")

    if marks>=17:
        print("Your'e eligible for \n1) Computer Science\n2) Computer Engineering\n3) Software Engineering\n4) Data Science\n5) Artificial Intelligence\n6)business administration")
    elif 13 <=marks <= 16:
        print("Your'e eligible for \n1) Data Science\n2) Artificial Intelligence\n3) Business Administration\n4) Computer Engineering")

    elif 9<=marks <= 12:
        print("Your'e eligible for \n1) Artificial Intelligence\n2) Business Administration")
    elif 5<=marks <= 0:
        print("Your'e only eligible for \n1) Business Administration")

    else:
        print("You've got less than 0 marks, try better next time!.")

    print()

    print("you have been offered BS (Bachelor's).")
    print()
    bs = input("to get the list of BS programs type BS: ")
    if bs.lower() == "bs":
        for i in BS_Program:
            print(f"{n}) {i}")
            n += 1
        print()
        choice = input("which program do you want?: ")
        choice = choice.lower()
        print()
        if choice == "computer science":
            if marks >= 17:
                print("The fee for this degree is 135k per semester.")
                print()
                ch = input("do you want to continue with the CS program? Y or N: ")
                print()
                if ch.lower() == "y":
                    outline = input("Do you want the outline of the CS degree? Y or N: ")
                    if outline.lower() == 'y':
                        print(f"{BOLD}{UNDERLINE}{ITALIC}=== CS Outline ==={RESET}")
                        for i, y in otl_CS.items():
                            print(f"{i} = {y}")
                    print()
                    inp6 = input("have u decided to enroll for the CS degree?: ")
                    print()
                    if inp6.lower() == 'y':
                        print("""Congrats!🎉🎉 you are on your way to become a computer scientist!🔭 
Welcome Aboard. 💓🎓""")
                    else:
                        print("now u have to run the program again and choose a different field should've taken while had the chance.")
                else:
                    print("You've decided to exit the program.")

        elif choice == "data science":
            if marks>=13:
                print("The fee for this degree is 120k per semester.")
                ch = input("do you want to continue with the DS program? Y or N: ")
                if ch.lower() == "y":
                    outline = input("Do you want the outline of the DS degree? Y or N: ")
                    if outline.lower() == 'y':
                        print(f"{BOLD}{UNDERLINE}{ITALIC}=== DS Outline ==={RESET}")
                        for i, y in otl_DS.items():
                            print(f"{i} = {y}")
                    inp6 = input("have u decided to enroll for the DS degree?: ")
                    if inp6.lower() == 'y':
                        print("""Congrats!🎉🎉 you are on your way to become a Data scientist!🔭 
Welcome Aboard. 💓🎓""")

        elif choice == "artificial intelligence":
            if marks>=9:
                print("The fee for this degree is 125k per semester.")
                ch = input("do you want to continue with the AI program? Y or N: ")
                if ch.lower() == "y":
                    outline = input("Do you want the outline of the AI degree? Y or N: ")
                    if outline.lower() == 'y':
                        print(f"{BOLD}{UNDERLINE}{ITALIC}=== AI Outline ==={RESET}")
                        for i, y in otl_AI.items():
                            print(f"{i} = {y}")
                    inp6 = input("have u decided to enroll for the AI degree?: ")
                    if inp6.lower() == 'y':
                        print("""Congrats!🎉🎉 you are on your way to become a AI Engineer!🔭 
Welcome Aboard. 💓🎓""")

        elif choice == "business administration":
            if marks>=5:
                print("The fee for this degree is 110k per semester.")
                ch = input("do you want to continue with the BA program? Y or N: ")
                if ch.lower() == "y":
                    outline = input("Do you want the outline of the BA degree? Y or N: ")
                    if outline.lower() == 'y':
                        print(f"{BOLD}{UNDERLINE}{ITALIC}=== BA Outline ==={RESET}")
                        for i, y in otl_BA.items():
                            print(f"{i} = {y}")
                    inp6 = input("have u decided to enroll for the BA degree?: ")
                    if inp6.lower() == 'y':
                        print("""Congrats!🎉🎉 you are on your way to become a Business Admin!🔭 
Welcome Aboard. 💓🎓""")

        elif choice == "software engineering":
            if marks>=17:
                print("The fee for this degree is 140k per semester.")
                ch = input("do you want to continue with the SE program? Y or N: ")
                if ch.lower() == "y":
                    outline = input("Do you want the outline of the SE degree? Y or N: ")
                    if outline.lower() == 'y':
                        print(f"{BOLD}{UNDERLINE}{ITALIC}=== SE Outline ==={RESET}")
                        for i, y in otl_SE.items():
                            print(f"{i} = {y}")
                    inp6 = input("have u decided to enroll for the SE degree?: ")
                    if inp6.lower() == 'y':
                        print("""Congrats!🎉🎉 you are on your way to become a Software Engineer!🔭 
Welcome Aboard. 💓🎓""")

        elif choice == "computer engineering":
            if marks>=14:
                print("The fee for this degree is 145k per semester.")
                ch = input("do you want to continue with the CE program? Y or N: ")
                if ch.lower() == "y":
                    outline = input("Do you want the outline of the CE degree? Y or N: ")
                    if outline.lower() == 'y':
                        print(f"{BOLD}{UNDERLINE}{ITALIC}=== CE Outline ==={RESET}")
                        for i, y in otl_CE.items():
                            print(f"{i} = {y}")
                    inp6 = input("have u decided to enroll for the CE degree?: ")
                    if inp6.lower() == 'y':
                        print("""Congrats!🎉🎉 you are on your way to become a Computer Engineer!🔭 
Welcome Aboard. 💓🎓""")
        else:
            print("Invalid program choice or marks not sufficient!")

elif 30 <= age < 37:
    print("you have been offered MS (Masters).")
    ms = input("to get the list of MS programs type MS: ")
    if ms.lower() == "ms":
        n = 0
        for i in MS_Program:
            print(f"{n}) {i}")
            n += 1

        choice = input("which program do you want?: ")
        choice = choice.lower()

        cgpa_input = input("Enter your CGPA (0-4.0): ")
        try:
            cgpa = float(cgpa_input)
        except:
            print("Invalid CGPA! Defaulting to 0.")
            cgpa = 0

        if choice == "computer science":
            if cgpa >= 3.0:
                print(f"{BOLD}{UNDERLINE}{ITALIC}=== MS Computer Science ==={RESET}")
                print("You are ELIGIBLE! 🎉")
                ch = input("do you want to continue with the MS CS program? Y or N: ")
                if ch.lower() == "y":
                    outline = input("Do you want the outline of the MS CS degree? Y or N: ")
                    if outline.lower() == 'y':
                        for i, y in otl_MS_CS.items():
                            print(f"{i} = {y}")
                    inp6 = input("have u decided to enroll for the MS CS degree?: ")
                    if inp6.lower() == 'y':
                        print("""Congrats!🎉🎉 you are on your way to become a MS Computer Scientist!🔭
    Welcome Aboard. 💓🎓""")
                    else:
                        print("No worries! Best wishes for your future endeavors. 👋")
                else:
                    print("Thanks for considering! Good luck! 😊")
            else:
                print(f"Sorry, minimum CGPA required: 3.0. Your CGPA: {cgpa}")

        elif choice == "cyber security":
            if cgpa >= 2.8:
                print(f"{BOLD}{UNDERLINE}{ITALIC}=== MS Cyber Security ==={RESET}")
                print("You are ELIGIBLE! 🎉")
                ch = input("do you want to continue with the Cyber Security program? Y or N: ")
                if ch.lower() == "y":
                    outline = input("Do you want the outline of the Cyber Security degree? Y or N: ")
                    if outline.lower() == 'y':
                        for i, y in otl_MS_Cyber.items():
                            print(f"{i} = {y}")
                    inp6 = input("have u decided to enroll for the Cyber Security degree?: ")
                    if inp6.lower() == 'y':
                        print("""Congrats!🎉🎉 you are on your way to become a Cyber Security Expert!🔭
    Welcome Aboard. 💓🎓""")
                    else:
                        print("No worries! Best wishes for your future endeavors. 👋")
                else:
                    print("Thanks for considering! Good luck! 😊")
            else:
                print(f"Sorry, minimum CGPA required: 2.8. Your CGPA: {cgpa}")

        elif choice == "machine learning":
            if cgpa >= 3.2:
                print(f"{BOLD}{UNDERLINE}{ITALIC}=== MS Machine Learning ==={RESET}")
                print("You are ELIGIBLE! 🎉")
                ch = input("do you want to continue with the ML program? Y or N: ")
                if ch.lower() == "y":
                    outline = input("Do you want the outline of the ML degree? Y or N: ")
                    if outline.lower() == 'y':
                        for i, y in otl_MS_ML.items():
                            print(f"{i} = {y}")
                    inp6 = input("have u decided to enroll for the ML degree?: ")
                    if inp6.lower() == 'y':
                        print("""Congrats!🎉🎉 you are on your way to become a ML Engineer!🔭
    Welcome Aboard. 💓🎓""")
                    else:
                        print("No worries! Best wishes for your future endeavors. 👋")
                else:
                    print("Thanks for considering! Good luck! 😊")
            else:
                print(f"Sorry, minimum CGPA required: 3.2. Your CGPA: {cgpa}")

        elif choice == "software engineering":
            if cgpa >= 2.9:
                print(f"{BOLD}{UNDERLINE}{ITALIC}=== MS Software Engineering ==={RESET}")
                print("You are ELIGIBLE! 🎉")
                ch = input("do you want to continue with the SE program? Y or N: ")
                if ch.lower() == "y":
                    outline = input("Do you want the outline of the SE degree? Y or N: ")
                    if outline.lower() == 'y':
                        for i, y in otl_MS_SE.items():
                            print(f"{i} = {y}")
                    inp6 = input("have u decided to enroll for the SE degree?: ")
                    if inp6.lower() == 'y':
                        print("""Congrats!🎉🎉 you are on your way to become a Software Engineering Master!🔭
    Welcome Aboard. 💓🎓""")
                    else:
                        print("No worries! Best wishes for your future endeavors. 👋")
                else:
                    print("Thanks for considering! Good luck! 😊")
            else:
                print(f"Sorry, minimum CGPA required: 2.9. Your CGPA: {cgpa}")

        elif choice == "data science/analytics":
            if cgpa >= 3.0:
                print(f"{BOLD}{UNDERLINE}{ITALIC}=== MS Data Science ==={RESET}")
                print("You are ELIGIBLE! 🎉")
                ch = input("do you want to continue with the DS program? Y or N: ")
                if ch.lower() == "y":
                    outline = input("Do you want the outline of the DS degree? Y or N: ")
                    if outline.lower() == 'y':
                        for i, y in otl_MS_DS.items():
                            print(f"{i} = {y}")
                    inp6 = input("have u decided to enroll for the DS degree?: ")
                    if inp6.lower() == 'y':
                        print("""Congrats!🎉🎉 you are on your way to become a Data Scientist!🔭
    Welcome Aboard. 💓🎓""")
                    else:
                        print("No worries! Best wishes for your future endeavors. 👋")
                else:
                    print("Thanks for considering! Good luck! 😊")
            else:
                print(f"Sorry, minimum CGPA required: 3.0. Your CGPA: {cgpa}")

        elif choice == "cloud engineering":
            if cgpa >= 2.7:
                print(f"{BOLD}{UNDERLINE}{ITALIC}=== MS Cloud Engineering ==={RESET}")
                print("You are ELIGIBLE! 🎉")
                ch = input("do you want to continue with the Cloud program? Y or N: ")
                if ch.lower() == "y":
                    outline = input("Do you want the outline of the Cloud degree? Y or N: ")
                    if outline.lower() == 'y':
                        for i, y in otl_MS_Cloud.items():
                            print(f"{i} = {y}")
                    inp6 = input("have u decided to enroll for the Cloud degree?: ")
                    if inp6.lower() == 'y':
                        print("""Congrats!🎉🎉 you are on your way to become a Cloud Engineer!🔭
    Welcome Aboard. 💓🎓""")
                    else:
                        print("No worries! Best wishes for your future endeavors. 👋")
                else:
                    print("Thanks for considering! Good luck! 😊")
            else:
                print(f"Sorry, minimum CGPA required: 2.7. Your CGPA: {cgpa}")

        else:
            print("Invalid program choice!")
elif age >= 37:
    print("you have been offered PHD.")

else:
    print("Enter a valid input.")
