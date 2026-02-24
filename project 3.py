# Task1: creating two sets
opening_ceremony={"Faraz","Ayan","Zaviar","Rohan"}
gala_dinner={"Faraz","suhaib","Zaviar","Jatin"}

# Task2: Find the names attending both events
print(f"Guests attending both events: {opening_ceremony & gala_dinner}")

# Task3: List of guests attending atleast one event
unique=opening_ceremony ^ gala_dinner
Final_lst=[unique]
print(f"Guests attending at least 1 event: {Final_lst}")

#Task4: Guests in opening ceremony but not in gala dinner
print(f"guests in opening ceremony but not in gala dinner: {opening_ceremony-gala_dinner}")