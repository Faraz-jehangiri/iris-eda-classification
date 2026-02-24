# # # import sys
# # # print("dgdgdf","\t\n","dsda")
# # # print("dadgja")
# # # y=5
# # # print(type (y))
# # # a=float(5)
# # # print(a)
# # #
# # # z=2+5j
# # # print(z.imag)
# # #
# # # print(sys.getsizeof(z))
# # # x,y,z=2,"sda",33.2
# # # print(type(x))
# # # print(type(z))
# # # print(type(y))
# # # print(1j)
# #
# #
# # # a=input("enter a num")
# # # b=input("enter a num")
# # # print(type(a))
# #
# # # a="10010"
# # # b=int(a,16)
# # # print(b)
# #
# # # x=2
# # # y=int("3")
# # # print(x+y)
# # # x=str(76242342642)
# # # for i in range(len(x)-1,-1,-1):
# # #     print(x[i])
# #
# # #string reversal
# # # h="fa raz"
# # # print(h[4::-1])
# # # print(f"original: {h}")
# # # print("reversed: ")
# # # for i in range(len(h)-1,-1,-1):
# # #     ar=h[i]
# # #
# # #     print(ar, end="")
# # #     #print(h[i])
# # # a=2
# # # j=str(a)
# # # print("")
# # # print(type(j))
# # # m=h[0].upper()
# # # print(m)
# # # print(h.split("  "))
# # # print(h.endswith("ra"))
# # # j="akjdajkjahdakdhakjd hel"
# # # print(j.find("hel",18,23))
# # # print(j.index("hel",18,23))
# # #
# # #
# # # n="he"
# # # b=n.zfill(3)
# # # print(b[0])
# # # print(type(b[0]))
# # #
# # # hello=["dhaudhk","akjdaj","bbbj"]
# # # hel=["dhaudhk","akjdaj","adhakhak"]
# # # he=["dhaudhk","akjdaj","adhakhak"]
# # # tuple=" ".join(hello)
# # # print(tuple)
# # #
# # # dict={"aada":"jj","ggggggggg":"adhakjdhakdha"}
# # # print(" ".join(dict.keys()))
# # # seyt={4,7,6,5,4}
# # # print(seyt)
# # # x=5>10
# # # print(x)
# # #
# # # kj=["ff",6,"gf"]
# # # for i in range(2,-1,-1):
# # #     print(type(kj[i]))
# # #
# # # for i in hello:
# # #     again=[]
# # #     again.append("*")
# # # print(again)
# # # print()
# # # for i in range(0,5,2):
# # #     print(i,end="")
# #
# # # thislist = ["banana", "Orange", "Kiwi", "cherry"]
# # #
# # # h=thislist
# # # h.pop()
# # #
# # # print(thislist)
# # #
# # #
# # # j=("dad",)
# # # print(type(j))
# #
# # #Assignment 1 task
# # Course="Python Programming"
# # print(len(Course))
# # print(Course[0])
# # print(Course.upper())
# #
# # #Assignment 1 task
# # lst=["apple","banana","cherry"]
# # lst.append("orange")
# # lst[1]="blueberry"
# # print(lst)
# #
# # print(type(10/2))
# #
# # sett={"aad",2,224,4}
# # j=sett.update({"aadadddda","faraz"})
# # print(j)
# # print(sett)
# #
# # dic={"name": {1, 2, 3}}
# # print(type(dic["name"]))
# #
# # thisdict={"name":"faraz"}
# # mydict=thisdict
# # anotherdict=thisdict.copy()
# #
# # anotherdict.pop("name")
# # print(thisdict)
# #
# # age=int(input("age:"))
# # if age>=18:
# #     print("you are adult")
# #
# #     for i in range(5):
# #         print("ab or kia bolun hogye bas adult.")
# #
# # else:
# #     print("chilkoot.")
# #
# # while True:
# #     try:
# #         month=int(input("Enter the month: "))
# #         day=int(input("Enter the day: "))
# #         match day:
# #             case 1|2|3 if month==13:
# #                 print("helo")
# #             case 4:
# #                 break
# #             case _:
# #                 print("nope")
# #     except ValueError:
# #         print("enter a valid number")
# #
# # formula=(2.5/100)*2000000
# # print(int(formula))
# # x=2
# # b=3
# # print("yes") if 5>2 else print("false")
# #
# # for i in range(5):
# #     pass
# # else:
# #     print("yes")
#
# def cal(a,b):
#     c=a+b
#     return c
#
# print(cal(1,2))
#
# def cal(a, b):
#     global c
#     c = a + b
#     return c  # Optional: return the value
# print(cal(1, 2))
#
# print((1,2)*2)
# lst=["ada"]
#
# print(lst.index("ada"))
# dct={1:"dadad",2:"daddaa"}
# print(type(dct))
# print(len({"a": 1, "b": 2}))
# print(dct.keys())
# del dct[1]  # Correct: removes key 1 silently
# print(dct)  # Now: {2: 'daddaa'}
# print(not 5>2)
# for i in 'hi':print(i)
#
# print(3*'a')
# print(bool(0))
# print(type(1_000))
#
# import calculator_class_project
# import datetime
# print(dir(datetime))
# print(datetime.datetime.today())
#
# from calculator_class_project import calculator
# lst=[1,2,3,4]
# print(dir(calculator_class_project))
# print(calculator(lst))
# def counting(n):
#     count=1
#     lst=[]
#     while count<=n:
#         lst.append(count)
#         count+=1
#     return lst
#
# for i in counting(5):
#     print(i)
# import numpy as np
# print(dir(np))
# import math as m
# print(dir(m))
class D:
    def bark(self,n):
        print(f"{n} says woof.")

    def walk(self,n):
        print(f"{n} is walking")




d=D()
P=D()
d.bark("dog")
d.walk("CAt")
P.bark("Wolf")
P.walk("Paladin")