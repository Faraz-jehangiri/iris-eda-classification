from token import NUMBER


def calculator(num):

    def add(numbers):
        result=0
        for i in numbers:
            result+=float(i)
        return result

    def subtract(numbers):
        result=float(numbers[0])
        for i in numbers[1:]:
            result-=float(i)
        return result

    def multiply(numbers):
        result=1
        for i in numbers:
            result*=float(i)
        return result

    def divide(numbers):
        result=float(numbers[0])
        for i in numbers[1:]:
            result/=float(i)
        return result

    add=add(num)


    subtract=subtract(num)


    multiply=multiply(num)


    divide=divide(num)
    answers=[add,subtract,multiply,divide]
    return answers
if __name__=='__main__':
    num=[]
    print("If u want to stop entering numbers type 'S' to stop: ")
    while True:
        try:
            res=input("Enter a number: ")
            if res!="":
                num.append(res)
            if res=="":
                break
        except not int or not float:
            print("not a number.")
    if num==[]:
       print("you have not entered ny numbers")
    else:
        s=calculator(num)
        print(s)


