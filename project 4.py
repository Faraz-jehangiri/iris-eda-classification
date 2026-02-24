# Task1: create a dictionry named directory
directory = {"Faraz": "0007","Khurram":"1728"}

# Task2: Add another employee
directory["Smith"]="4002"

# Task3: use .get() method
if directory.get("Jones") not in directory:
    print("User not Found.")
else:
    print("User found.")

# Task4: delete an employee record
directory.pop("Khurram")

# Task5: print the final dictionary
for i,y in directory.items():
    print(f"{i} => {y}")
