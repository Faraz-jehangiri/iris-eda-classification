# n=0
# for i in range(0,21,2):
#     print(f"2 X {n} = {i}")
#     n+=1
while True:
    try:
        h=int(input("table of which?: "))
        m=int(input("how long?: "))

        if m <= 50:
            for i in range(1, m + 1):
                print(f"{h} X {i} = {h * i}")

        else:
            print("table too long enter a number equal to or less than 50")

    except ValueError:
        print("Please enter a number.")


    again = input("do u want to continue?: ")
    if again.lower() == 'n':
        break
