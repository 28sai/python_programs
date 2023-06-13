lemons=int(input("enter lemons:"))
rem=lemons-21
ex=21-lemons
if lemons==21:
    print("ewually distributed")
elif lemons<0:
    print("you need to give a positive number")
elif(lemons>21):
    print(f"no of lemons in hand={rem} ")
elif(lemons<21):
    print(f"you need {ex} more lemons to distribute")
