age = int(input("enter your age :"))
if age >= 20:
    print("you can enroll in bachelors degree.")
    program = str(input("do you want to explor the bachelors program?"))
    departments = ["we offer three programs" ,"engineering", "computer science" , "medical"]
    print(departments)
    dept = str(input("which program you want to explor"))
    if dept == "engineering":
     print(dict)
     dict = {
        "program1": {
            "course1" : "electrical engineering",
            "fees_structure" : "lum sum 50k per semester",
            "duration" : "four years degree program",
            "documentation" : "original inter marksheet",
        },
        "program2": {
             "course2" : "mechanical engineering",
             "fees_structure": "lum sum 60k per semester",
             "duration": "four years degree program",
             "documentation": "original inter marksheet",
         },
        "program3": {
            "course3": "civil engineering",
            "fees_structure": "lum sum 60k per semester",
            "duration": "four years degree program",
            "documentation": "original inter marksheet",
        },
        "program4": {
            "course4": "industrial engineering",
            "fees_structure": "lum sum 90k per semester",
            "duration": "four years degree program",
            "documentation": "original inter marksheet",
        }
     }
     for x, obj in dict.items():
         print(x)
         print()
         for y in obj:
             print(y + ':', obj[y])

    if dept == "computer science":

        dict1 = {
        "program1": {
            "course1" : "software engineering",
            "fees_structure" : "lum sum 50k per semester",
            "duration" : "four years degree program",
            "documentation" : "original inter marksheet",
        },
        "program2": {
             "course2" : "cyber security",
             "fees_structure": "lum sum 60k per semester",
             "duration": "four years degree program",
             "documentation": "original inter marksheet",
         },
        "program3": {
            "course3": "A.I",
            "fees_structure": "lum sum 60k per semester",
            "duration": "four years degree program",
            "documentation": "original inter marksheet",
        },
        "program4": {
            "course4": "data scientist",
            "fees_structure": "lum sum 90k per semester",
            "duration": "four years degree program",
            "documentation": "original inter marksheet",
        }
        }

        for x , obj in dict1.items():
            print(x)
            for y in obj:
                print(y + ':' , obj[y])
# elif age > 30 and  age <= 40:
#     print("you can enroll in masters")
# elif 31 < age <=40:
#     print("you can enroll in phd")
# else:
#     print("you cannot enroll in higher education")