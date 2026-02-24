print("                                                         ===Marksheet===")
print("                                                --Enter your Marks of 4 Subjects--")

def GetMarks():
    try:
            eng=int(input("Enter the marks obtained in English: "))
            PST=int(input("Enter the marks obtained in Pakistan Studeies: "))
            Urd=int(input("Enter the marks obtained in Urdu: "));Isl=int(input("Enter the marks obtained in islamiat: "))



            if(eng<0 or PST<0 or Urd<0 or Isl<0):
                print("The number can not be negative.")
                GetMarks()

    except ValueError:
        print("Invalid Input! Enter a Number")
        GetMarks()

    def  cal(eng,PST,Urd,Isl):
        Total_Marks = eng + PST + Urd + Isl
        Per = Total_Marks / 400 * 100
        print(Per, "%")

        if (Per > 70):
            print("pass")

        else:
            print("fail")

    cal(eng, PST, Urd, Isl)

while(True):
    GetMarks()
    ask=input("Do u wish to continue?: ")
    if(ask=="y"):
        GetMarks()
    else:
        break