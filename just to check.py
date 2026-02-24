print("MY CALCULATOR ".center(60, "*"))
print("\n")  # Fixed: /n → "\n"
print("the operations are as follows:")
print("1. multiplication")
print("2. addition") 
print("3. subtraction")
print("4. division")

def mycalculator(ist, ch):
    print(f"Chosen operation: {ch}")  # Moved print here, formatted
    match ch:
        case 1:  # multiplication
            result = ist[0]
            for i in ist[1:]:
                result *= i  # Fixed: *= i (not 1)
            return result
        case 2:  # addition
            result = ist[0]
            for i in ist[1:]:
                result += i  # Fixed: += i (not *=1)
            return result
        case 3:  # subtraction
            result = ist[0]
            for i in ist[1:]:
                result -= i  # Fixed: -= i (not 1)
            return result
        case 4:  # division
            result = ist[0]
            for i in ist[1:]:
                if i != 0:  # Avoid div-by-zero
                    result /= i
                else:
                    return "Error: Division by zero"
            return result
        case _:
            return "Invalid choice!"  # Return instead of print for consistency

choice = int(input("Enter the number for your desired operation: "))
mylist = [2, 3, 4, 5, 6]
fout = mycalculator(mylist, choice)
print(f"The result of your desired operation is {fout}")
