name=input("what is your name?: ")
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"
part=input("HSC part I or II? (enter 1 or 2): ")
if part=="1":
    marks=input("Enter marks of 6 subjects separated by a space (English,Urdu,Maths,Physics,Chemistry,Islamiat respectively) ?: ")
else:
    marks = input("Enter marks of 6 subjects separated by a space (English,Urdu,Maths,Physics,Chemistry,PST respectively) ?: ")

arr=[]
lst={}

c=marks.split(" ")
for i in range (len(c)):
    arr.append(c[i])
if part=="1":
    lst[name]= {"English":0,"Urdu":0,"Maths":0,"Physics":0,"Chemistry":0,"Islamiat":0}
else:
    lst[name]= {"English":0,"Urdu":0,"Maths":0,"Physics":0,"Chemistry":0,"PST":0}
n=0
Obtained_Marks=0
for x,y in lst[name].items():
    for i in range (len(arr)):
        if i==n:
            lst[name][x]=arr[i]
    n += 1
    Obtained_Marks += int(lst[name][x])

Total_Marks=550
percentage=(Obtained_Marks/Total_Marks)*100
print()
print(f"{BOLD}=== Percentage ==={RESET}")
print(f"Your percentage of intermediate is just {percentage:.2f}% with total marks obtained {Obtained_Marks}. You idiot? what is this? have a life.")
i=0
print()
print(f"  {BOLD}=== Grades ==={RESET}  ")
for keys,values in lst[name].items():
    grades=int(arr[i])

    match grades:
        case x if x >= 80:
            print(f"Congratulations! you have got grade A in {keys} subject with {grades} marks.")

        case x if 70 <= x < 80:
            print(f"Congratulations! you have got grade B in {keys} subject with {grades} marks.")

        case x if 60 <= x < 70:
            print(f"Congratulations! you have got grade C in {keys} subject with {grades} marks.")
        case x if 50 <= x < 60:
            print(f"Congratulations! you have got grade D in {keys} subject with {grades} marks.")
        case x if 40 <= x < 50:
            print(f"Congratulations! you have got grade E in {keys} subject with {grades} marks.")
        case x if x < 40:
            print(f"Ahh better luck next time u have failed u miserable human with {grades} marks.")
    i+=1
