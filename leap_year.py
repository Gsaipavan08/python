year =int(input("ennter the year:"))

if ((year % 4==0 ) and (year % 100 != 0 or year %400 ==0)) :
    print(year,"is leap year")
else:
    print("Not a leap year")