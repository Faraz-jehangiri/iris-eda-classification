flight_path = [(12.5, 55.6), (54.9, 60.0), (33.3, 40.6)]

# Task 1: Print latitude of 2nd coordinate
print(flight_path[1][0])

# Task 3: Attempt to change 1st tuple's longitude to 0.0 (will fail)
try:
    flight_path[0][1] = 0.0  # Direct tuple change → TypeError
except TypeError:
    print("Data cannot be changed because tuples are immutable to ensure flight log\n"
          "accuracy for legal reasons.")
