BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"
print(f"{BOLD}{UNDERLINE}{ITALIC}=== The Inventory Manager ==={RESET}")
Inventory=["laptop","mouse","keyboard"]
inp=int(input("If u want to see the original inventory press 1: "))
print()
m=0
if inp == 1:
    print(f"{BOLD}{UNDERLINE}=== Original Inventory ==={RESET}")
    for i in Inventory:
        print(f"{m}) {i} ", end=" ")
        m+=1
else:
    print("enter a valid number.")
print()
print()
print("New Shipment arrived!! and is added to the list successfully 😊.")
Inventory.append("monitor")
print()
inp1=int(input("If u want to see the updated inventory press 2: "))
print()
c=0
if inp1 == 2:
    print(f"{BOLD}{UNDERLINE}=== Updated Inventory ==={RESET}")
    for i in Inventory:
        print(f"{c}) {i} ", end=" ")
        c+=1
else:
    print("enter a valid number.")

print()
print()
inp3=int(input("Congrats! 🎉 a sale has taken place and mouse is sold! press 3 to see the updated Inventory."))
print()
Inventory.remove("mouse")
n=0
if inp3==3:
    print(f"{BOLD}{UNDERLINE}=== Updated Inventory ==={RESET}")
    for i in Inventory:
        print(f"{n}) {i} ", end=" ")
        n+=1
else:
    print("enter a valid number.")

Inventory.sort()
print()
print()
inp4=int(input("To see a sorted Inventory press 4: "))
print()
x=0
if inp4==4:
    print(f"{BOLD}{UNDERLINE}=== Updated Inventory ==={RESET}")
    for i in Inventory:
        print(f"{x}) {i} ", end=" ")
        x+=1
else:
    print("enter a valid number.")
print()
print()
inp5=int(input("To see a sorted Inventory press 5: "))
z=0
if inp5==5:
    print(f"{BOLD}{UNDERLINE}=== Length of Inventory ==={RESET}")
    print(f"Length of Inventory is: {len(Inventory)}")
    print()
    print(f"{BOLD}{UNDERLINE}=== Final Inventory ==={RESET}")
    for i in Inventory:
        print(f"{z}) {i} ", end=" ")
        z+=1


